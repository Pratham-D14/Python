import pandas as pd

df = pd.read_csv("data.csv")

# Function to add a new expense entry
def addExpense():
    try:
        global df
        amount: int = int(input("Enter the amount: "))
        category: str = input("Enter the category (e.g., Food, Transport, Utilities): ").lower()
        date: str = input("Enter the date (DD-MM-YYYY): ")
        description: str = input("Enter a description (optional): ")
        mode_of_payment: str = input("Enter the mode of payment (e.g., Cash, Card, UPI): ").lower()
        payment_type: str = input("Enter the payment type (e.g., Debit, Credit): ").lower()

        # Collecting user inputs into a dictionary
        # Reading inputs from users
        new_entry = {
            "amount": amount, "category": category, "date": date, "description": description,
            "mode_of_payment": mode_of_payment, "payment_type": payment_type
        }

        # Append the new entry to the CSV file
        df = pd.DataFrame(new_entry, index=[0])
        with open('data.csv', 'a') as f:
            f.write('\n')
        df.to_csv("data.csv", mode='a', header=False, index=False)

        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter the correct data types.")

# Function to view all expense entries
def viewExpenses():
    try:
        global df
        print(df)
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Grouping by columns
def groupByCategory():
    try:
        global df
        print(df.columns)
        columnName = str(input("Enter the column name to group by: ")).lower()

        print(df[columnName].unique())
        selectVal = str(input(f'Enter the {columnName} to filter by: ')).lower()
        groupby_date = df[df[columnName] == selectVal]
        print(groupby_date)
        print(f'Your Total expense is {df.groupby(columnName).sum().loc[selectVal]['amount']} for the column grouped by {selectVal}')
    except FileNotFoundError:
        print("No expenses recorded yet.")
    except KeyError:
        print("Invalid Entry. Please try again.")

# Deleting an Entry
def deleteExpense():
    try:
        global df
        print(df)
        index_to_delete = int(input("Enter the index of the expense to delete: "))
        if 0 <= index_to_delete < len(df):
            df = df.drop(index=index_to_delete)
            df.to_csv("data.csv", index=False)
            print("Expense deleted successfully.")
        else:
            print("Invalid index. Please try again.")
    except FileNotFoundError:
        print("No expenses recorded yet.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Generating Reports
def generateReport():
    try:
        global df
        print("Generating report...")

        total_expense = df[df['payment_type'] == 'debit']['amount'].sum()
        total_income = df[df['payment_type'] == 'credit']['amount'].sum()
        net_balance = total_income - total_expense

        print(f'Total Income: {total_income}')
        print(f'Total Expense: {total_expense}')
        print(f'Net Balance: {net_balance}')
        # print(total_expense)
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Main function to run the expense tracker
def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Group by Category")
        print("4. Delete Expense")
        print("5. Generate Report")
        print("6. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            addExpense()
        elif choice == '2':
            viewExpenses()
        elif choice == '3':
            groupByCategory()
        elif choice == '4':
            deleteExpense()
        elif choice == '5':
            generateReport()
        elif choice == '6':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()
