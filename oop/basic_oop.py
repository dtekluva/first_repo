# class Student:
    
#     skin_colour = "yellow"
#     iq = 150
#     hair_colour = "black"
#     age = 10
    

#     def write_exam(self):
#         import time
#         print("Writing exams .......")
#         time.sleep(3)
#         print("Done..!!!")

#     def get_year_of_birth(self):
#         import time
        
#         print("Thinking...!!")
#         time.sleep(3)

#         year_of_birth  = 2020 - self.age
#         print("Hello i was born in ", year_of_birth)

#     # def is_an_adult(self):

#     #     if self.age >= 18:
#     #         print("Yes i am an adult..")
#     #     elif self.age < 18:
#     #         print("Sorry i am not an adult..")

#     def is_an_adult(self):
        
#         if self.age >= 18:
#             time_since_adulthood = self.age - 18
#             year_of_adulthood = 2020 - time_since_adulthood
#             print("yes am and adult", "i beacme an adult in ", year_of_adulthood)

#         elif self.age < 18:
#             time_till_adulthood = 18 - self.age
#             year_of_adulthood = 2020 + time_till_adulthood
#             print("No i am not an adult, but i will be i the year", year_of_adulthood)


# ayo = Student()
# print(Student)
# print(ayo.skin_colour)
# print(ayo.iq)
# print(ayo.hair_colour)

# ayo.write_exam()
# ayo.get_year_of_birth()
# ayo.is_an_adult()

# seun = Student()
# print(Student)
# print(seun.skin_colour)
# print(seun.iq)
# print(seun.hair_colour)

# seun.write_exam()
# seun.get_year_of_birth()
# seun.is_an_adult()



# class Student:
    
#     school_uniform = True
#     school_fee = "Not Paid"

#     def __init__(self, skin_colour, iq, hair_colour, age, name):

#         self.name = name
#         self.skin_colour = skin_colour
#         self.iq = iq
#         self.hair_colour = hair_colour
#         self.age = age
    

#     def write_exam(self):
#         import time
#         print("Writing exams .......")
#         time.sleep(3)
#         print("Done..!!!")

#     def get_year_of_birth(self):
#         import time
        
#         print("Thinking...!!")
#         time.sleep(3)

#         year_of_birth  = 2020 - self.age
#         print("Hello i was born in ", year_of_birth)

#     # def is_an_adult(self):

#     #     if self.age >= 18:
#     #         print("Yes i am an adult..")
#     #     elif self.age < 18:
#     #         print("Sorry i am not an adult..")

#     def is_an_adult(self):
        
#         if self.age >= 18:
#             time_since_adulthood = self.age - 18
#             year_of_adulthood = 2020 - time_since_adulthood
#             print("yes am and adult", "i beacme an adult in ", year_of_adulthood)

#         elif self.age < 18:
#             time_till_adulthood = 18 - self.age
#             year_of_adulthood = 2020 + time_till_adulthood
#             print("No i am not an adult, but i will be i the year", year_of_adulthood)


# ayo = Student(name = "Ayo", hair_colour = "black", age = 23, skin_colour = "brown", iq = 140)
# # print(ayo.name)
# # print(ayo.skin_colour)
# # print(ayo.iq)
# # print(ayo.hair_colour)

# # ayo.write_exam()
# # ayo.get_year_of_birth()
# # ayo.is_an_adult()

# seun = Student(name = "Seun", hair_colour = "brown", age = 19, skin_colour = "fair", iq = 165)
# # print(seun.name)
# # print(seun.skin_colour)
# # print(seun.iq)
# # print(seun.hair_colour)

# # seun.write_exam()
# # seun.get_year_of_birth()
# # seun.is_an_adult()

# print(f"{'name'.center(15)} {'age'.center(3)} {'skin'.center(10)} {'hair'.center(10)} {'iq'.center(10)}")
# print()

# for student in [ayo, seun]:
#     print(f"{student.name.center(15)} {str(student.age).center(3)} {student.skin_colour.center(10)} {student.hair_colour.center(10)} {str(student.iq).center(10)}")


# class Bank():

#     # user_data_file = 

#     def create_new_account(self):

#         username = input("Please enter your username : ")        
#         password = input("Please enter your password : ")        
#         balance = 0

#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "a")

#         file.write(f"{username},{password},{balance}\n")    

        

# keystone = Bank()
# keystone.create_new_account()

# class Bank():

#     # user_data_file = 
#     logged_in_user = ""
#     balance = 0

#     def create_new_account(self):

#         username = input("Please enter your username : ")        
#         password = input("Please enter your password : ")        
#         balance = 0

#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "a")

#         file.write(f"{username},{password},{balance}\n")    

        
#     def login(self):
        
#         username = input("Please enter your username : ")        
#         password = input("Please enter your password : ")        

#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "r")

#         for user in file.readlines():
            
#             splitted_data = user.split(",")
#             saved_username = splitted_data[0]
#             saved_password = splitted_data[1]
#             saved_balance = splitted_data[2]
#             print()
            
#             if username == saved_username:
#                 print("Username is  correct checking passwd")

#                 if password == saved_password:
#                     print("Password is  correct Logged IN")
#                     break

#                 else:
#                     print("Sorry wrong password ")
#         else:
#             print("Sorry wrong username ")
        
#         self.logged_in_user = saved_username
#         self.balance = int(saved_balance)

#     def deposit(self, amount):
#         self.login()
        
