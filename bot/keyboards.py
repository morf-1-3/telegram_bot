from aiogram.types import InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton
from aiogram.types import BotCommand, BotCommandScopeDefault, MenuButtonCommands
from aiogram import Bot
from aiogram import Bot
from aiogram.types import BotCommand, MenuButtonCommands, BotCommandScopeDefault


def main_menu():
    keyboard = [
        [InlineKeyboardButton(text="➕ Додати свій рецепт", callback_data="add_recipe")],
        [InlineKeyboardButton(text="📖 Переглянути рецепти", callback_data="get_recipes")],
        [InlineKeyboardButton(text="📚 Вчити англійську", callback_data="get_english")],
        
        # [InlineKeyboardButton(text="❓ Допомога", callback_data="help")],
        # [InlineKeyboardButton(text="📞 Контакти", callback_data="contacts")],
        # [InlineKeyboardButton(text="ℹ️ Про бота", callback_data="bot_info")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def start_menu():
    keyboard = [
        [InlineKeyboardButton(text="➕ Додати свій рецепт", callback_data="add_recipe")],
        [InlineKeyboardButton(text="📖 Переглянути рецепти", callback_data="get_recipes")],
        
        [InlineKeyboardButton(text="❓ Допомога", callback_data="help")],
        [InlineKeyboardButton(text="📞 Контакти", callback_data="contacts")],
        [InlineKeyboardButton(text="ℹ️ Про бота", callback_data="bot_info")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)



async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустити бота"),
        
        BotCommand(command="menu", description="Відкрити меню"),
        BotCommand(command="help", description="Допомога"),
        BotCommand(command="contacts", description="Контакти"),
        BotCommand(command="info", description="Про бота"),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

    # Встановлення кнопки "Меню" для всіх користувачів (без chat_id)
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())


def button_to_start_menu():
    keyboard = [
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="start")],
     ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def choice_difficulty_buttons():
    keyboard = [
        [InlineKeyboardButton(text="Легка 🌱", callback_data="Легка складність 🌱")],
        [InlineKeyboardButton(text="Середня 🍲", callback_data="Середня складність 🍲")],
        [InlineKeyboardButton(text="Складна 🔥", callback_data="Висока складність 🔥")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# def get_recipe_keyboard(recipes, page, total_pages):
#     # Створення клавіатури
#     keyboard = InlineKeyboardMarkup(row_width=2)
    
#     # Додаємо кнопки для кожного рецепта
#     recipe_buttons = [
#         InlineKeyboardButton(text=recipe["title"], callback_data=f"recipe_{recipe['_id']}")
#         for recipe in recipes
#     ]

#     # Додаємо кнопки рецептів до клавіатури
#     keyboard.add(*recipe_buttons)

#     # Кнопки пагінації
#     pagination_buttons = []

#     if page > 1:
#         pagination_buttons.append(InlineKeyboardButton("⬅️ Назад", callback_data=f"page_{page - 1}"))

#     pagination_buttons.append(InlineKeyboardButton("📜 Показати всі", callback_data="show_all_recipes"))

#     if page < total_pages:
#         pagination_buttons.append(InlineKeyboardButton("➡️ Вперед", callback_data=f"page_{page + 1}"))

#     # Додаємо кнопки пагінації в один ряд
#     keyboard.add(*pagination_buttons)

#     return keyboard

def get_recipe_keyboard(recipes,page,total_pages):
    
    keyboard = [
        [InlineKeyboardButton(text=recipe["title"], callback_data=f"recipe_{recipe["_id"]}")]
        for recipe in recipes
    ]
    pagination_buttons = []
    if page>1:
        pagination_buttons.append(InlineKeyboardButton(text= "⬅️ Назад", callback_data=f"page_{page-1}"))
    pagination_buttons.append(InlineKeyboardButton(text="📜 Всі", callback_data="show__recipes"))
    if page<total_pages:
        pagination_buttons.append(InlineKeyboardButton(text="➡️ Вперед", callback_data=f"page_{page+1}"))

    # Додаємо кнопки пагінації в один ряд
    keyboard.append(pagination_buttons)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)



# /////////////english///////////////////
def english_menu():
    keyboard = [
        [InlineKeyboardButton(text="🇺🇸 Перекладати з англійської", callback_data="get_word_in_english")],
        [InlineKeyboardButton(text=" 🇺🇦 Перекладати з української", callback_data="get_word_in_ukrainian")],        
          ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_word_menu_keyboard(word,lang,flag_show_means):
    keyboard = []
    text = ""
    if lang == "english":
        keyboard.append([InlineKeyboardButton(text=word["name_end"], callback_data=f"get_word_in_{lang}_showmeand_{word["_id"]}")])
        if flag_show_means:
            # keyboard.append([InlineKeyboardButton(text=word["name_ukr"], callback_data=f"calback_data")])
            text = word["name_ukr"]

    if lang == "ukrainian":
        keyboard.append([InlineKeyboardButton(text=word["name_ukr"], callback_data=f"get_word_in_{lang}_showmeand_{word["_id"]}")])
        if flag_show_means:
            # keyboard.append([InlineKeyboardButton(text=word["name_end"], callback_data=f"calback_data")])
            text = word["name_end"]
    keyboard.append([InlineKeyboardButton(text="➡️ Наступне слово", callback_data=f"get_word_in_{lang}")])    
    return InlineKeyboardMarkup(inline_keyboard=keyboard),text

