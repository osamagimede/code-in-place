import datetime

# Initialize the list to store expenses
expenses = []

# define a function used to add expenses
def add_expense(amount, description, date, category):
    expense = {
        'amount': amount,
        'description': description,
        'date': date,
        'category': category
    }
    expenses.append(expense)
    print("Expense added successfully!")

# define a function to view expenses 
def view_expenses():
    if not expenses:
        print("No expenses to show.")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: {expense['amount']}, Description: {expense['description']}, Date: {expense['date']}, Category: {expense['category']}")

# define a function to calculate the total expenses 
def total_expenses():
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total expenses: {total}")

#define a function that filters the expenses when the user request for it
def filter_expenses(filter_type, filter_value):
    filtered = []
    if filter_type == "date":
        for expense in expenses:
            if expense['date'] == filter_value:
                filtered.append(expense)
    elif filter_type == "category":
        for expense in expenses:
            if expense['category'] == filter_value:
                filtered.append(expense)
    
    if not filtered:
        print(f"No expenses found for {filter_type} = {filter_value}")
        return
    
    for i, expense in enumerate(filtered, start=1):
        print(f"{i}. Amount: {expense['amount']}, Description: {expense['description']}, Date: {expense['date']}, Category: {expense['category']}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View total expenses")
        print("4. Filter expenses by date")
        print("5. Filter expenses by category")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            add_expense(amount, description, date, category)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            date = input("Enter date (YYYY-MM-DD) to filter: ")
            filter_expenses("date", date)
        elif choice == '5':
            category = input("Enter category to filter: ")
            filter_expenses("category", category)
        elif choice == '6':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
