import logging
import unittest

from runner_and_tournament2 import Tournament, Runner

def is_frozen(val):
    def decorator(cls):
        if val:
            for attr_name in dir(cls):
                if attr_name.startswith('test_'):
                    attr = getattr(cls, attr_name)
                    setattr(cls, attr_name, unittest.skip('Тесты в этом кейсе заморожены')(attr))
        return cls
    return decorator

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('name', -2)
            for _ in range(1, 11):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as ve:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner2 = Runner(123, 5)  # Передаем что-то кроме строки в name
            for _ in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as te:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        r1 = Runner('name', 10)
        r2 = Runner('name', 5)
        for _ in range(1, 11):
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
        t = Tournament(90, self.obj1, self.obj2, self.obj3)
        results = t.start()
        self.__class__.all_results[3] = {place: runner.name for place, runner in results.items()}
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == 'Ник')

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")

if __name__ == '__main__':

    unittest.main()