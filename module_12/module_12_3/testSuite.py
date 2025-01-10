import  unittest

import tests_for_runner

runner_test = unittest.TestSuite()
runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_for_runner.RunnerTest))
runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_for_runner.TournamentTest))

run_tests = unittest.TextTestRunner(verbosity=2)
run_tests.run(runner_test)