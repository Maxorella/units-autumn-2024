import unittest
import math
from src.calculator import Calculator


class TestAddition(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_addition_2positive_integers(self):
        self.assertEqual(self.calculator.addition(2381, 1015), 3396)

    def test_addition_2negative_int(self):
        self.assertEqual(self.calculator.addition(-233, -20), -253)

    def test_addition_1negative_int(self):
        self.assertEqual(self.calculator.addition(-233, 20), -213)

    def test_addition_two_zero(self):
        self.assertEqual(self.calculator.addition(0, -0), 0)

    def test_addition_with_positive_infinity(self):
        self.assertEqual(self.calculator.addition(+math.inf, 0), +math.inf)

    def test_addition_with_negative_infinity(self):
        self.assertEqual(self.calculator.addition(-math.inf, 0), -math.inf)

    def test_addition_with_infinity_and_negative_infinity(self):
        result = self.calculator.addition(-math.inf, +math.inf)
        self.assertTrue(math.isnan(result))

    def test_addition_with_zero(self):
        self.assertEqual(self.calculator.addition(234.2523, 0), 234.2523)

    def test_addition_empty_string_with_data(self):
        self.assertEqual(self.calculator.addition('', 'good_data'), 'good_data')

    def test_addition_2positive_float(self):
        self.assertEqual(self.calculator.addition(345.386345, 2.22222), 347.608565)

    def test_addition_1negative_float(self):
        self.assertEqual(self.calculator.addition(345.386345, -2.22222), 343.164125)


    def test_addition_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.addition(1, 'a')


class TestMultiplication(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(1124, 0), 0)

    def test_multiplication_2positive_float(self):
        self.assertEqual(self.calculator.multiplication(131.2, 121.5), 15940.8)

    def test_multiplication_1negative_float(self):
        self.assertEqual(self.calculator.multiplication(32.32, -13.5), -436.32)

    def test_multiplication_2negative_float(self):
        self.assertEqual(self.calculator.multiplication(-1.235, -20.4), 25.194)


    def test_multiplication_2positive_int(self):
        self.assertEqual(self.calculator.multiplication(1421, 642), 912282)

    def test_multiplication_2negative_int(self):
        self.assertEqual(self.calculator.multiplication(1421, -642), -912282)
    def test_multiplication_string(self):
        self.assertEqual(self.calculator.multiplication('word', 4), 'wordwordwordword')


class TestDivision(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_division_by_zero(self):
        self.assertEqual(self.calculator.division(1124, 0), None)

    def test_division_2positive_float(self):
        self.assertEqual(self.calculator.division(1.000001, 1), 1.000001)

    def test_division_1negative_float(self):
        self.assertEqual(self.calculator.division(-1.000001, 1), -1.000001)

    def test_division_2negative_float(self):
        self.assertEqual(self.calculator.division(-1.000001, -1), 1.000001)

    def test_division_2positive_int(self):
        self.assertEqual(self.calculator.division(1421, 642), 2.2133956386292835)

    def test_division_1negative_int(self):
        self.assertEqual(self.calculator.division(-1125, 1125), -1)

    def test_division_2negatives_int(self):
        self.assertEqual(self.calculator.division(-1125, -1125), 1)
    def test_division_float_and_int(self):
        self.assertEqual(self.calculator.division(1462.5, 642), 2.27803738317757)

    def test_division_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.division(1, 'a')


class TestSubtraction(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_subtraction_2positive_int(self):
        self.assertEqual(self.calculator.subtraction(2381, 1015), 1366)

    def test_subtraction_1negative_int(self):
        self.assertEqual(self.calculator.subtraction(2381, -1015), 3396)

    def test_subtraction_2negative_int(self):
        self.assertEqual(self.calculator.subtraction(-2381, -1015), -1366)

    def test_subtraction_zeros(self):
        self.assertEqual(self.calculator.subtraction(0, -0), 0)

    def test_subtraction_with_positive_infinity(self):
        self.assertEqual(self.calculator.subtraction(+math.inf, 0), +math.inf)

    def test_subtraction_with_negative_infinity(self):
        self.assertEqual(self.calculator.subtraction(-math.inf, 0), -math.inf)

    def test_subtraction_infinity_and_negative_infinity(self):
        self.assertEqual(self.calculator.subtraction(-math.inf, +math.inf), -math.inf)

    def test_subtraction_1_positive_and_zero_float(self):
        self.assertEqual(self.calculator.subtraction(0.00001, 0), 0.00001)

    def test_subtraction_2positive_float(self):
        self.assertEqual(self.calculator.subtraction(345.386345, 2.22222), 343.164125)

    def test_subtraction_1negative_float(self):
        self.assertEqual(self.calculator.subtraction(345.386345, -2.22222), 347.608565)
    def test_subtraction_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction(1, 'a')


class TestAbsolute(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(-0), 0)

    def test_absolute_positive_integer(self):
        self.assertEqual(self.calculator.absolute(14215), 14215)

    def test_absolute_negative_integer(self):
        self.assertEqual(self.calculator.absolute(-14215), 14215)

    def test_absolute_positive_float(self):
        self.assertEqual(self.calculator.absolute(2421.7452), 2421.7452)

    def test_absolute_negative_float(self):
        self.assertEqual(self.calculator.absolute(-2421.7452), 2421.7452)

    def test_absolute_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute('a')


class TestDegree(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_degree_zero_exponent(self):
        self.assertEqual(self.calculator.degree(1, -0), 1)

    def test_degree_one_exponent(self):
        self.assertEqual(self.calculator.degree(12412, 0), 1)

    def test_degree_positive_exponent(self):
        self.assertEqual(self.calculator.degree(124, 1), 124)

    def test_degree_negative_exponent(self):
        self.assertEqual(self.calculator.degree(2, -1), 0.5)

    def test_degree_float_exponent(self):
        self.assertEqual(self.calculator.degree(16, 1.5), 64)

    def test_degree_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.degree(1, 'a')


class TestLn(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_ln_one(self):
        self.assertEqual(self.calculator.ln(1), 0.0)

    def test_ln_large_number(self):
        self.assertEqual(self.calculator.ln(12412), 9.42641902556827)

    def test_ln_float(self):
        self.assertEqual(self.calculator.ln(124.15157), 4.8215031578669665)
    def test_ln_int(self):
        self.assertEqual(self.calculator.ln(16), 2.772588722239781)

    def test_ln_negative_value(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    def test_ln_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.ln('a')


class TestLog(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_log_int_positive_base(self):
        self.assertEqual(self.calculator.log(12412, 24), 2.9660979734053874)

    def test_log_float_positive_base(self):
        self.assertEqual(self.calculator.log(124.15157, 4), 3.4779793477425747)
    def test_log_eq_one(self):
        self.assertEqual(self.calculator.log(124, 124), 1)

    def test_log_negative_value(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 2)

    def test_log_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.log(1, 'a')


class TestSqrt(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()


    def test_sqrt_int(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_float(self):
        self.assertEqual(self.calculator.sqrt(124.15157), 11.142332341121405)


    def test_sqrt_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt('a')


class TestNthRoot(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_nth_root_one(self):
        self.assertEqual(self.calculator.nth_root(124, 1), 124)

    def test_nth_root_positive_int_degree(self):
        self.assertEqual(self.calculator.nth_root(16, 2), 4)

    def test_nth_root_float_positive_float_degree(self):
        self.assertEqual(self.calculator.nth_root(124.15157, 10.345), 1.593719943467467)

    def test_nth_root_float_negativee_float_degree(self):
        self.assertEqual(self.calculator.nth_root(124.15157, -10.524), 0.6324566542318705)

    def test_nth_root_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('word', 2)


if __name__ == "__main__":
    unittest.main()
