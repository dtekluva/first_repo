# fever_status = input("Hello have you been having fever ? : ")

# if fever_status == "yes":

#     print("Has fever")

#     sneezing_status = input("Have you been sneezing ? : ")

#     if sneezing_status == "yes":

#         print("Has cold")

#         coughing_status = input("Have you been coughing ? : ")

#         if coughing_status == "yes":

#             print("Call NCDC")
#         else:
#             print("Okay Byee.")
    
#     else:
        
#         stooling_status = input("Have you been stooling ? : ")

#         if stooling_status == "yes":

#             print("Please drink some garri..!!")
#         else:

#             print("You might need to appease your village people..!!")

# else:

#     print("Has no fever")

# should_continue = bool(int(input("Shoud i continue : ")))

# while should_continue:
#     print("Hello")
#     should_continue = bool(int(input("Shoud i continue : ")))

# number_of_runs = 5
# n = number_of_runs
# should_continue = bool(int(input("Shoud i continue : ")))

# while should_continue:
#     n -= 1
#     print("Hello ..!")

#     if n == 0:
#         n = number_of_runs
#         should_continue = bool(int(input("Shoud i continue : ")))

# numbers_file_name = "numbers.csv"
# numbers_file = open(numbers_file_name, "w")

# qty_to_write = 1000 
# number_written = 1

# print("Numbers", "Multiples", sep = ",", file = numbers_file)

# while number_written != qty_to_write:
#     print(number_written, number_written * 10, sep = ",", file = numbers_file)
#     number_written = number_written + 1

numbers_file_name = "data/numbers.csv"
numbers_file = open(numbers_file_name, "w")

# print("1Times", "2Times","3Times", "4Times", sep = ",", file = numbers_file)


# qty_to_write = 500 
# number_written = 1

# while  number_written != qty_to_write:#

#     print("1", "x", number_written, "=", number_written, "", 
#             "2", "x", number_written, "=", number_written * 2, " ",
#             "3", "x", number_written, "=", number_written * 3, " ",
#             "4", "x", number_written, "=",number_written * 4, 
#             sep = ",", file = numbers_file)
#     number_written += 1



#WRITE EVEN NUMBER FROM 0 - 50 INTO A FILE7


# qty_to_write = 50 
# number_written = 1

# while  number_written != qty_to_write:

#     if number_written % 2 == 0:

#         print(number_written, "is an even num")
    
#     elif number_written % 2 != 0:

#         print(number_written, "is not an even num")
    
#     number_written += 1
