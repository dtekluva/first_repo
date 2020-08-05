# quantity = 5

# x = 0
# y = 1
# print(x)
# print(y)

# for i in range(quantity):
#     print(x + y)
#     x, y = y, x+y

students_scores= [
    ["atha", [
        ["m",30],
        ["e",30]],
        [["reading","20%"], ["playing","80%"]]
        ], 
    ["Flipzig", [
        ["m",60],
        ["e",47]],
        [["Sleep","40%"], ["Eat","60%"]]
        ], 
    ["bolu", [
        ["m",30],
        ["e",30]],
        [["singing","40%"], ["jumping","60%"]]
        ], 
    ["seun", [
        ["m",30],
        ["e",30]],
        [["dancing","45%"], ["traveling","45%"]]
    ]
    ]

# target_student = students_scores[2]

# name = target_student[0]
# print("Name : ", name)

# math_score = target_student[1][0][1]
# print("Math Score : ", math_score)

# english_score = target_student[1][1][1]
# print("English Score : ", english_score)

# hobbies = target_student[2]

# hobby1_is_greater = int(hobbies[0][1][:-1]) > int(hobbies[1][1][:-1]) 
# favourite_hobby = hobbies[0][0] if hobby1_is_greater == True else hobbies[1][0]
# print("Favourite Hobby is : ", favourite_hobby)

# for target_student in students_scores:

#     name = target_student[0]
#     print("Name : ", name)

#     math_score = target_student[1][0][1]
#     print("Math Score : ", math_score)

#     english_score = target_student[1][1][1]
#     print("English Score : ", english_score)

#     hobbies = target_student[2]

#     hobby1_is_greater = int(hobbies[0][1][:-1]) > int(hobbies[1][1][:-1]) 
#     favourite_hobby = hobbies[0][0] if hobby1_is_greater == True else hobbies[1][0]
#     print("Favourite Hobby is : ", favourite_hobby)

#     print()
#     print("-------------------------")
#     print("-------------------------")
#     print()

# names = ["john", "paul", "sean"] 

# index = 0

# while True:
#     # print(index, names[index])

#     names[index] = "Mr " +  names[index]

#     index += 1

#     if index == len(names):
#         break

# print(names)


# names = ["john", "paul", "sean"] 

# for index in range(len(names)):

#     names[index] = "Mr " +  names[index]

# print(names)

# list_of_values_entered = []
# while True:

#     value = input("Please enter a value \n: ")
#     list_of_values_entered.append(value) 

#     for value in list_of_values_entered:
#         print(value.center(10), str(len(value)).center(10))


# list_of_values_entered = []

# while True:

#     value = input("Please enter a value : ")

#     list_of_values_entered.append(value)
#     print("Yu now have", len(list_of_values_entered), "values in your list")

#     stop_or_continue = input("Press y to continue entering values or n to stop : ")

#     if stop_or_continue == "n":
#         break

# total_characters = 0

# print("Value".center(10), "Length".center(10), "Qty_A".center(10), "Qty_B".center(10), "Qty_C".center(10))

# for value in list_of_values_entered:

#     lenght_of_value = len(value)
#     total_characters += lenght_of_value
#     print(value.center(10), str(lenght_of_value).center(10),str(value.count("a")).center(10), str(value.count("b")).center(10), str(value.count("c")).center(10))

# print(f"\nValues in list : {len(list_of_values_entered)}. Total characters : {total_characters}.")

# word_list = []
# index = 0

# for char in "alphabet":
#     index += 1
#     word_list.append((index, char, char.upper()))
    
# print(word_list)


# ## EXTEND 

nums = [1,2,3,5,6,7, 7,7,7,7]

# nums.insert(3,4)
# print(nums)\

## REMOVE

# nums.remove(7)
# print(nums)

number_of_sevens = nums.count(7)

for _ in range(number_of_sevens):
    nums.remove(7)

print(nums)