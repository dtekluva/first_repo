# numbers = [4,5,3,6,5]

# mean_nums = sum(numbers)/len(numbers) # ALSO OUR X_BAR
# print("MEAN : ", mean_nums)

# for number in numbers:
    
#     print(number, round(number - mean_nums, 1), (number - mean_nums)**2)



###############################
# A MORE DESCRIPTIVE APPROACH #
###############################

numbers = [4,5,3,6,5,]

x_bar = sum(numbers)/len(numbers) # ALSO OUR X_BAR
print("MEAN : ", x_bar, "\n")
variance = 0

print(str("x").ljust(4), "|", str("x_xbar").ljust(6), "|", str("x_xbar_squared").ljust(8), "|")
print(str("-"*4).ljust(4), "+", str("-"*6).ljust(6), "+", str("-"*14).ljust(8), "-")
for number in numbers:

    x_xbar = round(number - x_bar, 2)
    x_xbar_squared = round(x_xbar**2, 2)

    variance += x_xbar_squared

    print(str(number).ljust(4), "|", str(x_xbar).ljust(6), "|", str(x_xbar_squared).ljust(14), "|")


print("\nVariance : ",variance)