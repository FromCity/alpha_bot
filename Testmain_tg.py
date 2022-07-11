import unittest

from internal import get_step_subfunctions
from lib.dialog import dialog
from internal import save_param, load_param, get_number_of_current_intent, added_intent_to_dialog
from lib.param import functions as FUNC


item_file_dialog = 'test_dialog.json'
item_file_param = 'test_param.json'
current_dialog_file = 'test_current_dialog.json'


class test_get_step_subfunctions(unittest.TestCase):

    def test_3(self):
        self.assertEqual(get_step_subfunctions(3, dialog), 4)

    def test_6(self):
        self.assertEqual(get_step_subfunctions(6, dialog), 6)

    '''def test_save_0(self):
        self.assertEqual(
            save_param(
                res = None,
                param = {"STEP": 0, "NAME": "", "AGE": 0},
                type_of_func = FUNC.TYPE_CONNECTION,
                name_func = FUNC.connect.ASK,
                dialog = dialog,
                item_file_dialog = item_file_param,
                item_file_param = item_file_param),
                load_param(item_file_dialog, item_file_param))'''


    def test_get_current_intent(self):
        self.assertEqual(get_number_of_current_intent(dialog), len(dialog))


    def test_added_intent_to_dialog(self):
        self.assertEqual(added_intent_to_dialog(dialog[0], current_dialog_file), 0)

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()