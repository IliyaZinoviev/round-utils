import unittest

from round_utils.round import floor, ceil


class TestRound(unittest.TestCase):

    def test_round_down_on_step(self):
        input_data_results_list = [
            ((32.333, 0.02), 32.32),
            ((32.32, 0.02), 32.32),
            ((5.1, 9.5), 0),
            ((5.1, 3), 3),
            ((9.9333, 0.2), 9.8),
            ((0.0009993, 0.0000020), 0.000998),
            ((-0.0009993, 0.0000020), -0.001),
            ((-5.1, 9.5), -9.5),
            ((5, 3.1), 3.1),
            ((0.00005, 0.000026), 2.6e-05),
            ((-0.00005, 0.000026), -5.2e-05)
        ]
        for args, result in input_data_results_list:
            self.assertEqual(floor(*args), result)

    def test_round_up_on_step(self):
        input_data_results_list = [
            ((32.333, 0.02), 32.34),
            ((32.32, 0.02), 32.32),
            ((5.1, 9.5), 9.5),
            ((5.1, 3), 6),
            ((9.9333, 0.2), 10.0),
            ((0.0009993, 0.0000020), 0.001),
            ((-0.0009993, 0.0000020), -0.000998),
            ((-5.1, 9.5), 0),
            ((5, 3.1), 6.2),
            ((0.00005, 0.000026), 5.2e-05),
            ((-0.00005, 0.000026), -2.6e-05)

        ]
        for args, result in input_data_results_list:
            self.assertEqual(ceil(*args), result)


if __name__ == '__main__':
    unittest.main()
