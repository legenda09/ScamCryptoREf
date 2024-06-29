from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio


### ---___--- ЮЗЕР МЕНЮ ---___--- ###
async def main_menu_keyboard():
    send_gift = InlineKeyboardButton(text="🎁 Отправить подарок", switch_inline_query="")
    update_balance = InlineKeyboardButton(text="🔄 Обновить баланс", callback_data="update_balance")
    withdraw_funds = InlineKeyboardButton(text="📥 Вывод средств", callback_data="withdraw_funds")
    main_menu = InlineKeyboardMarkup(row_width=2).add(update_balance, withdraw_funds, send_gift)
    return main_menu

async def get_gift_menu_keyboard(username_bot, tg_id):
    get_gift = InlineKeyboardButton(text="🎁 Получить", url=f"https://t.me/{username_bot}?start={tg_id}")
    get_gift_menu = InlineKeyboardMarkup().add(get_gift)
    return get_gift_menu

async def update_follow_menu_keyboard(channel):
    update_follow = InlineKeyboardButton(text="🔍 Проверить", callback_data="update_follow")
    channel_link = InlineKeyboardButton(text="↗ Перейти на канал", url=f"https://t.me/{channel.replace('@', '')}")
    update_follow_menu = InlineKeyboardMarkup(row_width=1).add(update_follow, channel_link)
    return update_follow_menu



### ---___--- АДМИН МЕНЮ ---___--- ###
async def admin_menu_keyboard():
    number_users = InlineKeyboardButton(text="👥 Количество пользователей", callback_data="number_users")
    download_database = InlineKeyboardButton(text="⏬ Скачать базу данных", callback_data="download_database")
    private_message = InlineKeyboardButton(text="✉ Личное сообщение", callback_data="private_message")
    mailing = InlineKeyboardButton(text="📪 Массовая рассылка", callback_data="mailing")
    changing_balance = InlineKeyboardButton(text="💰 Изменение баланса", callback_data="changing_balance")
    deleted_message = InlineKeyboardButton(text="❌ Закрыть сообщение", callback_data="deleted_message")
    admin_menu = InlineKeyboardMarkup(row_width=2).add(number_users, download_database, private_message, mailing,
                                                       changing_balance, deleted_message)
    return admin_menu

async def info_menu_keyboard():
    update_info = InlineKeyboardButton(text="🔄 Обновить", callback_data="update_info")
    deleted_message = InlineKeyboardButton(text="❌ Закрыть сообщение", callback_data="deleted_message")
    info_menu = InlineKeyboardMarkup(row_width=1).add(update_info, deleted_message)
    return info_menu



### ---___--- ОБЩЕЕ МЕНЮ ---___--- ###
async def deleted_message_menu_keyboard():
    deleted_message = InlineKeyboardButton(text="❌ Закрыть сообщение", callback_data="deleted_message")
    deleted_message_menu = InlineKeyboardMarkup(row_width=1).add(deleted_message)
    return deleted_message_menu
