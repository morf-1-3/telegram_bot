from aiogram import types, Dispatcher, Router,F
from aiogram.filters import Command
from aiogram import types
from aiogram.types import Message
from keyboards import *
from api_bot import get_recipe_by_id_api,get_random_word_api,get_word_by_id_api
from api_bot import get_recipes_api, add_recipes_api, get_count_recipes_api
from states import RecipeCreateStates
from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
import aiohttp
import json
import logging
router = Router()


# ///////////////////for comand///////////////////


@router.message(Command("start"))
async def start_comand(message: Message):
    await message.answer("👋 Привіт! Обери дію:", reply_markup=start_menu())





# ////////////////// for inline keybord ///////////////////////

@router.callback_query(F.data == "start")
async def start_handler(callback: types.CallbackQuery):
    await callback.message.answer("👋 Привіт! Обери дію:", reply_markup=start_menu())
    await callback.answer()




@router.callback_query(F.data == "help")
async def help_handler(callback: types.CallbackQuery):
    text_answer = (
    "🔎 **Як знайти рецепти?**\n"
    "Пошук смачних страв доступний у розділі **«Переглянути рецепти»**. "
    "Там ви знайдете безліч крутих страв, від домашньої класики до вишуканих ресторанних шедеврів. "
    "Просто оберіть категорію або знайдіть щось на свій смак! 🍽️\n\n"
    
    "📝 **Хочете поділитися своїм рецептом?**\n"
    "Легко! У розділі **«Додати свій рецепт»** ви можете надіслати власну страву. "
    "Ми перевіримо її протягом кількох днів і, якщо все добре, додамо до загального списку, щоб інші могли її спробувати! 👨‍🍳🔥\n\n"
    
    "📩 **Залишились питання? Хочете співпрацювати?**\n"
    "Завжди раді вашим ідеям та пропозиціям! Пишіть нам на email **customercareaboutyou@gmail.com**\n або в Telegram: "
    "(https://t.me/Development_impoving). 🚀"
    )
    await callback.message.answer(text_answer, reply_markup=button_to_start_menu())
    await callback.answer()

@router.callback_query(F.data == "contacts")
async def contacts_handler(callback: types.CallbackQuery):
    text_answer = (
        "📞 Контактна інформація 📞\n\n"
        "📧 Email: customercareaboutyou@gmail.com\n"
        "📱 Telegram: https://t.me/Development_impoving\n\n"
        "Завжди раді допомогти вам! Наші спеціалісти завжди на зв'язку, щоб відповісти на ваші питання та надати підтримку. 🌟"
    )
    await callback.message.answer(text_answer, reply_markup=button_to_start_menu())
    await callback.answer()

@router.callback_query(F.data == "bot_info")
async def bot_info_handler(callback: types.CallbackQuery):
    text_answer = (
    "🍽️ **Вітаємо у світі смачних ідей!**\n\n"
    "Ми створили цього бота, щоб кожен міг легко знаходити улюблені рецепти та ділитися своїми кулінарними шедеврами. "
    "Тут ви знайдете як прості домашні страви, так і ресторанні шедеври, що підкорять ваш смак! 🥗🍲\n\n"
    
    "🔎 **Шукайте рецепти** – обирайте категорії, відкривайте для себе нові смаки та надихайтеся гастрономічними ідеями.\n"
    "📝 **Додавайте власні рецепти** – поділіться улюбленими стравами з іншими користувачами та станьте частиною нашої кулінарної спільноти! 👨‍🍳🔥\n\n"
    
    "Ми старанно працювали, щоб бот сподобався кожному, хто любить смачно готувати та експериментувати на кухні. "
    "Готові спробувати? 🍳 Повертайтесь на головне меню і відкривайте світ смачних можливостей! 🚀"
    )
    await callback.message.answer(text_answer, reply_markup=button_to_start_menu())
    await callback.answer()

# @router.callback_query(F.data == "add_recipe")
# async def help_handler(callback: types.CallbackQuery):
#     await callback.message.answer("Це команда додати рецепт")
#     await callback.answer()


# @router.callback_query(F.data == "get_recipes")
# async def get_recipes_handler(callback: types.CallbackQuery, session :aiohttp.ClientSession):
#     # await callback.message.answer("Це команда отримати рецепти")
#     data = await get_recipes_api(session) 
#     if data:
#         data = json.dumps(data)
#     else:
#         data = "Немає доступних рецептів"
#     await callback.message.answer(data)
#     await callback.answer()


@router.message(Command("menu"))  # Використовуємо новий синтаксис фільтрів
async def show_menu(message: Message):
    # await message.answer("📌 Доступні команди:\n"
    #                      "/start - Запустити бота\n"
    #                      "/help - Допомога\n"
    #                      "/contacts - Контакти\n"
    #                      "/info - Про бота")
    await message.answer("👋 Привіт! Обери дію:", reply_markup=main_menu())



