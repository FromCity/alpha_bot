class  functions:
    TYPE_CONNECTION  = "CONNECT"
    TYPE_SUBFUNCTION = "SUBFUNC"
    """
    Функции бота
    """
    class subfunction:
        """функции общения
        """
        START       = "START"        # Начало диалога
        HELLO       = "HELLO"        # Вступление
        FIND        = "FIND"         # Найти слово в предложении
        FIND_NAME   = "FIND_NAME"    # Найти имя
        FIND_NUMBER = "FIND_NUMBER"  # Найти число
        WAIT        = "WAIT"         # Выждать паузу
        FINISH      = "FINISH"       # Отключить
        TRANSFER    = "TRANSFER"     # Перевести на другого оператора
        COUNT       = "COUNT"        # Сосчитать
        ERROR       = "ERROR"        # Ошибка бота
    class connect:
        """вспомогательные функции
        """
        SAYWITH     = "SAYWITH"      # Отправить сообщение с параметрами
        SOURCES     = "SOURCES"      # Ресурсы - ссылки, аудио, картинки, видео
        FEEDBACK    = "FEEDBACK"     # Обратная связь, оценка работы бота, полезность
        CONCLUSION  = "CONCLUSION"   # Завершение диалога
        SAY         = "SAY"          # Отправить сообщение собеседнику
        ASK         = "ASK"          # Задать вопрос собеседнику
        RESPOND     = "RESPOND"      # Ответить собеседнику
        BUTTON      = "BUTTON"       # Кнопки вместо ввода текста
        MENU        = "MENU"        # Отображение меню выбора из предложенных позиций


class results:
    """
    Результат действия
    """
    SUCCESS     = "SUCCESS"      # Успешное действие
    FAIL        = "FAIL"         # Неуспешное действие
    COUNT       = "COUNT"        # Счётчик
    NAME        = "NAME"         # Имя собеседника
    AGE         = "AGE"          # Возраст собеседника
    STEP        = "STEP"         # Шаг диалога для файла с сохранением


class actions:
    """
    Действия - реакция
    """
    AGREE = "AGREE"              # Согласиться
    DISAGREE = "DISAGREE"        # Отказаться