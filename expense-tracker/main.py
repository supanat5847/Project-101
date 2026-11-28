import sqlite3
from datetime import datetime

# =========================
# DATABASE CONNECTION
# =========================

def init_database():
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            type TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            category TEXT
        )
    """)

    conn.commit()

    return conn, cursor

def add_transaction(conn, cursor, transaction_type):
    print("===== Add Transaction =====")

    amount = get_amount()

    if amount is None:
        return

    date = get_date()

    if date is None:
        return 

    description = get_text("Enter description: ")

    if description is None:
        return

    category = get_text("Enter category: ")

    if category is None:
        return

    cursor.execute("""
        INSERT INTO transactions
        (amount, type, date, description, category)
        VALUES (?, ?, ?, ?, ?)
    """, (amount, transaction_type, date, description, category))

    conn.commit()

    print("Transaction added successfully!")

def get_amount():
    try:
        amount = float(input("Enter amount:"))
    
        if amount <= 0:
            print("Amount must be greater than 0")
            return None
        
        return amount

    except ValueError:
        print("Please enter number only")
        return None

def get_date():
    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date

    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD")
        return None

def get_text(prompt):
    text = input(prompt).strip()

    if text == "":
        print("This field cannot be empty")
        return None

    return text

def show_transactions(conn, cursor):

    cursor.execute("""
        SELECT id, amount, type, date, description, category
        FROM transactions
        ORDER BY date DESC, id DESC
    """)

    transactions = cursor.fetchall()

    if not transactions:
        print("No transaction records")
        return

    print("\n===== All Transactions =====")

    for transaction in transactions:
        print("--------------------------------")
        print(f"ID: {transaction[0]}")
        print(f"Amount: {transaction[1]:.2f}")
        print(f"Type: {transaction[2]}")
        print(f"Date: {transaction[3]}")
        print(f"Description: {transaction[4]}")
        print(f"Category: {transaction[5]}")

    print("--------------------------------")


def show_balance(conn, cursor):

    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type = 'income'
    """)
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type = 'expense'
    """)
    total_expense = cursor.fetchone()[0] or 0

    balance = total_income - total_expense

    print("\n===== Balance Summary =====")
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expense: {total_expense:.2f}")
    print(f"Balance: {balance:.2f}")



def delete_transaction(conn, cursor):

    cursor.execute("""
        SELECT id, amount, type, date, description
        FROM transactions
        ORDER BY id DESC
    """)

    transactions = cursor.fetchall()

    if not transactions:
        print("No transaction records to delete")
        return

    print("\n===== Transaction Records =====")

    for transaction in transactions:
        print(
            f"ID: {transaction[0]}, "
            f"Amount: {transaction[1]}, "
            f"Type: {transaction[2]}, "
            f"Date: {transaction[3]}, "
            f"Description: {transaction[4]}"
        )

    try:
        id_to_delete = int(input("Enter ID to delete: "))

        cursor.execute(
            "DELETE FROM transactions WHERE id = ?",
            (id_to_delete,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Transaction deleted successfully!")
        else:
            print("Invalid ID")

    except ValueError:
        print("Please enter number only")


def update_transaction(conn, cursor):

    cursor.execute("""
        SELECT id, amount, type, date, description, category
        FROM transactions
        ORDER BY id DESC
    """)

    transactions = cursor.fetchall()

    if not transactions:
        print("No transaction records to update")
        return

    print("\n===== Transaction Records =====")

    for transaction in transactions:
        print(
            f"ID: {transaction[0]}, "
            f"Amount: {transaction[1]}, "
            f"Type: {transaction[2]}, "
            f"Date: {transaction[3]}, "
            f"Description: {transaction[4]}, "
            f"Category: {transaction[5]}"
        )

    try:
        id_to_update = int(input("Enter ID to update: "))

        cursor.execute(
            "SELECT id FROM transactions WHERE id = ?",
            (id_to_update,)
        )

        if cursor.fetchone() is None:
            print("Invalid ID")
            return

        new_amount = get_amount()

        if new_amount is None:
            return

        new_date = get_date()

        if new_date is None:
            return
            
        new_description = get_text("Enter new description: ")

        if new_description is None:
            return

        new_category = get_text("Enter new category: ")
        if new_category is None:
            return

        cursor.execute("""
            UPDATE transactions
            SET amount = ?, date = ?, description = ?, category = ?
            WHERE id = ?
        """, (
            new_amount,
            new_date,
            new_description,
            new_category,
            id_to_update
        ))

        conn.commit()

        print("Transaction updated successfully!")

    except ValueError:
        print("Please enter number only")

def main():
    conn, cursor = init_database()

    try:
        choice = 0

        while choice != 7:
            print("===========================")
            print("      EXPENSE TRACKER")
            print("===========================")

            print("1. Add Income")
            print("2. Add Expense")
            print("3. Show Transactions")
            print("4. Show Balance")
            print("5. Delete Transaction")
            print("6. Update Transaction")
            print("7. Exit")

            try:
                choice = int(input("Choose menu: "))
            except ValueError:
                print("Please enter number only")
                continue

            if choice == 1:
                add_transaction(conn, cursor, 'income')

            elif choice == 2:
                add_transaction(conn, cursor, 'expense')

            elif choice == 3:
                show_transactions(conn, cursor)

            elif choice == 4:
                show_balance(conn, cursor)

            elif choice == 5:
                delete_transaction(conn, cursor)

            elif choice == 6:
                update_transaction(conn, cursor)

            elif choice == 7:
                print("Goodbye!")

            else:
                print("Invalid menu")

    finally:
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()