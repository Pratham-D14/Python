import sqlite3 as db

def get_db_connection():
    return db.connect('expenses.db')

# cn = conn.cursor()
def setup_database():
    conn = get_db_connection()
    cn = conn.cursor()
    cn.execute('''CREATE TABLE IF NOT EXISTS expenses
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount INTEGER NOT NULL,
                    category TEXT NOT NULL,
                    date TEXT NOT NULL,
                    description TEXT,
                    mode_of_payment TEXT NOT NULL,
                    payment_type TEXT NOT NULL CHECK(payment_type IN ('debit', 'credit')))
                ''')

    conn.commit()
    conn.close()
