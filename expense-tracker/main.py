print("===========================")
print("      EXPENSE TRACKER")
print("===========================")

print("1.Add Income")
print("2.Add Expense")
print("3.Show Transactions")
print("4.Show Balance")
print("5.Exit")

choice = int(input("Choose menu: "))

if choice == 1:
    print("Add Income")
elif choice == 2:
    print("Add Expense")
elif choice == 3:
    print("Show Transactions")
elif choice == 4:
    print("Show Balance")
elif choice == 5:
    print("Goodbye!")
else:
    print("Invalid menu")