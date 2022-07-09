from lib import kernel as Kernel
from lib.param import functions as FUNC
from lib.param import results as RES
from termcolor import cprint



def subfunction(name_func, intent, param, message):
    match name_func:
        case FUNC.subfunction.FIND_NAME:
            param['NAME'] = Kernel.find_name(sentence=message)
            res = False
        case FUNC.subfunction.FIND_NUMBER:
            param['AGE'] = Kernel.find_number(sentence=message)
            res = False
        case FUNC.subfunction.WAIT:
            seconds = Kernel.wait(intent=intent)
            res = seconds
        case _ as unknown_func:
            res = f"'400': bad function:{unknown_func}"
            cprint(res, 'yellow')
    return res, param


def connect(name_func, intent, param, message):
    match name_func:
        case FUNC.connect.SAY:
            sentence = Kernel.say(intent=intent)
            res = sentence
        case FUNC.connect.ASK:
            response, sentence = Kernel.ask(intent=intent, message=message)
            res = sentence
        case FUNC.connect.RESPOND:
            response = Kernel.respond(intent=intent)
            if Kernel.find(sentence=response):
                res = f'find!, {response}'
        case FUNC.connect.SAYWITH:
            sentence = Kernel.saywith(
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
        type_of_func = Kernel.get_type_of_func(intent)
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
    intent = dialog[step]
    Kernel.save_file(item_file_dialog, data=dialog)
    Kernel.save_file(item_file_param, param)
    return intent, step, param, dialog


def load_param(item_file_dialog, item_file_param):
    dialog = Kernel.load_file(item_file_dialog)
    param  = Kernel.load_file(item_file_param)
    step = param[RES.STEP]
    intent = dialog[step]
    return intent, step, param, dialog