# math_score = input("Please enter math score : ")
# english_score = input("Please enter english score : ")

# math_score = int(math_score)
# english_score = int(english_score)

# print()
# print("Qualified for Engineering".ljust(26), ":", math_score >= 80 and english_score >= 70)
# print("Qualified for Business".ljust(26), ":", math_score >= 60 and english_score >= 70)
# print("Qualified for Theology".ljust(26), ":", math_score >= 20 and english_score >= 80)

# print(12, 6, 2020, sep = "-")
# print(12, 6, 2020, sep = "/")
# print(12, 6, 2020, sep = ".")

# my_file = open("printing.csv", "w")

# print(12, 6, 2020, sep = "-", file = my_file)
# print(12, 6, 2020, sep = "/")
# print(12, 6, 2020, sep = ".")

# def crazy_func():
#     """I AM JUST A CRAZY OL' FUNKY FUNCTION OOPSY I DO NOTHING HAHA"""
#     pass


# crazy_func

# print(-1)
# print(abs(-1))
# name = "cbDd"
# print(min(name))
# print(max(name))

my_range = range(23) # CASE OF A SINGLE VALUE INPUT GIVES FROM ZERO TO SPECIFIED VALUE

my_range_list = list(range(23)) # CASE OF A SINGLE VALUE INPUT GIVES FROM ZERO TO SPECIFIED VALUE CONVERTED TO LIST

my_range_list = list(range(10,23)) # CASE OF A START AND STOP VALUE INPUT GIVES FROM START TO SPECIFIED VALUE CONVERTED TO LIST

my_range_list = list(range(2,23,3)) # CASE OF A START AND STOP STEP VALUE INPUT GIVES FROM START TO SPECIFIED VALUE CONVERTED TO LIST


# print(my_range)
# print(my_range_list)

my_ages = [2,8,1,1,0,4,2,7,5,99,5]
# print(sorted(my_ages, reverse = True))

# multiplier = lambda age: age * 10
# multipied_ages = map( multiplier, my_ages)

# print(list(multipied_ages))

# template_text = "Hello i am a boy and my name is : <name_here>"
# print(template_text)

# name = input("Please Enter your name : ")
# DOB = input("Please Enter your DOB as yy/mm/dd : ")

# stripped_name = name.strip()
# formatted_text_with_input_name  = template_text.replace("<name_here>", stripped_name)

# print(name)
# print(stripped_name)
# print(stripped_name)
# print(formatted_text_with_input_name)

# splitted_text = name.split()
# print(splitted_text)
# print(DOB.split("/"))

# splitted_dob = DOB.split("/")
# year_of_birth = splitted_dob[2]
# print(year_of_birth)

# reformatted_DOB = [splitted_dob[1], splitted_dob[0]] #FORMAT TO MM-YY
# reformatted_DOB = "-".join(reformatted_DOB)
# print(reformatted_DOB)

# char_list = ['a', 'd', 'a', 'o', 'r', 'a']  
# print("".join(char_list))

# reg_user_file = open("registered_users.csv", "a")
# current_year = 2020

# name = input("Please enter name : ")
# DOB = input("Please enter DOB as dd/mm/yy: ")

# year_of_birth = DOB.split("/")[2]
# int_year_of_birth = int(year_of_birth)
# age = current_year - int_year_of_birth

# print("Hello name you are age years old now.".replace("name", name.upper()).replace("age", str(age)))

# is_millenial =int_year_of_birth > 1990 and int_year_of_birth < 2000
# is_gen_x = int_year_of_birth >= 2000
# is_baby_boomer = int_year_of_birth < 1990

# print(name.upper(), DOB, age, len(name), is_millenial, is_gen_x, is_baby_boomer, sep = ",", file = reg_user_file)

# print('foo' in ['foo', 'bar', 'baz'])

# if 'foo' in ['foo', 'bar', 'baz']:        #  x
#     print('Outer condition is true')      #  x

#     print(10 > 20)
#     if 10 > 20:                           #  x
#         print('Inner condition 1')        #        x

#     print('Between inner conditions')     #  x

#     print(10 < 20)

#     if 10 < 20:                           #  x
#         print('Inner condition 2')        #  x

#     print('End of outer condition')       #  x
# print('After outer condition')            #  x



# read_or_write = input("What would you like to do\nR for read W for write ") # R for read W for write 

# if read_or_write.lower() == "w":

#     name = input("Please enter your Username : ")
#     password = input("Please enter your password : ")

#     user_detail_file = open("data/{}_detail.csv".format(name), "w")
#     user_detail_file.write(f"{name},{password}")

#     database = open(f"data/{name}_database.txt", "a")
    
#     data = input("Please enter your note : ")
#     database.write(f"{data}\n")

# elif read_or_write.lower() == "r":

#     name = input("Please enter your Username : ")
#     password_input = input("Please enter your password : ")

#     user_detail_file = open("data/{}_detail.csv".format(name), "r")

#     username, password = user_detail_file.readline().split(",")

#     username_is_correct = username == name
#     password_is_correct = password == password_input

#     if username_is_correct and password_is_correct:
#         database = open(f"data/{name}_database.txt", "r")
#         data = database.read()
#         print(data)
    

# user_detail_file.close()


# word =15

# try:
#     print(1/0)
#     print(word + 10)
# except TypeError:
#     print("Please respect is reciprocal.!!")
#     print("Cannot add int to string.!!")
# except ZeroDivisionError:
#     print("Please respect is reciprocal.!!")
#     print("You sef you fit divide by zero.!!")

behaviour = "hard"

bolu_nickname = "Buttie" if behaviour == "soft" else "omo munshin "

print(bolu_nickname)