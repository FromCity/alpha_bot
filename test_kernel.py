import unittest

from lib.kernel import find_name


class test_kernel(unittest.TestCase):

    def test_find_name_1(self):
        self.assertEqual(find_name('Добрый день, Борис, меня зовут'), 'Борис')

    def test_find_name_2(self):
        self.assertEqual(find_name('Алексей'), 'Алексей')

# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()