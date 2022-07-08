import logging # эта библиотека идет вместе с python
from aiogram import Bot, Dispatcher, executor, types # импортируем aiogram
from lib.kernel import *
from lib.dialog import dialog
from lib.param import functions as FUNC
from lib.param import results as RES
from lib.dialog import param
from termcolor import cprint


step = param[RES.STEP]
MAX_STEP = len(dialog)
intent = dialog[step]
item_file_dialog = 'test_dialog.json'
item_file_param = 'test_param.json'
save_file(
    item_file=item_file_dialog,
    data=dialog)
save_file(
    item_file=item_file_param,
    data=param)


def subfunction(name_func, intent, param, message):
    match name_func:
        case FUNC.subfunction.FIND_NAME:
            param['NAME'] = find_name(sentence=message)
            res = False
        case FUNC.subfunction.FIND_NUMBER:
            param['AGE'] = find_number(sentence=message)
            res = False
        case FUNC.subfunction.WAIT:
            seconds = wait(intent=intent)
            res = seconds
        case _ as unknown_func:
            res = f"'400': bad function:{unknown_func}"
            cprint(res, 'yellow')
    return res, param


def connect(name_func, intent, param, message):
    match name_func:
        case FUNC.connect.SAY:
            sentence = say(intent=intent)
            res = sentence
        case FUNC.connect.ASK:
            response, sentence = ask(intent=intent, message=message)
            res = sentence
        case FUNC.connect.RESPOND:
            response = respond(intent=intent)
            if find(sentence=response):
                res = f'find!, {response}'
        case FUNC.connect.SAYWITH:
            sentence = saywith(
                                intent=intent,
                                name=param['NAME'])
            res = sentence
        case _ as unknown_func:
            res = f"'400': bad function:{unknown_func}"
    return res, message


def get_step_subfunctions(step, dialog):
    stop = False
    i = step
    while not stop:
        intent = dialog[i]
        type_of_func = get_type_of_func(intent)
        if type_of_func == FUNC.TYPE_SUBFUNCTION:
            i+=1
        else:
            stop = True
    return i


def save_param(step, res, param, name_func, dialog, item_file_dialog,
                item_file_param):
    dialog[step] = {res: name_func}
    save_file(item_file_dialog, data=dialog)
    step += 1
    param[RES.STEP] = step
    save_file(item_file_param, param)


def get_param_from_file(item_file_dialog, item_file_param):
    dialog = load_file(item_file_dialog)
    param  = load_file(item_file_param)
    step = param[RES.STEP]
    intent = dialog[step]
    return intent, step, param, dialog


def bot_core(message):
    intent, step, param, dialog = get_param_from_file(item_file_dialog, item_file_param)
    if step > 0:
        intent_previous = dialog[step-1]
    res = None
    type_of_func = get_type_of_func(intent)
    name_func = get_func(intent)
    if type_of_func == FUNC.TYPE_SUBFUNCTION:
        steps = get_step_subfunctions(step, dialog=dialog)
        for i in range(step, steps+1):
            intent = dialog[i]
            type_of_func = get_type_of_func(intent)
            name_func = get_func(intent)
            res, param = subfunction(name_func, intent, param, message)
            param[RES.STEP]+=1
            save_param(step, res, param, name_func, dialog, item_file_dialog,
                item_file_param)
    if type_of_func == FUNC.TYPE_CONNECTION:
        intent, step, param, dialog = get_param_from_file(item_file_dialog, item_file_param)
        param[RES.STEP]+=1
        res, message = connect(name_func, intent, param, message)
    save_param(step, res, param, name_func, dialog, item_file_dialog,
                item_file_param)
    return res


API_TOKEN = '5462176083:AAG57-aMFkTFQ85LjEjofePVXnXKobxPoys' # Токен 
logging.basicConfig(level=logging.INFO) # Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply("Привет! Это простейший бот на aiogram") # отвечает на сообщение


@dp.message_handler()
async def echo(message: types.Message):
	message_text = message['text']
	bot_message_text = bot_core(message=message_text)
	await message.answer(bot_message_text)


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)