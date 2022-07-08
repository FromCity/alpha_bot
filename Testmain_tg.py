import unittest

from main_tg import get_step_subfunctions
from lib.dialog import dialog
from main_tg import save_param, load_param
from lib.param import functions as FUNC


item_file_dialog = 'test_dialog.json'
item_file_param = 'test_param.json'

class test_get_step_subfunctions(unittest.TestCase):

    '''def test_3(self):
        self.assertEqual(get_step_subfunctions(3, dialog), 4)

    def test_6(self):
        self.assertEqual(get_step_subfunctions(6, dialog), 6)'''

    def test_save_0(self):
        self.assertEqual(
            save_param(
                step = 0,
                res = None,
                param = {"STEP": 0, "NAME": "", "AGE": 0},
                type_of_func = FUNC.TYPE_CONNECTION,
                name_func = FUNC.connect.ASK,
                dialog = dialog,
                item_file_dialog = item_file_param,
                item_file_param = item_file_param),
                load_param(item_file_dialog, item_file_param))

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()