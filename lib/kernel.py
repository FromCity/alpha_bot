import re
from time import sleep
import json
import os


def _exitsFile(itemFileJs):
    _itemFileJs = itemFileJs
    if os.path.isfile(_itemFileJs):
        raise FileExistsError
    return _itemFileJs


def loadJs(itemFileJs):
    _itemFileJs = itemFileJs
    with open(_itemFileJs, "r") as f:
        dataJs = json.loads(f.read())
        return dataJs


def dumpJs(itemFileJs, dataJs):
    with open(itemFileJs, "w") as f:
        json.dump(dataJs, f)
    return 1

def save_file(item_file, data):
    res = dumpJs(itemFileJs=item_file, dataJs=data)
    return res

def load_file(item_file):
    data = loadJs(itemFileJs=item_file)
    return data

def get_func(dict_) -> str:
    return list(dict_.values())[0][0]


def get_type_of_func(dict_):
    return list(dict_.values())[0][1]


def get_data(dict_):
    return list(dict_)[0]


def set_param(dict_, param):
    data = get_data(dict_=dict_)
    data[param]
    return data


def say(intent):
    sentence = get_data(intent)
    return sentence


def saywith(intent, name):
    sentence = say(intent)
    print('sentence', sentence)
    print('name', name)
    sentence = re.sub(r'NAME', name, sentence)
    return sentence


def wait(intent):
    sec = float(get_data(intent))
    sleep(sec)
    return sec


def ask(intent, message):
    sentence = get_data(intent)
    response = message
    return response, sentence


def respond(intent):
    response = ask(intent=intent)
    return response


def find(sentence):
    question = False
    question = bool(sentence.find("?") + 1)
    return question


def find_name(sentence, names = ['Aleksey', 'Jonson' , 'Ivan', 'Mikki']):
    l = sentence.split()
    for word in l:
        if word in names:
            return word
    return None


def find_number(sentence):
    number = int(re.findall('[0-9]+', sentence)[0])
    return number
