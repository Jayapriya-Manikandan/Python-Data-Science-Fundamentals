import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv("data/expenses.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])


# -------------------------------
# Basic Dataset Information
# -------------------------------

print("\n" + "=" * 50)
print("       DATA SCIENCE ANALYSIS")
print("=" * 50)

print("\nDataset Shape:")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumn Names:")
print(list(df.columns))


# -------------------------------
# Statistical Analysis
# -------------------------------

total_spending = df["Amount"].sum()
average_spending = df["Amount"].mean()
maximum_spending = df["Amount"].max()
minimum_spending = df["Amount"].min()

print("\nSpending Statistics:")
print(f"Total Spending: ₹{total_spending:,.2f}")
print(f"Average Expense: ₹{average_spending:,.2f}")
print(f"Highest Expense: ₹{maximum_spending:,.2f}")
print(f"Lowest Expense: ₹{minimum_spending:,.2f}")


# -------------------------------
# Category Analysis
# -------------------------------

category_spending = df.groupby("Category")["Amount"].sum().sort_values(
    ascending=False
)

print("\nCategory-wise Spending:")
print(category_spending)


# -------------------------------
# NumPy Analysis
# -------------------------------

amounts = np.array(df["Amount"])

print("\nNumPy Analysis:")
print(f"Standard Deviation: ₹{np.std(amounts):,.2f}")
print(f"Median Expense: ₹{np.median(amounts):,.2f}")


# -------------------------------
# Create Category Chart
# -------------------------------

plt.figure(figsize=(8, 5))

category_spending.plot(kind="bar")

plt.title("Category-wise Expense Analysis")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/category_spending.png")
plt.show()


# -------------------------------
# Payment Method Analysis
# -------------------------------

payment_counts = df["Payment_Method"].value_counts()

print("\nPayment Method Usage:")
print(payment_counts)

plt.figure(figsize=(7, 5))

payment_counts.plot(kind="bar")

plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/payment_methods.png")
plt.savefig("outputs/category_spending.png")
plt.show()


print("\nAnalysis completed successfully!")
print("=" * 50)