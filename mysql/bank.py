import random
import pymysql_lib

class Bank():

    logged_user = ""
    balance = 0

    def get_new_acct_no(self):

        new_acct = random.choice(range(1,9999999999))
        max_chars = 8
        current_acct_chars = len(str(new_acct))

        deficiency = max_chars - current_acct_chars

        if  deficiency:
            new_acct = ("0"*deficiency) + str(new_acct)
        
        return new_acct

    def register(self):
        
        name = input("Please enter your name - ")
        age = int(input("Please enter your age - "))
        password = input("Please enter your password - ")

        pymysql_lib.add_user(name, age, password, self.get_new_acct_no())
        print("Successfully created account \n")

    def login(self):

        name_input = input("Please enter your name - ")
        password_input = input("Please enter your password - ")

        data = pymysql_lib.fetch_user_details(name_input)
        print(data)

        if data:

            print("Username was correct ..!!")
            if password_input == data[0]['password']:
                print("Loggin Successfull..!!")
                
                self.logged_user = name_input
                self.balance = data[0]['balance']

            else:
                print("Sorry your password was wrong")

        else :

            print("Username was wrong ..!!")

    def read_data(self):
        
        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            acct_no = splitted_line[2]
            balance = splitted_line[3]

            print("###########################")
            print("Name :", name)
            print("Acct :", acct_no)
            print("- - - - - - - - - - - - - - ")
            print("\nBalance :\n", balance)
            print("###########################\n")


    def read_user_data(self):
        
        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(":;")
            name = splitted_line[0]
            title = splitted_line[1]
            body = splitted_line[2]

            if name == self.logged_user:
                print("###########################")
                print("Name :", name)
                print("Title :", title)
                print("- - - - - - - - - - - - - - ")
                print("\nBody :\n", body)
                print("###########################\n")

    def get_balance(self):

        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            acct_no = splitted_line[2]
            balance = splitted_line[3]

            if name == self.logged_user:

                data = {"name":name, "acct_no":acct_no, "balance":balance}
                print(data)
                return data

    def deposit(self, amount, name = "self", comment = 'none', should_log = True):

        target_name = name if name != "self" else self.logged_user

        original_balance = pymysql_lib.get_balance(target_name)[0]['balance']
        bal = int(original_balance) + amount

        pymysql_lib.alter_balance(target_name,bal)

        if should_log:

            pymysql_lib.create_log(target_name, target_name, amount, comment, type = 'deposit')

        print("Deposit Successfull...!")
    
    
    def withdraw(self, amount, name = "self", comment = "none", should_log = True):

        target_name = name if name != "self" else self.logged_user

        original_balance = pymysql_lib.get_balance(target_name)[0]['balance']
        bal = int(original_balance) - amount

        pymysql_lib.alter_balance(target_name,bal)

        if should_log:
            pymysql_lib.create_log(target_name, target_name, amount, comment, type= 'withdrawal')

        print("withdrawal Successfull...!")

    
    def transfer(self, amount, target, comment):

        self.withdraw(amount, should_log = False)

        self.deposit(amount, target, should_log = False)

        pymysql_lib.create_log(self.logged_user, target, amount, comment, type= 'transfer')

    def get_transaction_logs_csv(self):

        logs = pymysql_lib.get_transaction_log()
        file = open("logs.csv", "w")
        file.write(f"sender,reciever,transaction_type,amount,comment\n")
        
        for transaction in logs:
            print(transaction)
            sender = transaction.get('sender')
            reciever = transaction.get('reciever')
            transaction_type = transaction.get('type')
            amount = transaction.get('amount')
            comment = transaction.get('comment')
            file.write(f"{sender},{reciever},{transaction_type},{amount},{comment}\n")
        


        

bank = Bank()
bank.get_transaction_logs_csv()
# bank.login()
# bank.deposit(450000, comment= 'My first hammer')
# bank.transfer(13000, target = 'adaeze', comment= 'Upkeep of my baby')