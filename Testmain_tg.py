import unittest

from main_tg import bot_core

class Testmain_tg(unittest.TestCase):
    
    def test_hello(self):
        self.assertEqual(bot_core('hi'), "hello! It's me")

    def test_how_are_you(self):
        self.assertEqual(bot_core('hello'), "how are you?")

    def test_what_is_you_name(self):
        self.assertEqual(bot_core('good'), "what is you name?")
    
    def test_how_old_are_you(self):
        self.assertEqual(bot_core("Ivan"), "how old are you?")

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()