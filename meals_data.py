# meals_data.py

# Dictionary containing the base meal options.
# Each key represents a food category
# and the value is a list of available foods.

base_meals = { 
    # Breakfast options
    "breakfast": ["bread with Nutella", "bread with jam", "tea with bread and jam"],

    # Carbohydrates category
    "carbs": ["pasta", "rice", "bread", "couscous", "polenta"],

    # Proteins category
    "proteins": ["beans", "sausages", "eggs", "tuna", "cheese", "lentils", "chicken"],

    # Available vegetables
    "veggies": ["tomatoes", "peppers", "zucchini", "carrots", "onions", "peas"],

    # Available fruits
    "fruits": ["apples", "bananas", "oranges", "pears", "melons"]
}

# Dictionary defining standard quantities per person
# for various ingredients, in grams (or ml if specified).

quantities = {
    # Breakfast
    "bread": 100,         # grams — 1 large bread roll or 3-4 slices
    "Nutella": 35,        # grams — spread quantity
    "jam": 35,            # grams — alternative to Nutella
    "milk": 250,          # ml per person
    "tea soluble": 5,     # grams — approx. 1 teaspoon

    # Carbohydrates
    "pasta": 140,         # grams per person
    "rice": 120,
    "couscous": 100,
    "polenta": 120,

    # Proteins
    "beans": 100,         # grams per person
    "sausages": 150,
    "eggs": 100,
    "tuna": 100,
    "cheese": 100,
    "lentils": 100,
    "chicken": 160,

    # Vegetables
    "tomatoes": 70,
    "peppers": 70,
    "zucchini": 80,
    "carrots": 60,
    "onions": 50,
    "peas": 70,

    # Fruits
    "apples": 200,
    "bananas": 180,
    "oranges": 200,
    "pears": 200,
    "melons": 250
}
