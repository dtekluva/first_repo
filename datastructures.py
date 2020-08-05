### 3 WAYS OF CREATING LISTS

# list1 = []
# list2 = ["a", "b"]
# list3 = list()

# print(list1, list2, list3, sep = "\n")

# import datetime

# then = datetime.datetime.now()
# number_of_runs = 10000000

# for i in range(number_of_runs):

#     list1 = []

# now = datetime.datetime.now()

# time_taken = now- then
# print(time_taken.microseconds/1000)

# then = datetime.datetime.now()
# number_of_runs = 10000

# for i in range(number_of_runs):

#     list1 = list()

# now = datetime.datetime.now()

# time_taken = now- then
# print(time_taken.microseconds/1000)


# list1 = ['physics', 'chemistry', 1997, 2000, "Tetiary"]


# print(list1[1:3])

# list1[2:4] = ["Boli", "Epa"]

# print(list1)



# scores_list = []

# for i in range(10000):
#     score = input("Please enter score : ")
#     scores_list.append(score)

#     print(scores_list)

# DICE ROLLING GAME 

# import random 

# player1_score = 0
# player2_score = 0

# import random 

# players = [["Haleemah", 0], ["Atha", 0], ["Tobi", 0], ["Kayode", 0], ["Lawal", 0]]

# for index, player in enumerate(players):

#     name = player[0]
#     score = player[1]

#     input(f"Hello {name} please press enter to roll : ")

#     rolled_number = random.randint(1,6)

#     players[index][1] += rolled_number 
#     score += rolled_number 
    
#     print(name, "\nScore", score, end = "\n\n")

# print(players)

# import random 

# players = [["unnammed", 0], ["unnammed", 0], ["unnammed", 0], ["unnammed", 0], ["unnammed", 0]]

# for index in range(len(players)):
#     players[index][0] = input(f"Please enter name for player {index} : ")

# for index, player in enumerate(players):

#     name = player[0]
#     score = player[1]

#     input(f"Hello {name} please press enter to roll : ")

#     rolled_number = random.randint(1,6)

#     players[index][1] += rolled_number 
#     score += rolled_number 
    
#     print(name, "\nScore", score, end = "\n\n")
    
# print(players)

# names = ["lola", "seun", "jega", "sola", "wunmi", "kane", "yomi", "lola", "lola"]

# print(names)

# for i in range(10):
#     names.append("Shina")

# for i in range(5):
#     names.append("Bolu")


# print("After appending")

# print(names)

# print("After remove : ")

# names.remove("lola")
# print(names)

# names[2:5] = []
# print(names)

# print(names.count("lola"))

# file_name = "names.txt"
# file = open(file_name, "r")

# all_names = []

# for fullname in file.readlines():
#     name, lastname = fullname.replace("\n", "").split(" ")[:2]
#     all_names.append(name)
#     all_names.append(lastname)
# print(all_names)

# name_to_search = input("Please enter name to search for : ")

# print(all_names.count(name_to_search))
# names.clear()
# print("After cleared: ")
# print(names)
# new_photocopy = names.copy()
# print("after copy")
# print(new_photocopy)
# new_photocopy.append("sghalewa")

# print()
# print(new_photocopy)
# print(names)

# names.extend(["boy", "dog"])
# print("new list :",names)

# names.insert(4, "teju")
# print(names)
# position= names.index("seun")
# print(position)

# import datetime

# test_length = 150000000 # NUMBER OF TIMES TO RUN THE TEST FOR 

# start_time = datetime.datetime.now()


# for i in range(test_length):

#     list1 = [] 

# end_time = datetime.datetime.now()

# time_taken = end_time - start_time
# print("Braces Took : ", time_taken)


# test_length = 1000000 # NUMBER OF TIMES TO RUN THE TEST FOR 

# start_time = datetime.datetime.now()

# for i in range(test_length):

#     list1 = list()

# end_time = datetime.datetime.now()

# time_taken = end_time - start_time
# print("List() Took : ", time_taken)


list1 = ['physics', 'chemistry', 1997, 2000, "board", "tv"] 

# print(list1)

# list1.append("Foluke")

# print(list1)

# for _ in range(20):
#     list1.append("Foluke")

# print(list1)

# for i in list(range(0,20)):# "all characters":
#     print(i)

# for alphabet in "all characters":
#     print(alphabet)


# for each_letter in "foluke":
#     print(each_letter)

# scores = [1,45,12,32,4,23,54,23,56]

# for each_value in scores:
#     print(each_value)

# print(list1[1:4])
# print(list1[1], list1[2], list1[3])
# print(list1)

# list1.remove("chemistry")
# print(list1)
# print(list1.count(1997))
# print(len("chemistry"))
# list1.clear()
# print(list1)

# newcomers = ["Jide", "Shola"]
# list1.extend(newcomers)

# print(list1)

# list1.append(newcomers)
# print(list1)

# list1.insert(2,"Edafe")
# print(list1)

# popped_value = list1.pop(3)
# print(list1)
# print("Successfully removed : ", popped_value)

# index_of_value = list1.index(1997)
# print(index_of_value)

scores = [1,45,12,32,56]
hobby = ["swim", "dance", "pray", "read", "swim"]
students = ["Ali", "Salami", "Rhaman", "George", "Qudus"]
raw_zipped_values = zip(students, hobby, scores)

print(raw_zipped_values)
print(list(raw_zipped_values))