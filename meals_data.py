# meals_data.py

# Dizionario che contiene le opzioni base dei pasti.
# Ogni chiave rappresenta una categoria di cibo
# e il valore è una lista degli alimenti disponibili.

base_meals = { 
    # Opzioni per la colazione
    "breakfast": ["bread with Nutella", "bread with jam", "tea with bread and jam"],
    
    # Categoria dei carboidrati
    "carbs": ["pasta", "rice", "bread", "couscous", "polenta"],
    
    # Categoria delle proteine
    "proteins": ["beans", "sausages", "eggs", "tuna", "cheese", "lentils", "chicken"],
    
    # Verdure disponibili
    "veggies": ["tomatoes", "peppers", "zucchini", "carrots", "onions", "peas"],
    
    # Frutta disponibile
    "fruits": ["apples", "bananas", "oranges", "pears", "melons"]
}

# Dizionario che definisce le quantità standard per persona
# dei vari ingredienti, espresse in grammi (o ml se specificato).

quantities = {
    # Colazione
    "bread": 100,         # grammi — 1 panino grande o 3-4 fette
    "Nutella": 35,        # grammi — quantità da spalmare
    "jam": 35,            # grammi — alternativa alla Nutella
    "milk": 250,          # ml per persona
    "tea soluble": 5,     # grammi — circa 1 cucchiaino

    # Carboidrati
    "pasta": 140,         # grammi a persona
    "rice": 120,
    "couscous": 100,
    "polenta": 120,

    # Proteine
    "beans": 100,         # grammi a persona
    "sausages": 150,
    "eggs": 100,
    "tuna": 100,
    "cheese": 100,
    "lentils": 100,
    "chicken": 160,

    # Verdure
    "tomatoes": 70,
    "peppers": 70,
    "zucchini": 80,
    "carrots": 60,
    "onions": 50,
    "peas": 70,

    # Frutta
    "apples": 200,
    "bananas": 180,
    "oranges": 200,
    "pears": 200,
    "melons": 250
}