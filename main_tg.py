import logging
from threading import current_thread # эта библиотека идет вместе с python
from aiogram import Bot, Dispatcher, executor, types # импортируем aiogram
import internal as Internal
from lib import kernel as Kernel
from lib.dialog import dialog as d
from lib.param import functions as FUNC
from lib.param import results as RES
from lib.dialog import param
from termcolor import cprint


step = param[RES.STEP]
MAX_STEP = len(d)
intent = d[step]
item_file_dialog = 'test_dialog.json'
item_file_param = 'test_param.json'
current_dialog_file = 'test_current_dialog.json'


def bot_core(message):
    step, param, dialog = Internal.load_param(item_file_dialog, item_file_param)
    res = None
    intent = d[step]
    type_of_func = Kernel.get_type_of_func(intent)
    name_func = Kernel.get_func(intent)
    if type_of_func == FUNC.TYPE_SUBFUNCTION:
        cprint('SUBFUNC', 'yellow')
        steps = Internal.get_step_subfunctions(step, dialog=d)
        Internal.save_param(res, param, type_of_func, name_func, dialog, item_file_dialog,
            item_file_param)
        step = param[RES.STEP]
        i = step
        for i in range(step, steps+1):
            print('step', step, 'steps+1', steps+1)
            print('i', i)
            step, param, dialog = Internal.load_param(item_file_dialog, item_file_param)
            print(f'intent {intent}')
            intent = d[step]
            type_of_func = Kernel.get_type_of_func(intent)
            name_func = Kernel.get_func(intent)
            cprint(f'name of func:{name_func}', 'yellow')
            res, param = Internal.subfunction(name_func, intent, param, message)
            Internal.save_dialog(res, param, type_of_func, name_func, dialog, item_file_dialog,
                item_file_param)
            param[RES.STEP] = i
            Internal.save_param(res, param, type_of_func, name_func, dialog, item_file_dialog,
                item_file_param)
    step, param, dialog = Internal.load_param(item_file_dialog, item_file_param)
    intent = d[step]
    type_of_func = Kernel.get_type_of_func(intent)
    name_func = Kernel.get_func(intent)
    if type_of_func == FUNC.TYPE_CONNECTION:
        cprint('CONNECT', 'blue')
        cprint(f'name of func:{name_func}', 'blue')
        res, message = Internal.connect(name_func, intent, param, message)
        Internal.save_dialog(res, param, type_of_func, name_func, dialog, item_file_dialog,
            item_file_param)
        param[RES.STEP]+=1
        step = param[RES.STEP]
        Internal.save_param(res, param, type_of_func, name_func, dialog, item_file_dialog,
            item_file_param)
    print('param', param)
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