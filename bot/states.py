from aiogram.fsm.state import State,StatesGroup


# FSM для збереження рецепта
class RecipeCreateStates(StatesGroup):
    title = State()
    description = State()
    ingredients = State()
    steps = State()
    categories = State()
    cooking_time = State()
    difficulty = State()
    image = State()
