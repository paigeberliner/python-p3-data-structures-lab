spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest_foods.append(food)
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        heat_level = food['heat_level']
        spicy_food = food['name']
        cuisine = food['cuisine']
        spice_indicator = '🌶' * heat_level
        spiciest_foods.append(f"{spicy_food} ({cuisine}) | Heat Level: {spice_indicator}")

    result = '\n'.join(spiciest_foods)
    print(result)  # Add this line to actually print the result
    return result 

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods: 
        if food['cuisine'] == cuisine: 
            return {
                'name': food['name'],
                'cuisine': food['cuisine'],
                'heat_level': food['heat_level']
            }
    return None
        

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods: 
        heat_level = food['heat_level']
        spicy_food = food['name']
        cuisine = food['cuisine']
        spice_indicator = '🌶' * heat_level
        if food["heat_level"] > 5: 
            print(f"{spicy_food} ({cuisine}) | Heat Level: {spice_indicator}")
        

def get_average_heat_level(spicy_foods):
    heat_level_array = []

    for food in spicy_foods:
        heat_level = food['heat_level']
        heat_level_array.append(heat_level)

    average = sum(heat_level_array) / len(heat_level_array) if len(heat_level_array) > 0 else 0

    return average



def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

