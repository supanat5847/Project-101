import sqlite3

conn = sqlite3.connect('expense.db')
cursor = conn.cursor()

#สร้างตาราง incomes 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS incomes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL
    )
""")
#สร้างตาราง expenses
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL
    )
""")

conn.commit()

def add_income():
    try:
        amount = float(input("Enter income amount:"))
    
        if amount <= 0:
            print("Amount must be greater than 0")

        else:
           cursor.execute(
                "INSERT INTO incomes (amount) VALUES (?)", 
                (amount,)
           )

           conn.commit()
           print("Income added successfully!")

    except ValueError:
        print("Please enter number only")
        

def add_expense():
    try:
        amount = float(input("Enter expense amount:"))
    
        if amount <= 0:
            print("Amount must be greater than 0")

        else:
            cursor.execute(
                "INSERT INTO expenses (amount) VALUES (?)",
                (amount,)
            )
            conn.commit()
            print("Expense added successfully!")

    except ValueError:
        print("Please enter number only")

def show_transactions():

    # ดึงข้อมูลรายรับ
    cursor.execute("SELECT id, amount FROM incomes")
    incomes = cursor.fetchall()

    # ดึงข้อมูลรายจ่าย
    cursor.execute("SELECT id, amount FROM expenses")
    expenses = cursor.fetchall()

    print("\n===== Income Records =====")
    if not incomes:
        print("No income records")
    else:
        for income in incomes:
            print(f"ID: {income[0]}, Amount: {income[1]}")

    print("\n===== Expense Records =====")
    if not expenses:
        print("No expense records")
    else:
        for expense in expenses:
            print(f"ID: {expense[0]}, Amount: {expense[1]}")

def show_balance():

    # คำนวณรายรับทั้งหมด
    cursor.execute("SELECT SUM(amount) FROM incomes")
    total_income = cursor.fetchone()[0] or 0

    # คำนวณรายจ่ายทั้งหมด
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expense = cursor.fetchone()[0] or 0

    balance = total_income - total_expense

    print("\n===== Balance Summary =====")
    print("Total Income: ", f"{total_income:.2f}")
    print("Total Expense: ", f"{total_expense:.2f}")
    print("Balance: ", f"{balance:.2f}")

def delete_income():

    cursor.execute("SELECT id, amount FROM incomes")
    incomes = cursor.fetchall()

    if not incomes:
        print("No income records to delete")
        return

    print("\n===== Income Records =====")

    for income in incomes:
        print(f"ID: {income[0]}, Amount: {income[1]}")

    try:
        id_to_delete = int(input("Enter ID of income to delete: "))

        cursor.execute(
            "DELETE FROM incomes WHERE id = ?",
            (id_to_delete,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Income record deleted successfully!")
        else:
            print("Invalid ID")

    except ValueError:
        print("Please enter number only")

def delete_expense():
    cursor.execute("SELECT id, amount FROM expenses")
    expenses = cursor.fetchall()

    if not expenses:
        print("No expense records to delete")
        return

    print("\n===== Expense Records =====")

    for expense in expenses:
        print(f"ID: {expense[0]}, Amount: {expense[1]}")

    try:
        id_to_delete = int(input("Enter ID of expense to delete: "))

        cursor.execute(
            "DELETE FROM expenses WHERE id = ?",
            (id_to_delete,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Expense record deleted successfully!")
        else:
            print("Invalid ID")

    except ValueError:
        print("Please enter number only")

def update_income():

    cursor.execute("SELECT id, amount FROM incomes")
    incomes = cursor.fetchall()

    if not incomes:
        print("No income records to update")
        return

    print("\n===== Income Records =====")

    for income in incomes:
        print(f"ID: {income[0]}, Amount: {income[1]}")

    try:
        id_to_update = int(input("Enter ID of income to update: "))
        new_amount = float(input("Enter new amount: "))

        if new_amount <= 0:
            print("Amount must be greater than 0")
            return

        cursor.execute(
            "UPDATE incomes SET amount = ? WHERE id = ?",
            (new_amount, id_to_update)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Income updated successfully!")
        else:
            print("Invalid ID")

    except ValueError:
        print("Please enter number only")

def update_expense():

    cursor.execute("SELECT id, amount FROM expenses")
    expenses = cursor.fetchall()

    if not expenses:
        print("No expense records to update")
        return

    print("\n===== Expense Records =====")

    for expense in expenses:
        print(f"ID: {expense[0]}, Amount: {expense[1]}")

    try:
        id_to_update = int(input("Enter ID of expense to update: "))
        new_amount = float(input("Enter new amount: "))

        if new_amount <= 0:
            print("Amount must be greater than 0")
            return

        cursor.execute(
            "UPDATE expenses SET amount = ? WHERE id = ?",
            (new_amount, id_to_update)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Expense updated successfully!")
        else:
            print("Invalid ID")

    except ValueError:
        print("Please enter number only")

choice = 0

while choice != 9:
    print("===========================")
    print("      EXPENSE TRACKER")
    print("===========================")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Transactions")
    print("4. Show Balance")
    print("5. Delete Income")
    print("6. Delete Expense")
    print("7. Update Income")
    print("8. Update Expense")
    print("9. Exit")

    try:
        choice = int(input("Choose menu: "))
    except ValueError:
        print("Please enter number only")
        continue

    if choice == 1: #เพิ่มรายรับ
        add_income()
    #------------------------------------------------
    elif choice == 2: #เพิ่มรายจ่าย
        add_expense()
    #------------------------------------------------
    elif choice == 3: #แสดงรายการธ list
        show_transactions()
    #------------------------------------------------
    elif choice == 4: #แสดงยอดคงเหลือ
        show_balance()
    #------------------------------------------------
    elif choice == 5:
        delete_income()
    #------------------------------------------------
    elif choice == 6: #ลบรายจ่าย
        delete_expense()
    #------------------------------------------------
    elif choice == 7: #อัพเดตรายรับ
        update_income()
    #------------------------------------------------
    elif choice == 8: #อัพเดตรายจ่าย
        update_expense()
    #------------------------------------------------
    elif choice == 9: #ออกจากโปรแกรม
        print("Goodbye!")
    else:
        print("Invalid menu")

conn.close()
print("Database connection closed.")