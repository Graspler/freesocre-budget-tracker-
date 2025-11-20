# GCSE Programming Concepts Reference

This document maps where each GCSE Computer Science programming concept is used in the budget tracker code.

## 1. Variables and Data Types

### Location: Throughout `budget_tracker.py`

```python
# Float variables (line 9)
balance = 0.0

# String variables (line 18)
description = input("Enter description: ")

# Boolean variables (line 120)
running = True
```

**What this teaches:** How to store different types of data (numbers, text, true/false)

---

## 2. Lists

### Location: `budget_tracker.py`, line 6

```python
# Creating an empty list (line 6)
transactions = []

# Adding to a list (line 21-25)
transactions.append(transaction)

# Getting list length (line 62)
if len(transactions) == 0:

# Looping through a list (line 65)
for i in range(len(transactions)):
```

**What this teaches:** How to store multiple items and work with collections

---

## 3. Dictionaries

### Location: `budget_tracker.py`, lines 19-24

```python
# Creating a dictionary (line 19-23)
transaction = {
    "type": "income",
    "amount": amount,
    "description": description
}

# Accessing dictionary values (line 67-69)
trans_type = transaction["type"]
amount = transaction["amount"]
description = transaction["description"]
```

**What this teaches:** How to store related data together with labels

---

## 4. Functions

### Location: Throughout `budget_tracker.py`

```python
# Defining a function (line 12)
def add_income():

# Calling a function (line 125)
display_menu()
```

**Functions in the program:**
- `add_income()` - Adds money received
- `add_expense()` - Adds money spent
- `view_balance()` - Shows current balance
- `view_transactions()` - Lists all transactions
- `view_summary()` - Shows totals
- `display_menu()` - Shows menu options
- `main()` - Runs the program

**What this teaches:** Breaking code into reusable, organized pieces

---

## 5. While Loops

### Location: `budget_tracker.py`, line 121

```python
# While loop (line 121-141)
running = True
while running:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    # ... process choice ...
```

**What this teaches:** Repeating code as long as a condition is true

---

## 6. For Loops

### Location: `budget_tracker.py`, lines 65 and 85

```python
# For loop with range (line 65)
for i in range(len(transactions)):
    transaction = transactions[i]
    # ... process transaction ...

# For loop with items (line 85)
for transaction in transactions:
    if transaction["type"] == "income":
        # ... process ...
```

**What this teaches:** Repeating code a specific number of times or for each item

---

## 7. If/Elif/Else Statements

### Location: `budget_tracker.py`, lines 72 and 127

```python
# If-else (line 72)
if trans_type == "income":
    print(f"{i+1}. INCOME: +£{amount:.2f} - {description}")
else:
    print(f"{i+1}. EXPENSE: -£{amount:.2f} - {description}")

# If-elif-else chain (line 127-141)
if choice == "1":
    add_income()
elif choice == "2":
    add_expense()
elif choice == "3":
    view_balance()
# ... more choices ...
else:
    print("\nInvalid choice!")
```

**What this teaches:** Making decisions based on conditions

---

## 8. Input and Output

### Location: Throughout `budget_tracker.py`

```python
# Getting input (line 15)
amount = float(input("Enter income amount: £"))

# Printing output (line 27)
print(f"Income of £{amount:.2f} added successfully!")
```

**What this teaches:** Interacting with users - getting data and showing results

---

## 9. String Formatting

### Location: Throughout `budget_tracker.py`

```python
# F-strings with formatting (line 28)
print(f"New balance: £{balance:.2f}")

# .2f formats a number to 2 decimal places
```

**What this teaches:** Displaying data in a readable, formatted way

---

## 10. Global Variables

### Location: `budget_tracker.py`, lines 26 and 46

```python
# Using global keyword (line 26)
global balance
balance = balance + amount
```

**What this teaches:** Modifying variables from outside a function's local scope

---

## How to Learn from This Code

1. **Start with one concept** - Pick one section above and find it in the code
2. **Read the comments** - The code has helpful explanations
3. **Modify values** - Try changing amounts or messages to see what happens
4. **Add features** - Try adding new menu options or transaction types
5. **Break it** - Make intentional errors to understand what each part does

## Practice Exercises

### Beginner
- Change the currency symbol from £ to $
- Add a "clear all transactions" option to the menu
- Change the menu colors or borders

### Intermediate
- Add a category field to each transaction (e.g., "Food", "Transport")
- Create a function to delete a specific transaction
- Add a budget limit warning feature

### Advanced
- Save transactions to a text file
- Load transactions when the program starts
- Add date/time stamps to each transaction
- Create charts showing spending by category

---

**Remember:** This is GCSE-level code, which means:
- ✅ Simple and clear
- ✅ Well-commented
- ✅ Uses basic concepts
- ✅ Easy to understand and modify
- ✅ No complex libraries or frameworks
