from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    main = State()
    write_Name = State()