@router.message(Command('help'))
async def help_handler(message: types.Message):
    help_text = (
        "ℹ️ *Довідка по боту*\n\n"
        "🔹 /start - Запустити бота\n"
        "🔹 /menu - Відкрити меню\n"
        "🔹 /contacts - Контакти\n"
        "🔹 /info - Про бота\n"
        "🔹 /help - Показати цю довідку\n\n"
        "❓ Якщо у вас є запитання, звертайтесь до підтримки."
    )

    await message.answer(help_text, parse_mode="Markdown")



@router.callback_query(F.data == "add_recipe")
async def add_recipe_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Введіть назву рецепта:")
    await state.set_state(RecipeCreateStates.title)


@router.message(RecipeCreateStates.title)
async def procces_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Тепер введіть короткий опис рецепту:")
    await state.set_state(RecipeCreateStates.description)


@router.message(RecipeCreateStates.description)
async def procces_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Тепер введіть потрібні інгредієнти і грамовки(через кому):")
    await state.set_state(RecipeCreateStates.ingredients)


@router.message(RecipeCreateStates.ingredients)
async def procces_ingredients(message: types.Message, state: FSMContext):
    ingredients_list = [ingredient.strip() for ingredient in message.text.split(",")]
    await state.update_data(ingredients=ingredients_list)
    await message.answer("Тепер введіть кроки приготування через точку, або повністю інструкцію приготування:")
    await state.set_state(RecipeCreateStates.steps)


@router.message(RecipeCreateStates.steps)
async def procces_steps(message: types.Message, state: FSMContext):
    steps_list = [step.strip() for step in message.text.strip(".").split(".")]
    await state.update_data(steps=steps_list)
    await message.answer("Тепер введіть до яких категорій належить страва(для зручності пошуку)(категорії вказуйте через кому):")
    await state.set_state(RecipeCreateStates.categories)


@router.message(RecipeCreateStates.categories)
async def procces_categories(message: types.Message, state: FSMContext):
    categories_list = [category.strip() for category in message.text.split(",")]
    await state.update_data(categories=categories_list)
    await message.answer("Тепер введіть скільки часу потрібно що б приготувати страву:")
    await state.set_state(RecipeCreateStates.cooking_time)


@router.message(RecipeCreateStates.cooking_time)
async def procces_cooking_time(message: types.Message, state: FSMContext):
    await state.update_data(cooking_time=message.text)
    await message.answer("Оберіть складність приготування :", reply_markup=choice_difficulty_buttons())
    await state.set_state(RecipeCreateStates.difficulty)


