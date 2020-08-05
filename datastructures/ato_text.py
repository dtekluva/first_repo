# sentence = input("Please enter your sentence \nWith dashes denoting blank points :\n ")
# replacements = input("Please enter your replacements in order\nseperated by commas :\n ")

# ## SPLIT SENTENCE INTO WORDS
# sentence_words = sentence.split(" ")

# print(sentence_words)

# ## GET CORRESPONDING REPLACEMENTS
# replacement_words = replacements.split(',')
# replacement_index = 0

# # search and replace dashes with replacement words
# for i in range(len(sentence_words)):

#     ## FIND DASHES IN WORDS OF GIVEN SENTENCE
#     if sentence_words[i].find("_") != -1:

#         ## REPLACE DASHES WITH CORRESPONDING REPLACEMENT WORDS.
#         sentence_words[i] = sentence_words[i].replace("_", replacement_words[replacement_index])
#         replacement_index+=1

# full_sentence = " ".join(sentence_words)
# print(full_sentence)

# prices = [200, 300, 400, 213, 32 ]
# marked = 1.5

# for i in range(len(prices)):
#     prices[i] = prices[i]*marked

# print(prices)

x = 20

# def do_somthing():
#     global x
#     x = 30
#     print(x)
#     return 23

# do_somthing()
# print(x)

# def numbers(one, two, three):
#     print("One : ",one, "Two : ", two, "Three : ", three)

# numbers(2,3,1)
# numbers(two = 2, three = 3, one = 1)

def greet(name, gender):

    if gender == "male":
        print(f"Hello Mr {name}..!")
    else:
        print(f"Hello Mrs {name}..!")

greet("Bolu", "female")

people = [("bolu", "male", 23), ("ade", "female", 15), ("sholu", "female", 45), ("manny", "male", 33)]

# for person in people:
#     greet(person[0], person[1])

for name, gender in people:
    greet(name, gender)