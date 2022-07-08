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
    i = step
    while True:
        intent = dialog[i]
        type_of_func = get_type_of_func(intent)
        if type_of_func == FUNC.TYPE_SUBFUNCTION:
            i+=1
        else:
            if i > step:
                return i-1
            elif i == step:
                return i


def save_param(res, param, type_of_func, name_func, dialog, item_file_dialog,
                item_file_param):
    step = param[RES.STEP]
    dialog[step] = {res: [name_func, type_of_func]}
    save_file(item_file_dialog, data=dialog)
    save_file(item_file_param, param)
    return intent, step, param, dialog


def load_param(item_file_dialog, item_file_param):
    dialog = load_file(item_file_dialog)
    param  = load_file(item_file_param)
    step = param[RES.STEP]
    intent = dialog[step]
    return intent, step, param, dialog


def bot_core(message):
    intent, step, param, dialog = load_param(item_file_dialog, item_file_param)
    res = None
    type_of_func = get_type_of_func(intent)
    name_func = get_func(intent)
    print('param', param)
    if type_of_func == FUNC.TYPE_SUBFUNCTION:
        steps = get_step_subfunctions(step, dialog=dialog)
        save_param(res, param, type_of_func, name_func, dialog, item_file_dialog,
                item_file_param)
        while step < steps:
            print('use SUBFUNCTION step:', step)
            print('steps:', steps)
            intent, step, param, dialog = load_param(item_file_dialog, item_file_param)
            cprint(f'intent {intent}', 'red')
            type_of_func = get_type_of_func(intent)
            name_func = get_func(intent)
            print('name_func', name_func)
            res, param = subfunction(name_func, intent, param, message)
            print('param before save:', param)
            save_param(res, param, type_of_func, name_func, dialog, item_file_dialog,
                item_file_param)
            param[RES.STEP]+=1
            step = param[RES.STEP]
    if type_of_func == FUNC.TYPE_CONNECTION:
        print('param from connect:', param)
        intent, step, param, dialog = load_param(item_file_dialog, item_file_param)
        print('next param:', param)
        res, message = connect(name_func, intent, param, message)
        param[RES.STEP]+=1
        print('param before', param)
        save_param(res, param, type_of_func, name_func, dialog, item_file_dialog,
                item_file_param)
    print('res', res)
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