#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "r")

#         for user in file.readlines():
            
#             splitted_data = user.split(",")
#             saved_username = splitted_data[0]
#             saved_password = splitted_data[1]

#             if self.logged_in_user == saved_username:

#                 self.balance += amount

#                 file.close()

#                 file_name = "oop/user_data_file.csv"
#                 file = open(file_name, "a")

#                 file.write(f"{self.logged_in_user},{saved_password},{self.balance}\n")    
            
#             else:
#                 file.close()
#                 file_name = "oop/user_data_file.csv"
#                 file = open(file_name, "a")
#                 file.write(user)
                
# keystone = Bank()
# keystone.create_new_account()


# class Bank():

#     # user_data_file = 
#     logged_in_user = ""
#     balance = 0

#     def create_new_account(self):

#         username = input("Please enter your username : ")        
#         password = input("Please enter your password : ")        
#         balance = 0

#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "a")

#         file.write(f"{username},{password},{balance}\n")    

        
#     def login(self):
        
#         username = input("Please enter your username : ")        
#         password = input("Please enter your password : ")        

#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "r")

#         for user in file.readlines():
            
#             splitted_data = user.split(",")
#             saved_username = splitted_data[0]
#             saved_password = splitted_data[1]
#             saved_balance = splitted_data[2]
#             print()
            
#             if username == saved_username:
#                 print("Username is  correct checking passwd")

#                 if password == saved_password:
#                     print("Password is  correct Logged IN")
#                     break

#                 else:
#                     print("Sorry wrong password ")
#         else:
#             print("Sorry wrong username ")
        
#         self.logged_in_user = saved_username
#         self.balance = int(saved_balance)

#     def deposit(self, amount):

#         self.login()
        
#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "r")
#         data = file.readlines()
#         file.close()

#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "w")

#         for user in data:
            
#             splitted_data = user.split(",")
#             saved_username = splitted_data[0]
#             saved_password = splitted_data[1]

#             if self.logged_in_user == saved_username:

#                 self.balance += amount

#                 file.write(f"{self.logged_in_user},{saved_password},{self.balance}\n")    
            
#             else:
#                 file.write(user)
    
#     def withdraw(self, amount):

#         self.login()
        
#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "r")
#         data = file.readlines()
#         file.close()

#         file_name = "oop/user_data_file.csv"
#         file = open(file_name, "w")

#         for user in data:
            
#             splitted_data = user.split(",")
#             saved_username = splitted_data[0]
#             saved_password = splitted_data[1]

#             if self.logged_in_user == saved_username:

#                 self.balance -= amount

#                 file.write(f"{self.logged_in_user},{saved_password},{self.balance}\n")
#                 print("Successfully Withdrawn..!!")    
            
#             else:
#                 file.write(user)
        
                
# keystone = Bank()
# keystone.withdraw(810000)

class Bank():

    # user_data_file = 
    logged_in_user = ""
    balance = 0

    def create_new_account(self):

        username = input("Please enter your username : ")        
        password = input("Please enter your password : ")        
        balance = 0

        file_name = "oop/user_data_file.csv"
        file = open(file_name, "a")

        file.write(f"{username},{password},{balance}\n")    

        
    def login(self):
        
        username = input("Please enter your username : ")        
        password = input("Please enter your password : ")        

        file_name = "oop/user_data_file.csv"
        file = open(file_name, "r")

        for user in file.readlines():
            
            splitted_data = user.split(",")
            saved_username = splitted_data[0]
            saved_password = splitted_data[1]
            saved_balance = splitted_data[2]
            print()
            
            if username == saved_username:
                print("Username is  correct checking passwd")

                if password == saved_password:
                    print("Password is  correct Logged IN")
                    break

                else:
                    print("Sorry wrong password ")
        else:
            print("Sorry wrong username ")
        
        self.logged_in_user = saved_username
        self.balance = int(saved_balance)

    def deposit(self, amount, beneficiary = False):

        if beneficiary == False:
            self.login()
        
        target_user = self.logged_in_user if not beneficiary else beneficiary
        
        file_name = "oop/user_data_file.csv"
        file = open(file_name, "r")
        data = file.readlines()
        file.close()

        file_name = "oop/user_data_file.csv"
        file = open(file_name, "w")

        for user in data:
            
            splitted_data = user.split(",")
            saved_username = splitted_data[0]
            saved_password = splitted_data[1]
            saved_balance = int(splitted_data[2])

            if target_user == saved_username:

                saved_balance += amount

                file.write(f"{target_user},{saved_password},{saved_balance}\n")    
            
            else:
                file.write(user)
    
    def withdraw(self, amount):

        self.login()
        
        file_name = "oop/user_data_file.csv"
        file = open(file_name, "r")
        data = file.readlines()
        file.close()

        file_name = "oop/user_data_file.csv"
        file = open(file_name, "w")

        for user in data:
            
            splitted_data = user.split(",")
            saved_username = splitted_data[0]
            saved_password = splitted_data[1]

            if self.logged_in_user == saved_username:

                self.balance -= amount

                file.write(f"{self.logged_in_user},{saved_password},{self.balance}\n")
                print("Successfully Withdrawn..!!")    
            
            else:
                file.write(user)


    def transfer(self, beneficiary, amount):

            self.withdraw(amount)
            self.deposit(amount, beneficiary)
        
                
keystone = Bank()
keystone.transfer('paul', 810000)