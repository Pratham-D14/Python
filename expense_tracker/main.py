from db import setup_database
from expense_tracker import ExpenseTracker
from reports import generate_report, group_by_category

def main():
    setup_database()
    tracker = ExpenseTracker()

    while True:
        print("\n====== Expense Tracker: ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Generate Report")
        print("5. Grouping Data")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (e.g., Food, Transport): ").lower()
                date = input("Enter date (YYYY-MM-DD): ")
                description = input("Enter description (optional): ")
                mode_of_payment = input("Enter mode of payment (e.g., Cash, Card): ").lower()
                payment_type = input("Enter payment type (debit/credit): ").lower()

                tracker.add_expense(amount, category, date, description, mode_of_payment, payment_type)
            except ValueError:
                print("❌ Invalid input. Please enter the correct inputs.")
                continue
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            try:
                expense_id = int(input("Enter the ID of the expense to delete: "))
                tracker.delete_expense(expense_id)
                print("✅ Expense deleted successfully.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid ID.")
        elif choice == '4':
            generate_report()
        elif choice == '5':
            group_by_category()
        elif choice == '6':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")
            continue

if __name__ == "__main__":
    main()