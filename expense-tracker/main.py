incomes = []
expenses = []

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
        amount = float(input("Enter income amount: "))
        incomes.append(amount)
        print("Income added successfully!")
    #------------------------------------------------
    elif choice == 2: #เพิ่มรายจ่าย
        print("Add Expense")
    #------------------------------------------------
    elif choice == 3: #แสดงรายการธ list
        if not incomes:
            print("No income records")
        else:
            print("\nIncomes Records:")
            for income in incomes:
                print(income)
    #------------------------------------------------
    elif choice == 4: #แสดงยอดคงเหลือ
        print("Show Balance")
    #------------------------------------------------
    elif choice == 5:
        print("Goodbye!")
    #------------------------------------------------
    else:
        print("Invalid menu")