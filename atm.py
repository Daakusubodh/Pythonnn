class atm:
    def __init__(self):
        self.pin = ""
        self.amount = 0
        self.menu()
    def menu(self):
        user_input = input("""
            Hello, Press:
            1. To set the new pin
            2. To deposit
            3. To Withdraw
            4. To check balance
            5. To Exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            exit()
    def create_pin(self):
         self.pin = input("Enter your pin") 
         print("Pin set successfully")
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
             amount = int(input("Enter the amount")) 
             self.balance = self.balance + amount 
             print("Deposit successful")
        else:
            print("Invalid pin")
    def withdraw(self):
        temp = input("Enter your pin")

        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Operation successful")
            else:
                print("insufficient funds")
        else: 
            print("invalid amounts")
    def check_balance(self):
        temp = input("Enter your pin")
        if self.pin == temp:
            print(f"Your balance is {self.amount}")
        else:
            print("invalid")
    
        
sbi= atm()