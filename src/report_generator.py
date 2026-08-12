import pandas as pd
import numpy as np


# Load the dataset
df = pd.read_csv("data/expenses.csv")


# -------------------------------
# Calculate statistics
# -------------------------------

total_spending = df["Amount"].sum()
average_expense = df["Amount"].mean()
highest_expense = df.loc[df["Amount"].idxmax()]

category_summary = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

payment_summary = df["Payment_Method"].value_counts()

median_expense = np.median(df["Amount"])


# -------------------------------
# Generate report
# -------------------------------

report = []

report.append("=" * 55)
report.append("             PERSONAL EXPENSE REPORT")
report.append("=" * 55)

report.append("\nDATASET OVERVIEW")
report.append("-" * 55)
report.append(f"Total Transactions : {len(df)}")
report.append(f"Total Spending    : ₹{total_spending:,.2f}")
report.append(f"Average Expense   : ₹{average_expense:,.2f}")
report.append(f"Median Expense    : ₹{median_expense:,.2f}")

report.append("\nHIGHEST EXPENSE")
report.append("-" * 55)
report.append(
    f"{highest_expense['Description']} "
    f"({highest_expense['Category']}) - "
    f"₹{highest_expense['Amount']:,.2f}"
)

report.append("\nCATEGORY-WISE SPENDING")
report.append("-" * 55)

for category, amount in category_summary.items():
    report.append(f"{category:<20} ₹{amount:,.2f}")

report.append("\nPAYMENT METHOD USAGE")
report.append("-" * 55)

for method, count in payment_summary.items():
    report.append(f"{method:<20} {count} transactions")


# -------------------------------
# Key insight
# -------------------------------

top_category = category_summary.idxmax()
top_category_amount = category_summary.max()

report.append("\nKEY INSIGHT")
report.append("-" * 55)
report.append(
    f"The highest spending category is {top_category} "
    f"with total spending of ₹{top_category_amount:,.2f}."
)

report.append("\n" + "=" * 55)
report.append("Report generated automatically using Python.")
report.append("=" * 55)


# -------------------------------
# Save report to a file
# -------------------------------

with open("outputs/expense_report.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(report))


print("Expense report generated successfully!")
print("Saved to: outputs/expense_report.txt")
