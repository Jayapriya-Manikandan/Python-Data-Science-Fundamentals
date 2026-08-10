import csv


# -------------------------------
# 1. Read expense data from CSV
# -------------------------------

def load_expenses(filename):
    expenses = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["Amount"] = float(row["Amount"])
            expenses.append(row)

    return expenses


# -------------------------------
# 2. Calculate total spending
# -------------------------------

def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["Amount"]

    return total


# -------------------------------
# 3. Category-wise spending
# -------------------------------

def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    return summary


# -------------------------------
# 4. Find highest expense
# -------------------------------

def highest_expense(expenses):
    highest = expenses[0]

    for expense in expenses:
        if expense["Amount"] > highest["Amount"]:
            highest = expense

    return highest


# -------------------------------
# 5. Payment method summary
# -------------------------------

def payment_summary(expenses):
    summary = {}

    for expense in expenses:
        method = expense["Payment_Method"]

        if method in summary:
            summary[method] += 1
        else:
            summary[method] = 1

    return summary


# -------------------------------
# 6. Generate insights
# -------------------------------

def generate_insights(expenses):
    total = calculate_total(expenses)
    categories = category_summary(expenses)
    highest = highest_expense(expenses)

    print("\n" + "=" * 45)
    print("       PERSONAL EXPENSE ANALYZER")
    print("=" * 45)

    print(f"\nTotal Spending: ₹{total:,.2f}")

    print("\nCategory-wise Spending:")
    for category, amount in categories.items():
        print(f"  {category}: ₹{amount:,.2f}")

    print("\nHighest Expense:")
    print(
        f"  {highest['Description']} - "
        f"₹{highest['Amount']:,.2f} "
        f"({highest['Category']})"
    )

    print("\nPayment Method Usage:")
    payments = payment_summary(expenses)

    for method, count in payments.items():
        print(f"  {method}: {count} transactions")

    print("\n" + "=" * 45)


# -------------------------------
# 7. Main program
# -------------------------------

if __name__ == "__main__":

    file_path = "data/expenses.csv"

    expenses = load_expenses(file_path)

    generate_insights(expenses)