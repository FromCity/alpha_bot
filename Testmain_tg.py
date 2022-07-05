import unittest

from main_tg import bot_core

class Testmain_tg(unittest.TestCase):
    
    def test_bot_core(self):
        self.assertEqual(bot_core('hi'), "hello! It's me")

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()