import unittest

from runner_and_tournament import Tournament, Runner

def is_frozen(val)->bool:
    def decorator(cls):
        if val:
            for attr_name in dir(cls):
                if attr_name.startswith('test_'):
                    attr = getattr(cls, attr_name)
                    setattr(cls, attr_name, unittest.skip('Тесты в этом кейсе заморожены')(attr))
        return cls
    return decorator


@is_frozen(False)
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('name')
        for _ in range(1, 11):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner2 = Runner('name')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)


    def test_challenge(self):
        r1 = Runner('name')
        r2 = Runner('name')
        for _ in range(1,11):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)



@is_frozen(True)
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.obj1 = Runner('Усэйн', 10)
        self.obj2 = Runner('Андрей', 9)
        self.obj3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for _, val in cls.all_results.items():
            print(val)

    def test_run_tournament_1(self):
        t = Tournament(90, self.obj1, self.obj3)
        results = t.start()
        self.__class__.all_results[1] = {place: runner.name for place, runner in results.items()}
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == 'Ник')

    def test_run_tournament_2(self):
        t = Tournament(90, self.obj2, self.obj3)
        results = t.start()
        self.__class__.all_results[2] = {place: runner.name for place, runner in results.items()}
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == 'Ник')

    def test_run_tournament_3(self):
        t = Tournament(90, self.obj2, self.obj2, self.obj3)
        results = t.start()
        self.__class__.all_results[3] = {place: runner.name for place, runner in results.items()}
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == 'Ник')

if __name__ == '__main__':
    unittest.main()