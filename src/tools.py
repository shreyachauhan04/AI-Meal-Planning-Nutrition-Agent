from langchain_core.tools import tool
from src.database import get_recipe_retriever

# Instantiate retriever once
retriever = get_recipe_retriever()


@tool
def search_recipe_database(query: str) -> str:
    """Searches the database for meal ideas or recipes based on semantic meaning and dietary preferences."""
    docs = retriever.invoke(query)
    return "\n".join([d.page_content for d in docs])


@tool
def lookup_ingredient_nutrition(ingredient_name: str, weight_g: float) -> str:
    """Looks up precise calories and macronutrients for raw items (e.g., chicken breast, soya chunks, paneer)."""
    food_db = {
        "chicken breast": {"cals": 165, "protein": 31, "carbs": 0, "fats": 3.6},
        "soya chunks": {"cals": 345, "protein": 52, "carbs": 33, "fats": 0.5},
        "paneer": {"cals": 265, "protein": 18, "carbs": 1.2, "fats": 20},
    }
    name_clean = ingredient_name.lower().strip()
    if name_clean not in food_db:
        return f"Could not find exact database match for '{ingredient_name}'."

    factor = weight_g / 100.0
    base = food_db[name_clean]
    return (
        f"{weight_g}g of {ingredient_name}: {base['cals']*factor:.0f} kcal, "
        f"P: {base['protein']*factor:.1f}g, C: {base['carbs']*factor:.1f}g, "
        f"F: {base['fats']*factor:.1f}g"
    )


@tool
def calculate_body_metrics(weight_kg: float, height_cm: float, age: int, gender: str, goal: str) -> str:
    """Calculates BMI and gender-specific BMR/calorie targets using the Mifflin-St Jeor equation."""
    bmi = weight_kg / ((height_cm / 100.0) ** 2)
    base_bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age)

    bmr = base_bmr + 5 if gender.lower() in ["male", "man"] else base_bmr - 161
    tdee = bmr * 1.375  # Assuming light daily activity
    target_cals = tdee - 400 if goal.lower() == "loss" else tdee + 300

    return f"BMI: {bmi:.1f} | BMR: {bmr:.0f} kcal | Target Energy Intake: {target_cals:.0f} kcal"