@router.callback_query(RecipeCreateStates.difficulty)
async def procces_difficulty(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(difficulty=callback.data)
    await callback.message.answer("Завантажте фотографію рецепту або пропустіть цей крок :")
    await state.set_state(RecipeCreateStates.image)


@router.message(RecipeCreateStates.image)
async def procces_title(message: types.Message, state: FSMContext, bot: Bot,session :aiohttp.ClientSession):
    if message.photo:
        
        await message.answer("Фото успішно завантажилось")
        file_id = message.photo[-1].file_id
        image = await bot.get_file(file_id)

        # await message.answer(await bot.get_file(file_id))
        # await message.answer_photo(file_id, caption="Ось ваше фото. Тепер введіть інструкції.")

    else:
        await message.answer("Фото не додалось")
        file_id = None
        image = None
    
    await state.update_data(image_id_in_telegram=file_id)
    await state.update_data(image_file=image)

    state_data = await state.get_data()
    title =  state_data.get("title")
    description =  state_data.get("description")
    ingredients =  state_data.get("ingredients")
    steps =  state_data.get("steps")
    categories =  state_data.get("categories")
    cooking_time =  state_data.get("cooking_time")
    difficulty =  state_data.get("difficulty")
    image_id_in_telegram =  state_data.get("image_id_in_telegram")

    image_file =  state_data.get("image_file")
    text_out = (
        "🍽 *" + title + "*\n"
        + description + "\n\n"
        "📌 *Категорії:* " + ", ".join(categories) + "\n"
        "⏳ *Час приготування:* " + cooking_time + " хв\n"
        "🔥 *Складність:* " + difficulty + "\n\n"
        "🛒 *Інгредієнти:*\n" 
        + chr(10).join(["- " + ingredient for ingredient in ingredients]) + "\n\n"
        "👨‍🍳 *Кроки приготування:*\n"
        + chr(10).join([str(i+1) + ". " + step for i, step in enumerate(steps)]) + "\n"
    )
    
    try:
        await message.answer_photo(
            photo=image_id_in_telegram,
            caption=text_out,
            parse_mode="Markdown"
        )
    except Exception as e:
        await message.answer("❌ Не вдалося завантажити фото. Ось ваш рецепт:\n\n" + text_out, 
            parse_mode="Markdown"
        )
        logging.info(f"Помилка при відправки фото {e}")
    
    user_id = message.from_user.id
   
    rezult = data = {
        "title": title,
        "description": description,
        "ingredients": ingredients,
        "steps": steps,
        "categories": categories,
        "cooking_time": cooking_time,
        "difficulty": difficulty,
        "image_id_in_telegram": image_id_in_telegram,
        "user_id": user_id
    }
    if not image_id_in_telegram:
        rezult["image_id_in_telegram"] = None
    await add_recipes_api(data=rezult,session=session)
    await state.clear()




@router.callback_query(F.data == "get_recipes")
async def get_recipes_handler(callback: types.CallbackQuery, session :aiohttp.ClientSession,page:int = 1):
    
    limit = 7
    page = 1
    response = await get_count_recipes_api(session)
    total_count = response.get('count') if response and isinstance(response, dict) else 0
    total_pages = (total_count + limit - 1) // limit
    recipes = await get_recipes_api(session=session,page=page,limit=limit)
    await callback.message.edit_text(
        "Оберіть рецепт:",
        # reply_markup=get_recipe_keyboard(recipes, page, total_pages)
        reply_markup=get_recipe_keyboard(recipes,page,total_pages)
    )
    await callback.answer()


@router.callback_query(F.data.startswith("page_"))
async def paginate_handler(callback: types.CallbackQuery, session :aiohttp.ClientSession,page:int = 1):
    page = int(callback.data.split("_")[1])
    limit = 7
    response = await get_count_recipes_api(session)
    total_count = response.get('count') if response and isinstance(response, dict) else 0
    total_pages = (total_count + limit - 1) // limit
    recipes = await get_recipes_api(session=session,page=page,limit=limit)
    await callback.message.edit_text(
        "Оберіть рецепт:",
        # reply_markup=get_recipe_keyboard(recipes, page, total_pages)
        reply_markup=get_recipe_keyboard(recipes,page,total_pages)
    )
    await callback.answer()


@router.callback_query(F.data.startswith("recipe_"))
async def paginate_handler(callback: types.CallbackQuery, session :aiohttp.ClientSession,page:int = 1):
    # logging.info(callback.data)
    recipe_id = str(callback.data.split("_")[1])
    
    recipe = await get_recipe_by_id_api(session=session, recipe_id=recipe_id)

    text_out = (
        "🍽 *" + recipe["title"] + "*\n"
        + recipe["description"] + "\n\n"
        "📌 *Категорії:* " + ", ".join(recipe["categories"]) + "\n"
        "⏳ *Час приготування:* " + recipe["cooking_time"] + " хв\n"
        "🔥 *Складність:* " + recipe["difficulty"] + "\n\n"
        "🛒 *Інгредієнти:*\n" 
        + chr(10).join(["- " + ingredient for ingredient in recipe["ingredients"]]) + "\n\n"
        "👨‍🍳 *Кроки приготування:*\n"
        + chr(10).join([str(i+1) + ". " + step for i, step in enumerate(recipe["steps"])]) + "\n"
    )
    
    try:
        if len(text_out)< 1024:
            await callback.message.answer_photo(
                photo=recipe["image_id_in_telegram"],
                caption=text_out,
                parse_mode="Markdown"
            )
        # --------------------------------
        else:
            await callback.message.answer_photo(photo=recipe["image_id_in_telegram"])

            # Якщо текст досить довгий, відправляємо його окремим повідомленням
            await callback.message.answer(text_out, parse_mode="Markdown")
# ----------------------------------------,

        

        
    except Exception as e:
        await callback.message.answer("❌ Не вдалося завантажити фото. Ось ваш рецепт:\n\n" + text_out, 
            parse_mode="Markdown"
        )
        logging.info(f"Помилка при відправки фото {e}")
    
    await callback.answer()
    
# ////////////////////////////////// english
@router.callback_query(F.data == "get_english")
async def get_recipes_handler(callback: types.CallbackQuery):
    await callback.message.answer("Обери дію", reply_markup=english_menu())    
    await callback.answer()

@router.callback_query(F.data.startswith("get_word_in_"))
async def get_rundom_word_handler(callback: types.CallbackQuery, session :aiohttp.ClientSession):
    data_split = (callback.data.split("_"))

    lang = data_split[3]
    
    if len(data_split) >= 5:
        flag_show_means = True
    else:
        flag_show_means = False


    if len(data_split) == 6:
        vacab_id = data_split[5]
        word = await get_word_by_id_api(session,vacab_id)
    
    else:
        word = await get_random_word_api(session)

    
    # await callback.message.edit_text("Обери дію", reply_markup=get_word_menu_keyboard(word=word,lang=lang,flag_show_means=flag_show_means))    
    keybord,text = get_word_menu_keyboard(word=word,lang=lang,flag_show_means=flag_show_means)
    if not text:
        text = "Перекладіть"
    # await callback.message.answer(f" {text}", reply_markup=keybord) 
    current_text = callback.message.text  # Отримуємо поточний текст повідомлення
    text_new = f"{text}"
    logging.info(text_new)
    logging.info(current_text)
    if current_text != f"{text}" or current_text =="Перекладіть":
        await callback.message.edit_text(f" {text}", reply_markup=keybord)    
    await callback.answer()
    