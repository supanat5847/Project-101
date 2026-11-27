incomes = []
expenses = []

def add_income():
    try:
        amount = float(input("Enter income amount:"))
    
        if amount <= 0:
            print("Amount must be greater than 0")

        else:
            incomes.append(amount)
            print("Income added successfully!")

    except ValueError:
        print("Please enter number only")
        

def add_expense():
    try:
        amount = float(input("Enter expense amount:"))
    
        if amount <= 0:
            print("Amount must be greater than 0")

        else:
            expenses.append(amount)
            print("Expense added successfully!")

    except ValueError:
        print("Please enter number only")

def show_transactions():
    if not incomes:
        print("No income records")
    else:
        print("\n=====Income Records=====")
        for income in incomes:
            print(income)
    if not expenses:
        print("No expense records")
    else:
        print("\n=====Expense Records=====")
        for expense in expenses:
            print(expense)

def show_balance():
    total_income = sum(incomes)
    total_expense = sum(expenses)
    balance = total_income - total_expense
    print("\n=====Balance Summary=====")
    print("Total Income: ", f"{total_income:.2f}")  
    print("Total Expense: ", f"{total_expense:.2f}")
    print("Balance: ", f"{balance:.2f}")

def delete_income():
    if not incomes:
        print("No income records to delete")
        return

    print("\n=====Income Records=====")
    for index, income in enumerate(incomes):
        print(index, income)

    try:
        index_to_delete = int(input("Enter index of income to delete: "))
    
        if 0 <= index_to_delete < len(incomes):
            del incomes[index_to_delete]
            print("Income record deleted successfully!")
        else:
            print("Invalid index. Please try again.")

    except ValueError:
        print("Please enter number only")

def delete_expense():
    if not expenses:
        print("No expense records to delete")
        return
    
    print("\n=====Expense Records=====")
    for index, expense in enumerate(expenses):
        print(index, expense)

    try:
        index_to_delete = int(input("Enter index of expense to delete: "))
    
        if 0 <= index_to_delete < len(expenses):
            del expenses[index_to_delete]
            print("Expense record deleted successfully!")
        else:
            print("Invalid index. Please try again.")

    except ValueError:
        print("Please enter number only")

choice = 0

while choice != 7:
    print("===========================")
    print("      EXPENSE TRACKER")
    print("===========================")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Transactions")
    print("4. Show Balance")
    print("5. Delete Income")
    print("6. Delete Expense")
    print("7. Exit")

    choice = int(input("Choose menu: "))

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
    elif choice == 7: #ออกจากโปรแกรม
        print("Exit program")
    else:
        print("Invalid menu")