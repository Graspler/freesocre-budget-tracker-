"""
Simple Budget and Expense Tracker
GCSE Level Code - Using basic Python concepts
"""

# Store transactions as a list of dictionaries
transactions = []

# Store the starting balance
balance = 0.0


def add_income():
    """Add income to the budget"""
    # Get income amount from user
    amount = float(input("Enter income amount: £"))
    description = input("Enter description: ")
    
    # Add to transactions list
    transaction = {
        "type": "income",
        "amount": amount,
        "description": description
    }
    transactions.append(transaction)
    
    # Update balance
    global balance
    balance = balance + amount
    
    print(f"Income of £{amount:.2f} added successfully!")
    print(f"New balance: £{balance:.2f}")


def add_expense():
    """Add an expense to the budget"""
    # Get expense amount from user
    amount = float(input("Enter expense amount: £"))
    description = input("Enter description: ")
    
    # Add to transactions list
    transaction = {
        "type": "expense",
        "amount": amount,
        "description": description
    }
    transactions.append(transaction)
    
    # Update balance
    global balance
    balance = balance - amount
    
    print(f"Expense of £{amount:.2f} added successfully!")
    print(f"New balance: £{balance:.2f}")


def view_balance():
    """Display current balance"""
    print("\n" + "="*40)
    print(f"Current Balance: £{balance:.2f}")
    print("="*40)


def view_transactions():
    """Display all transactions"""
    print("\n" + "="*40)
    print("TRANSACTION HISTORY")
    print("="*40)
    
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        # Loop through all transactions
        for i in range(len(transactions)):
            transaction = transactions[i]
            trans_type = transaction["type"]
            amount = transaction["amount"]
            description = transaction["description"]
            
            # Show income with + and expense with -
            if trans_type == "income":
                print(f"{i+1}. INCOME: +£{amount:.2f} - {description}")
            else:
                print(f"{i+1}. EXPENSE: -£{amount:.2f} - {description}")
    
    print("="*40)


def view_summary():
    """Display a summary of income, expenses, and balance"""
    # Calculate totals
    total_income = 0.0
    total_expenses = 0.0
    
    for transaction in transactions:
        if transaction["type"] == "income":
            total_income = total_income + transaction["amount"]
        else:
            total_expenses = total_expenses + transaction["amount"]
    
    # Display summary
    print("\n" + "="*40)
    print("BUDGET SUMMARY")
    print("="*40)
    print(f"Total Income:    £{total_income:.2f}")
    print(f"Total Expenses:  £{total_expenses:.2f}")
    print(f"Current Balance: £{balance:.2f}")
    print("="*40)


def display_menu():
    """Show the main menu"""
    print("\n" + "="*40)
    print("BUDGET & EXPENSE TRACKER")
    print("="*40)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. View Summary")
    print("6. Exit")
    print("="*40)


def main():
    """Main program loop"""
    print("\nWelcome to Budget & Expense Tracker!")
    
    # Keep running until user chooses to exit
    running = True
    while running:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        # Use if-elif to handle menu choices
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_balance()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            view_summary()
        elif choice == "6":
            print("\nThank you for using Budget Tracker!")
            print("Goodbye!")
            running = False
        else:
            print("\nInvalid choice! Please enter a number from 1 to 6.")


# Run the program
if __name__ == "__main__":
    main()
