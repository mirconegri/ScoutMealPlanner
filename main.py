#!/usr/bin/env python3
# main.py

import random
from collections import defaultdict
from meals_data import base_meals, quantities
import csv

def generate_menu(days, people):
    """
    Generates the camp menu and shopping list
    days: number of camp days
    people: number of participants
    Returns: menu list and shopping_list dictionary
    """
    menu = []
    shopping_list = defaultdict(int)

    for day in range(1, days + 1):
        # --- Breakfast ---
        breakfast_choice = random.choice(base_meals["breakfast"])

        if "Nutella" in breakfast_choice:
            shopping_list["bread"] += quantities["bread"] * people
            shopping_list["Nutella"] += quantities["Nutella"] * people
            shopping_list["milk"] += quantities["milk"] * people

        elif "jam" in breakfast_choice and "tea" not in breakfast_choice:
            shopping_list["bread"] += quantities["bread"] * people
            shopping_list["jam"] += quantities["jam"] * people
            shopping_list["milk"] += quantities["milk"] * people

        elif "tea" in breakfast_choice:
            shopping_list["bread"] += quantities["bread"] * people
            shopping_list["jam"] += quantities["jam"] * people
            shopping_list["tea soluble"] += quantities["tea soluble"] * people

        # --- Lunch and Dinner ---
        lunch_carbs = random.choice(base_meals["carbs"])
        lunch_protein = random.choice(base_meals["proteins"])
        lunch_veggie = random.choice(base_meals["veggies"])
        lunch_fruit = random.choice(base_meals["fruits"])

        dinner_carbs = random.choice(base_meals["carbs"])
        dinner_protein = random.choice(base_meals["proteins"])
        dinner_veggie = random.choice(base_meals["veggies"])
        dinner_fruit = random.choice(base_meals["fruits"])

        menu.append(
            f"Day {day}:\n"
            f"  🍞 Breakfast: {breakfast_choice}\n"
            f"  🍽️ Lunch: {lunch_carbs.capitalize()} with {lunch_protein} and {lunch_veggie}\n"
            f"  🍽️ Dinner: {dinner_carbs.capitalize()} with {dinner_protein} and {dinner_veggie}\n"
            f"  🍎 Fruits: {lunch_fruit}, {dinner_fruit}\n"
        )

        # Add ingredients to shopping list
        for item in [
            lunch_carbs, lunch_protein, lunch_veggie,
            dinner_carbs, dinner_protein, dinner_veggie,
            lunch_fruit, dinner_fruit
        ]:
            shopping_list[item] += quantities.get(item, 100) * people

    return menu, shopping_list

def save_results(menu, shopping_list):
    """
    Saves menu to menu.txt and shopping_list to shopping_list.txt and shopping_list.csv
    """
    # Save menu.txt
    with open("menu.txt", "w") as f:
        f.write("🏕️ Scout Camp Menu 🏕️\n\n")
        f.write("\n".join(menu))

    # Save shopping_list.txt
    with open("shopping_list.txt", "w") as f:
        f.write("🛒 Shopping List 🛒\n\n")
        for item, qty in shopping_list.items():
            f.write(f"{item.capitalize():<20} - {qty} g/ml\n")

    # Save shopping_list.csv
    with open("shopping_list.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Ingredient", "Quantity (g/ml)"])
        for item, qty in shopping_list.items():
            writer.writerow([item.capitalize(), qty])

def main():
    print("🔥 Welcome to Scout Meal Planner 🔥")
    days = int(input("Enter number of camp days: "))
    people = int(input("Enter number of participants: "))

    menu, shopping_list = generate_menu(days, people)
    save_results(menu, shopping_list)

    print("\n✅ Menu and shopping list generated!")
    print("📁 Check 'menu.txt', 'shopping_list.txt', and 'shopping_list.csv'")

if __name__ == "__main__":
    main()
