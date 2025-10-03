from db import get_db_connection

class ExpenseTracker:
    def __init__(self, ):
        ...

    def add_expense(self, amount, category, date, description, mode_of_payment, payment_type):
        conn = get_db_connection()
        cn = conn.cursor()
        cn.execute(f'INSERT INTO expenses (amount, category, date, description, mode_of_payment, payment_type) VALUES ({amount}, "{category}", "{date}", "{description}", "{mode_of_payment}", "{payment_type}")')
        conn.commit()
        conn.close()
        print("Expense added successfully.")


    def view_expenses(self):
        conn = get_db_connection()
        cn = conn.cursor()
        tracker = cn.execute('SELECT * FROM expenses').fetchall()
        conn.close()
        for expense in tracker:
            print(expense)

    def delete_expense(self, expense_id):
        conn = get_db_connection()
        cn = conn.cursor()
        cn.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        conn.commit()
        conn.close()

    def group_by_category(self):
        ...
