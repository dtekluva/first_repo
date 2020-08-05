# name = input("Please enter your name : ")
# headache = input("Please Do you have Headache : ")
# user_file = open(f"{name}.csv", "a")

# if headache == "t":
    
#     vomitting = input("Please have you been vomitting : ")

#     if vomitting == "t":

#         stooling = input("Please have you been stooling : ")

#         if stooling == "t":

#             print("You might have food poisoning..!!")
#             print(name, "food poisoning", sep = ",", file = user_file)

#         else:

#             fever = input("Please have you been feverish : ")

#             if fever == "t":

#                 print("You might have thyphoid..!!")
#                 print(name, "thyphoid", sep = ",", file = user_file)

#             else:

#                 print("Your solution no de market..")
#                 print(name, "village people", sep = ",", file = user_file)

#     else:

#         fever = input("Please have you been fever : ")

#         if fever == "t":

#             print("You might have malaria..!!")
#             print(name, "malaria", sep = ",", file = user_file)

#         else:

#             print("No diagnosis.")
#             print(name, "no diagnoses", sep = ",", file = user_file)

# else:
#     print("No diagnosis.")
#     print(name, "No diagnosis", sep = ",", file = user_file)

# response = input("Please what would you like to do (game or calc): ")

# if response == "calc":
#     n1, d1 = input("Please enter frac1 as (x/y) : ").split("/")
#     n2, d2 = input("Please enter frac2 as (x/y) : ").split("/")

#     n1, d1 = [int(n1), int(d1)]
#     n2, d2 = [int(n2), int(d2)]

#     n_total = (n1 * d2) + (d1 * n2)
#     d_total = d1 * d2


#     top = n1 * n2
#     bottom = d1 * d2


#     print(n_total, "/", d_total)
#     print(top, "/", bottom)

# elif response == "game":

#     import random

#     select_num = random.randint(1, 10)
#     print(select_num)

#     guessed_value = int(input("Please enter your guess : "))

#     if guessed_value == select_num:

#         print("Wow you got it.!")

#     elif guessed_value != select_num:

#         print("sorry try again.!")

# file = open("numbers.csv", "w")

# for i in range(10):
#     print("Hello", i, sep = ",", file = file)

# file = open("numbers.csv", "w")
# number_of_decades = 1

# for i in range(1,51):

#     print(i, i*2, sep = ",", file = file)

#     if i % 10 == 0:

#         print("Decade", number_of_decades, sep = ",", file = file)
#         number_of_decades += 1

# text2 = "ABCDE"
# text1 = "LMNOP"

# for i in text1:
    
#     for j in text2:
#         print(i, j)

# import winsound
# import time

# value = 10


# for i in reversed(range(value)):

    
#     time.sleep(1)
#     print(i)
#     for i in range(5):
#         winsound.Beep(1000, 200)
# winsound.Beep(1000, 4000)

# file = open("names.txt", "r")
# data = file.read().split(" - ")
# file.close()

# file = open("names.txt", "w")

# for line in data:
#     file.write(line)
#     file.write("\n")

# file = open("names.txt", "r")
# data = file.readlines()

# for line in data:
#     print(line)

# number = 500

# for i in range(1, number):
#     print(i)
#     if number%i == 7:
#         break

#     if i == 13:
#         print()
#         continue

#     print("Sorry no match yet")


# file = open("names.txt", "r")
# data = file.readlines()

# name_to_search = input("Please enter name to search : ")

# for line in data:

#     if name_to_search.lower() in line.lower():
#         print(line)


# DICE ROLLING GAME 

# import random 

# player1_score = 0
# player2_score = 0


# while True:
    
#     input("Please press enter to roll.!!")
#     die1 = random.randint(1, 6)
#     die2 = random.randint(1, 6)

#     player1_score += die1
#     player2_score += die2

#     print("Player 1 :", player1_score, die1)
#     print("Player 2 :", player2_score, die2)

#     if player1_score > 20 or player2_score > 20:
#         wining_player = "Player 1" if player1_score > 20 else "Player 2"
#         print(f"weldone {wining_player} won. !!")
#         break


# import datetime

# then = datetime.datetime.now()
# number_of_runs = 10000

# for i in range(10):

#     while number_of_runs>0:
#         (500 ** i)/2
#         number_of_runs -= 1

#     now = datetime.datetime.now()

#     time_taken = now- then
#     print(500 ** i, time_taken.microseconds/1000)

# file = open("application_data.csv", "r")
# write_file = open("application_data_copy.csv", "w")



# for line_number, line in enumerate(file.readlines()):

#     if line_number == 0:
#         line_to_write = line.replace("\n", "") + "," + "payback" + "," + "interestValue" + "\n"
#         write_file.write(line_to_write)
#         continue

#     values = line.split(",")
#     amount, interest = float(values[4]), float(values[5])

#     payback = amount +(amount * (interest /100))
#     interest_value = amount * (interest /100)

#     # print(amount, interest, payback)

#     line_to_write = line.replace("\n", "") + "," + str(payback) + "," + str(interest_value) +"\n"

#     write_file.write(line_to_write)


# for i in range(100, 999):
#     sum_nums = i + i + i
    
#     last_char_of_num = str(i)[2]*3

#     sum_nums_as_str = str(sum_nums)

#     print(i, sum_nums, last_char_of_num, sum_nums_as_str == last_char_of_num)

#     if sum_nums_as_str == last_char_of_num: break;

#DISPLAY BASIC
# for i in range(1,12):
#     for j in range(1,5):
#         print(i*j, end = "\t")
#     print()

#DISPLAY MORE DESCRIPTIVE

# for i in range(1,5):
#     for j in range(1,5):
#         print(f"{i}x{j} = {i*j}".ljust(10), end = "")
#     print()

# PRINT TO FILE

# file = open("multiplicationtable.csv", "w")

# for i in range(1,5):
#     text = ""
#     for j in range(1,5):
#         print(f"{i}x{j} = {i*j}".ljust(10), end = "")
#         text += f"{i}x{j} = {i*j},".ljust(10)

#     print(text, file = file, end = "\n")
#     print()


# PRINT EVEN AND ODD NUMBERS FOR DECADES
total_even = 0
total_odds = 0
highest_even_ratio = 0

for i in range(1,101):

    if i%2 == 0:
        total_even += i
        # print("Even", i)
    else:
        total_odds += i
        # print("Odd", i)

    if i%10 == 0:
        ratio = total_even/total_odds

        if ratio > highest_even_ratio:
            highest_even_ratio = ratio

        print("Decade - ", i, total_even, total_odds, ratio)
        total_even = 0
        total_odds = 0
        
print(highest_even_ratio)

