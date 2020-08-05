# # def multiply(number):
# #     """THIS FUNCTION MULTIPLIES NUMBERS BY 3"""

# #     print("The answer is : ", number * 3)


# # multiply(2)

# # name = "Adedibu"

# # def print_name():

# #     global name

# #     name = "Bolu"
# #     print(name)


# # print_name()
# # print(name)

# import  requests

# url_to_get = "http://checklight.pythonanywhere.com/streets"
# # url_to_get = "http://jumia.com"
# response_data = ""

# def make_request(url):
#     global response_data

#     response = requests.get(url)
#     response_data = response

# def check_for_success():

#     if response_data.status_code == 200:
#         print("Request was successful")

# def json_or_content():

#     try:
#         response_data.json()
#         print("Data type is json")

#     except: 
#         response_data.content
#         print("Data type is HTML =-=-=> use content")

# make_request(url_to_get)
# check_for_success()
# json_or_content()


# ANAGRAM TESTER


# def test_anagram(word, test_word):

#     sorted_word = sorted(word.lower())
#     sorted_test_word = sorted(test_word.lower())
    
#     if sorted_test_word == sorted_word:
#         print(test_word , "is an anagram of", word)
#         return True
#     else:
#         print(test_word , "is not an anagram of", word)
#         return False



# def test_palindrome(word):

#     reversed_word = word[::-1]

#     if reversed_word.lower() == word.lower():
#         print(word, "is a palindrome")

#         return True

#     elif reversed_word.lower() != word.lower():
#         print(word, "is not a palindrome")

#         return False

# # test_anagram("web", "bew")
# # test_palindrome("blake")

# def run_string_tests(an_word, an_tword, pal_word ):

#     palindrome_result = test_palindrome(pal_word)
#     anagram_result = test_anagram(an_word, an_tword)

#     print(palindrome_result, anagram_result)


# run_string_tests("blank", "blink", "madam")

# def function_name():

#     print("This is Hello from another function.") 

# function_name()
# function_name()


# def add_name_to_surname(first_name):

#     full_name = first_name + " Inyang"
#     print(full_name)

# add_name_to_surname("Atha")
# add_name_to_surname("Bolu")
# add_name_to_surname("Sean")

# def multiply(value, multiplier):

#     answer = value * multiplier
#     print(answer)

# multiply(3, 2)
# multiply(6, 4)
# multiply(7, 0)

# def add_multiple_name_to_surname(*first_names):

#     # print(first_name)
#     # full_name = first_name + " Inyang"
#     # print(full_name)
    
#     for first_name in first_names:

#         full_name = first_name + " Inyang"
#         print(full_name)

# add_multiple_name_to_surname("Atha", "shade", "Jonah")


# def multiply_multiple_numbers(*numbers):
    
#     for number in numbers:

#         multiple = number * 2
#         print(multiple)

# multiply_multiple_numbers(2,3,5,2,4,65,67)

# POSITIONAL ARGUMENTS

# def dumb_function(name, age, gender):
#     print("name :", name, "Age :", age, "Gender :", gender)


# dumb_function( 20, "Male", "Paul")


# KEYWORD ARGUMENTS

# def dumb_function( age = 20, gender = "Male", name = "Paul"):
#     print("name :", name, "Age :", age, "Gender :", gender)


# dumb_function()

# def many_keyword_args(**people):
#     print(people)


# many_keyword_args(a=1, b=2, c=3,d=4)

# def my_function(*args, **kid):
#     print(kid)
#     # print("His last name is " + kid["lname"])

# # my_function(fname = "Tobias", lname = "Refsnes")
# my_function(**{"1":2, "2":3,"3":4})

# print("iusdgis", "blaze", file = "kdsjskk")


# def multiply(value, multiplier):

#     answer = value * multiplier
#     # print(answer)
#     return answer

# function_return_value = multiply(3, 2)
# print(function_return_value)

# def get_birth_year_from_age(age):

#     year_of_birth = 2020 - age

#     return year_of_birth

# def generate_username(name, age):

#     username = name + age

#     return username


# name = input("Please enter you name : ")
# age = input("Please enter you age : ")

# year_of_birth = get_birth_year_from_age(int(age))
# username = generate_username(name, age)

# file_name = "students.csv"
# file = open(file_name, "a")

# file.write(f"{name},{username},{age},{year_of_birth}\n")



def write_file(data):

    file_name = "functions/notes.csv"
    file = open(file_name, "a")
    file.write(data)

    return True

def read_file():

    file_name = "functions/notes.csv"
    file = open(file_name, "r")
    data = file.read()

    return data

def collect_data():

    name = input("Please enter your name : ")
    title = input("Please enter your note title : ")
    body = input("Please enter your Body : ")
    
    save_structure = f"{name};|{title};|{body}\n"

    return save_structure

def process_and_display_data(data):

    for line in data.split("\n"):
        splitted_line = line.split(";|")
        name = splitted_line[0]
        title = splitted_line[1]
        body = splitted_line[2]

        print("##########################")
        print("Name :",  name)
        print()
        print("Title :", title)
        print()
        print("Body :", body)
        print("##########################")
        print()

choice = input("Welcome. \n\nEnter (w) to write and \n(r) to read : ")

if choice == "w":

    data = collect_data()
    write_file(data)

elif choice == "r":

    saved_notes = read_file()
    process_and_display_data(saved_notes)
    # print(saved_notes)