from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import pandas as pd
from datetime import datetime

# sleep tracker lists
days_list = []
hours_list = []
energy_list = []


def instructions():
    print("Welcome to your [title]")
    print(
        "[title] is an online tracker that tracks the user’s daily activities and habits such as fitness, mood, and sleep. Additionally, other organizational features include reminders, timers, and to-do lists."
    )
    input("Press enter to continue ")


def menu():
    while True:
        print("\nMenu:")
        print("1. Sleep Tracker")
        print("2. Habit Tracker")
        print("3. To-Do List")
        print("4. Quit")
        user_choice = input("Enter a number: ")
        if user_choice == "1":
            sleep_tracker()
        elif user_choice == "2":
            habit_tracker()
        elif user_choice == "3":
            todo_list()
        elif user_choice == "4":
            print("Exiting...")
            sys.exit()
        else:
            print("Please enter a valid number.")


def save_analysis(results, filename):
    with open(filename, "w") as file:
        for data in results:
            file.write(str(f"{data.title()}: {results.get(data)}"))


def sleep_tracker():
    print("\n--- Sleep Tracker ---")
    days_and_months = {
        "january": 31,
        "february": 28,
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31,
    }
    while True:
        month = input("What month is it? ").lower()
        if month not in days_and_months:
            print("Invalid input.")
            continue
        try:
            day = int(input("What day do you want to track (number)? "))
            if not 1 <= day <= days_and_months.get(month):
                print("Invalid input.")
                continue
        except ValueError:
            print("Invalid input.")
            continue
        days_list.append(day)
        try:
            hours_input = int(input("How many hours of sleep did you get at night? "))
        except ValueError:
            print("Invalid input.")
            continue
        try:
            energy_input = int(
                input("On a scale of 1-10, how much energy did you wake up with? ")
            )
            if not 1 <= energy_input <= 10:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")
        break

    today = str(datetime.now().date())
    hours_list.append(hours_input)
    energy_list.append(energy_input)
    entry = {"date": today, "hours": hours_list, "energy": energy_list}
    print(f"Logged: {hours_input} hours on {today}.")
    print(entry)
    save_analysis(entry, "test.csv")
    x = np.array(days_list)
    y = np.array(hours_list)
    plt.title("Sleep Tracker")
    # plt.xlabel(f"Days of {month.title()}")
    plt.ylabel("Hours")
    plt.scatter(x, y)
    plt.show()
    input("Press enter to go back to the menu")
    menu()


def view_tracker():
    print(user_habits)
    print("Press Enter to Continue.")
    habit_tracker()


def track_habit():
    pass


# mood tracker habit lists
user_habits = []


def add_habit():
    habit_name = input("Enter the habit name you would like to add: ")
    user_habits.append(habit_name)
    print(f"Habit {habit_name} added successfully")
    print("Press Enter to Continue")
    habit_tracker()


def habit_tracker():
    print("\n--- Habit Tracker Menu ---")
    print("\n1. View Habits")
    print("2. Mark Habit as completed")
    print("3. Add Habit")
    print("4. Go back to Main Menu")
    while True:
        habit_choice = int(input("Enter a number: "))
        if habit_choice == 1:
            view_tracker()
        elif habit_choice == 2:
            track_habit()
        elif habit_choice == 3:
            add_habit()
        elif habit_choice == 4:
            menu()
        else:
            print("Please enter a valid number.")


def todo_list():
    print("--- To-Do List ---")
    print("\n1. Add To-Do")
    print("2. View To-Do List")
    print("3. Mark item as compeleted")
    print("4. Go back to main menu")
    while True:
        todo_choice = input("Please enter a number.")
        if todo_choice == "1":
            pass
        elif todo_choice == "2":
            pass
        elif todo_choice == "3":
            pass
        elif todo_choice == "4":
            menu()
        else:
            print("Please print a valid number")


instructions()
menu()
