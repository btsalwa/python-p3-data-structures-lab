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
    names = [food["name"] for food in spicy_foods]
    return names
    pass

def get_spiciest_foods(spicy_foods):
    sorted_foods = sorted(spicy_foods, key=lambda x: x["heat_level"], reverse=True)
    max_heat_level = sorted_foods[0]["heat_level"]
    
    spiciest_foods = [food for food in sorted_foods if food["heat_level"] == max_heat_level]
    return spiciest_foods
    pass

def print_spicy_foods(spicy_foods):
   
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    pass

def print_spiciest_foods(spicy_foods):
   
    pass

def get_average_heat_level(spicy_foods):
   
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)  
    return spicy_foods
    pass
