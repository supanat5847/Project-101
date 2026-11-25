incomes = []
expenses = []

def add_income():
    amount = float(input("Enter income amount: "))
    incomes.append(amount)
    print("Income added successfully!")

def add_expense():
    amount = float(input("Enter expense amount :"))
    expenses.append(amount)
    print("Expense added successfully!")

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

choice = 0

while choice != 5:
    print("===========================")
    print("      EXPENSE TRACKER")
    print("===========================")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Transactions")
    print("4. Show Balance")
    print("5. Exit")

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
        print("Goodbye!")
    #------------------------------------------------
    else:
        print("Invalid menu")