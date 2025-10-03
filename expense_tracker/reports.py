from db import get_db_connection
import sqlite3

def generate_report():
    try:
        conn = get_db_connection()
        cn = conn.cursor()

        cn.execute('SELECT SUM(amount) FROM expenses WHERE payment_type="debit"')
        total_expense = cn.fetchone()[0] or 0

        cn.execute('SELECT SUM(amount) FROM expenses WHERE payment_type="credit"')
        total_income = cn.fetchone()[0] or 0

        net_balance = total_income - total_expense

        print("====== Expense Report ======")
        print(f'Total Income: {total_income}')
        print(f'Total Expense: {total_expense}')
        print(f'Net Balance: {net_balance}')

        conn.close()
    except TypeError:
        print('Something went wrong')

def group_by_category():
    try:
        conn = get_db_connection()
        cn = conn.cursor()

        cn.execute("SELECT * FROM expenses LIMIT 1")
        print([description[0] for description in cn.description])
        column_name = input("Enter the column name to add filter: ")
        cn.execute(f'SELECT DISTINCT {column_name} FROM expenses')
        values = [row[0] for row in cn.fetchall()]
        print(values)
        selected_value = input("Please select the value to filter by: ")
        cn.execute(f"SELECT * FROM expenses where {column_name} == '{selected_value}'")
        rows = cn.fetchall()

        cn.execute(f"SELECT SUM(amount) FROM expenses WHERE {column_name} == '{selected_value}'")
        total_expense = cn.fetchone()[0] or 0
        print(rows)
        print("Total: ", total_expense)

        conn.close()
    except ValueError:
        print("Something went wrong")
    except sqlite3.OperationalError:
        print("please enter valid inputs")
