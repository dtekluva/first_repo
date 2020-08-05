# year_of_birth = int(input("Please enter year of birth : "))
# current_year = 2020

# # USING FOR LOOPS

# for i in range(year_of_birth, current_year+1):

#     if i%4 == 0:
#         print(i, "is a leap year")


# # USING WHILE LOOPS

# i = year_of_birth

# while  i != current_year:
    
#     i = i + 1

#     if i%4 == 0:
#         print(i, "is a leap year")



#CHECK WHICH IS FASTER FOR OR WHILE LOOPS
import datetime

year_of_birth = int(input("Please enter year of birth : "))
current_year = datetime.datetime.now().year
test_length = 1000000 # NUMBER OF TIMES TO RUN THE TEST FOR 

start_time = datetime.datetime.now()

for i in range(test_length):

    # USING FOR LOOPS

    for i in range(year_of_birth, current_year+1):

        if i%4 == 0:
            # print(i, "is a leap year")
            pass

end_time = datetime.datetime.now()

time_taken = end_time - start_time
print("For Took : ", time_taken)



start_time = datetime.datetime.now()

for _ in range(test_length):
    # USING WHILE LOOPS

    i = year_of_birth

    while  i != current_year:
        
        i = i + 1

        if i%4 == 0:
            # print(i, "is a leap year")
            pass

end_time = datetime.datetime.now()

time_taken = end_time - start_time
print("While Took : ", time_taken)