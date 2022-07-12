from lib.param import functions as FUNC


dialog = [
    {"Добрый день, это я!": [FUNC.connect.SAY, FUNC.TYPE_CONNECTION]},
    {"Как твои дела?": [FUNC.connect.ASK, FUNC.TYPE_CONNECTION]},
    {"Как тебя зовут?": [FUNC.connect.ASK, FUNC.TYPE_CONNECTION]},
    {"NAME": [FUNC.subfunction.FIND_NAME, FUNC.TYPE_SUBFUNCTION]},
    {"2": [FUNC.subfunction.WAIT, FUNC.TYPE_SUBFUNCTION]},
    {"Сколько тебе лет?": [FUNC.connect.ASK, FUNC.TYPE_CONNECTION]},
    {"AGE": [FUNC.subfunction.FIND_NUMBER, FUNC.TYPE_SUBFUNCTION]},
    {"Есть вопросы?": [FUNC.connect.SAY, FUNC.TYPE_CONNECTION]},
    {"Спасибо, NAME, пока!": [FUNC.connect.SAYWITH, FUNC.TYPE_CONNECTION]}]

param = {
    "STEP": 0,
    "NAME": "",
    "AGE": 0}

history = dialog

second_dialog: list