# letters = ["a", "b", "c", "d", "e", "f"]

# for i in letters:
#     print(i)

# print(list(range(6)))
# for i in range(6):
#     print(i, letters[i])


# for i in "banana":
#     print(i)
#     print("---")

# while True:
#     print("I am running..!")
#     print(".......!")

word = "proliferate"
index = 0

# while True:

#     print(word[index])
#     index += 1

#     if index == len(word):
#         break

# word = "emancipation"

# for letter in word:

#     if letter == "p":
#         print("Yaayy!!!. Found letter (p)\n")
#         break
#     else:
#         print("Searching for p", "found", letter)

# else:
#     print("Sorry P was not found in", word)

sentence = "In this example, <iterable> is the list a, and <var> is the variable i. Each time through the loop, i takes on a successive item in a, so print() displays the values 'foo', 'bar', and 'baz', respectively. A for loop like this is the Pythonic way to process the items in an iterable."

word_list = sentence.split(" ")
place_holder = "" 

# for word in word_list:

#     if len(word ) > len(place_holder):
#         place_holder = word

# print(place_holder)

# index = 0

# while True:

#     if len(word_list[index]) > len(place_holder):
#         place_holder = word_list[index]  
    
#     index +=1

#     if index == len(word_list):
#         break


# print(place_holder)

# number = 0
# stop_value = 200

# while True:

#     print(number)
#     number += 1

#     if number == stop_value:
#         break

# WITH A STEP VALUE 

# step_value = 2
# number = 0
# stop_value = 200

# while True:

#     print(number)
#     number += step_value

#     if number >= stop_value + 1:
#         break

# for i in range(1,200,1):
#     print(i)

# COUNT DOWNTIMER

import time
import winsound

# number_of_seconds = int(input("Enter time in seconds : "))

# for i in reversed(range(number_of_seconds)):
#     print(i)
#     time.sleep(1)

# winsound.Beep(500, 1000)


# number_of_mins = int(input("Enter time in mins : "))
# number_of_seconds = int(input("Enter time in seconds : "))

# total_secs = (number_of_mins * 60 ) + number_of_seconds

# for i in reversed(range(total_secs)):
#     mins = i//60
#     secs = i%60
#     print(f"{mins}:{secs}")
#     time.sleep(1)

# for i in range(3):

#     time.sleep(0.6)

#     for j in range(4):
#         time.sleep(0.3)
#         winsound.Beep(1000, 200)

# for i in range(100, 999):

#     sum_nums = i * 3
#     last_nums = str(i)[2] * 3

#     if sum_nums == int(last_nums):

#         print(i, sum_nums, last_nums)
#         break


# number_of_mins = int(input("Enter time in mins : "))
# number_of_seconds = int(input("Enter time in seconds : "))

# total_secs = (number_of_mins * 60 ) + number_of_seconds

# while True:
    
#     mins = total_secs//60
#     secs = total_secs%60
#     print(f"{mins}:{secs}")
#     time.sleep(1)
#     total_secs -= 1

#     if total_secs <= 0:
#         break

# numbers = [50, 10, 100, 99, 80, 80, 30]
# numbers_deviation = []
# numbers_deviation_squared = []

# n = len(numbers)
# mean = sum(numbers)/n

# for number in numbers:

#     numbers_deviation.append(number - mean)
#     print(number - mean)

# print(numbers_deviation)

# file_name = "loops/buhari.txt"
# file = open(file_name, "r", errors='ignore')

# data = file.read()

# lines = data.replace("-", " ").splitlines()
# buhari_place_holder = ""

# for line in lines:
    
#     words = line.split(" ")
#     for word in words:
#         if len(word) > len(place_holder):
#             place_holder = word


# file_name = "loops/obama.txt"
# file = open(file_name, "r", errors='ignore')

# data = file.read()

# lines = data.replace("-", " ").splitlines()
# obama_place_holder = ""

# for line in lines:
    
#     words = line.split(" ")
#     for word in words:
#         if len(word) > len(place_holder):
#             place_holder = word

# longestword_owner = "Buhari" if len(buhari_place_holder) > len(obama_place_holder) else "Obama"
# print(longestword_owner)

file_name = "loops/num_file.csv"
file = open(file_name, "w")

numbers = [50, 10, 100, 99, 80, 80, 30]

file.write(f"Scores, Passed\n")
for number in numbers:
    file.write(f"{number},{number >50}\n")


# numbers = [50, 10, 100, 99, 80, 80, 30]
# numbers_deviation = []
# numbers_deviation_squared = []

# n = len(numbers)
# mean = sum(numbers)/n

# for number in numbers:

#     numbers_deviation.append(number - mean)
#     print(number - mean)

# print(numbers_deviation)