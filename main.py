#!/usr/bin/env python3
# main.py

import random
from collections import defaultdict
from meals_data import base_meals, quantities
import csv


def generate_menu(days, people):
    """
    Generates the camp menu and shopping list.
    
    Parameters:
        days (int): number of camp days
        people (int): number of participants
    
    Returns:
        menu (list): list of formatted daily menus
        shopping_list (dict): dictionary with ingredients and total quantities
    """
    menu = []
    shopping_list = defaultdict(int)  # initializes with default value = 0

    for day in range(1, days + 1):
        # --- Breakfast selection ---
        breakfast_choice = random.choice(base_meals["breakfast"])

        # Different breakfast combinations update the shopping list differently
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

        # --- Lunch and Dinner selections ---
        # Randomly choose one item per category
        lunch_carbs = random.choice(base_meals["carbs"])
        lunch_protein = random.choice(base_meals["proteins"])
        lunch_veggie = random.choice(base_meals["veggies"])
        lunch_fruit = random.choice(base_meals["fruits"])

        dinner_carbs = random.choice(base_meals["carbs"])
        dinner_protein = random.choice(base_meals["proteins"])
        dinner_veggie = random.choice(base_meals["veggies"])
        dinner_fruit = random.choice(base_meals["fruits"])

        # Format the menu for the current day
        menu.append(
            f"Day {day}:\n"
            f"  🍞 Breakfast: {breakfast_choice}\n"
            f"  🍽️ Lunch: {lunch_carbs.capitalize()} with {lunch_protein} and {lunch_veggie}\n"
            f"  🍽️ Dinner: {dinner_carbs.capitalize()} with {dinner_protein} and {dinner_veggie}\n"
            f"  🍎 Fruits: {lunch_fruit}, {dinner_fruit}\n"
        )

        # Add all chosen items to the shopping list
        for item in [
            lunch_carbs, lunch_protein, lunch_veggie,
            dinner_carbs, dinner_protein, dinner_veggie,
            lunch_fruit, dinner_fruit
        ]:
            # If the item isn’t in quantities, use a default of 100 g/ml per person
            shopping_list[item] += quantities.get(item, 100) * people

    return menu, shopping_list


def save_results(menu, shopping_list):
    """
    Saves the generated menu and shopping list to text and CSV files.
    
    Creates:
        - menu.txt
        - shopping_list.txt
        - shopping_list.csv
    """
    # Save the menu as UTF-8 encoded text
    with open("menu.txt", "w", encoding="utf-8") as f:
        f.write("🏕️ Scout Camp Menu 🏕️\n\n")
        f.write("\n".join(menu))

    # Save the shopping list as a formatted text file
    with open("shopping_list.txt", "w", encoding="utf-8") as f:
        f.write("🛒 Shopping List 🛒\n\n")
        for item, qty in shopping_list.items():
            f.write(f"{item.capitalize():<20} - {qty} g/ml\n")

    # Save the shopping list as a CSV file for spreadsheet use
    with open("shopping_list.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Ingredient", "Quantity (g/ml)"])
        for item, qty in shopping_list.items():
            writer.writerow([item.capitalize(), qty])


def main():
    """
    Main entry point for the program.
    Asks for user input and generates the files.
    """
    print("🔥 Welcome to Scout Meal Planner 🔥")
    days = int(input("Enter number of camp days: "))
    people = int(input("Enter number of participants: "))

    # Generate menu and shopping list
    menu, shopping_list = generate_menu(days, people)

    # Save results to files
    save_results(menu, shopping_list)

    # Print confirmation messages
    print("\n✅ Menu and shopping list generated!")
    print("📁 Check 'menu.txt', 'shopping_list.txt', and 'shopping_list.csv'")


# Only run the program if this file is executed directly
if __name__ == "__main__":
    main()