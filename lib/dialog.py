from lib.param import functions as FUNC


dialog = [
    {"hello! It's me": [FUNC.connect.SAY, FUNC.TYPE_CONNECTION]},
    {"how are you?": [FUNC.connect.ASK, FUNC.TYPE_CONNECTION]},
    {"what is you name?": [FUNC.connect.ASK, FUNC.TYPE_CONNECTION]},
    {"NAME": [FUNC.subfunction.FIND_NAME, FUNC.TYPE_SUBFUNCTION]},
    {"2": [FUNC.subfunction.WAIT, FUNC.TYPE_SUBFUNCTION]},
    {"1": [FUNC.subfunction.WAIT, FUNC.TYPE_SUBFUNCTION]},
    {"how old are you?": [FUNC.connect.ASK, FUNC.TYPE_CONNECTION]},
    {"AGE": [FUNC.subfunction.FIND_NUMBER, FUNC.TYPE_SUBFUNCTION]},
    {"any questions?": [FUNC.connect.SAY, FUNC.TYPE_CONNECTION]},
    {"thanks, NAME, buy!": [FUNC.connect.SAYWITH, FUNC.TYPE_CONNECTION]}]

param = {
    "STEP": 0,
    "NAME": "",
    "AGE": 0}

history = dialog

second_dialog: list