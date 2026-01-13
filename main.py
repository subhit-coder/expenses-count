import csv
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Function to add expense
def add_expense(date, category, amount, notes):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, notes])
    print("✅ Expense added successfully!")

# Function to view all expenses
def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            print("\n--- All Expenses ---")
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Notes: {row[3]}")
    except FileNotFoundError:
        print("No expenses found yet!")

# Function to show summary (total spent)
def summary():
    total = 0
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print(f"\n💰 Total Spent: {total}")
    except FileNotFoundError:
        print("No expenses found yet!")
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summary (Total Spent)")
    print("4. Monthly & Yearly Summary")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (Food/Travel/Shopping/etc): ")
        amount = input("Enter amount: ")
        notes = input("Enter notes: ")
        add_expense(date, category, amount, notes)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        summary()

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice, try again!")
