from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    write_Name = State()

    main = State()
