from modules.budget import Budget
from modules.month import Month
from modules.transaction import Transaction
# Main runner
class Interface:
    
    def __init__(self):
        self.budget = Budget()



    def run(self):
        while True:
            self.print_menu()
            option = int(input("Select Option: "))
            if option == 1:
                month = int(input("Enter a month: "))
                try:
                    print(self.budget.get_monthly_cost(month))
                except: 
                    print("ERROR")      
            elif option == 3:
                amount = int(input("Enter amount spent: "))
                category = int(input("Enter category: "))
                month = int(input("Enter month: "))
                txn = Transaction(amount, category, month)
                try:
                    self.budget.add_transactions(txn)
                except: 
                    print("ERROR ADDING TXN!!!!")
                else:
                    print("Transaction added")
            elif option == 5:
                break

            print("\n---------------\n")


    def print_menu(self):
        print("1. See Total Monthly Expense")
        print("2. See Costs by Category (Pct")
        print("3. Add Transaction")
        print("4. Set Monthly Income")
        print("5. Quit")