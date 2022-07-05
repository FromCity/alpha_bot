from lib.kernel import *
from lib.dialog import dialog
from lib.param import functions as FUNC
from lib.param import results as RES
from lib.dialog import param


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

def bot_core(message):
    dialog = load_file(item_file_dialog)
    param  = load_file(item_file_param)
    print('dialog', dialog)
    print('param', param)
    step = param[RES.STEP]
    intent = dialog[step]
    if step > 0:
        intent_previous = dialog[step-1]
    res = None
    name_func = get_type_of_func(intent)
    print('name_func:',name_func)
    match name_func:
        case FUNC.SAY:
            sentence = say(intent=intent)
            res = sentence
        case FUNC.ASK:
            response = ask(intent=intent, message=message)
            res = response
        case FUNC.FIND_NAME:
            param['NAME'] = find_name(say(intent=intent_previous))
        case FUNC.FIND_NUMBER:
            param['AGE'] = find_number(say(intent=intent_previous))
        case FUNC.WAIT:
            seconds = wait(intent=intent)
            res = seconds
        case FUNC.RESPOND:
            response = respond(intent=intent)
            if find(sentence=response):
                res = f'find!, {response}'
        case FUNC.SAYWITH:
            sentence = saywith(
                                intent=intent,
                                param=param['NAME'])
            res = sentence
        case _ as unknown_func:
            res = f"'400': bad function:{unknown_func}"
    dialog[step] = {res: name_func}
    save_file(item_file_dialog, data=dialog)
    step += 1
    param[RES.STEP] = step
    save_file(item_file_param, param)
    if res is None:
        res = bot_core()
    return res

for i in range(1, MAX_STEP+1):
    x = bot_core(message="Привет")
    if x:
        print('x', x)
