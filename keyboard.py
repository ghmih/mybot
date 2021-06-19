from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Назад', callback_data='back')
        ]
    ]
)
