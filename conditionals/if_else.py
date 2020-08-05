# x = 10
# y = 5

# if x < y:
#     print("Yes")

# if x:
#     print("... Ths pulled true")
# import time

# password = "123qwert"
# username = "owambe21"

# input_username = input("Please enter username : ")
# input_password = input("Please enter password : ")


# if input_username == username:

#     print("Weldone your username exists ...")
#     print(".....checking password. Hold on.!")
#     print()

#     if input_password == password:

#         print(".....Congrats you are signed in.!")
    
#     elif input("Enter recovery mode ? (y/n): ") == "y":
#         user_wants_to_recover_password = input("Do you want to recover your password y/n : ")

#         if user_wants_to_recover_password == "y":
#             print("Your password is : ", password)
#         else:
#             print("Okay thanks for trying. Bye.!")

# elif input("Enter recovery mode ? (y/n): ") == "y":

#     user_wants_to_recover_user_name = input("Do you want to recover your username y/n : ")
#     print("Your username is : ", username)
    


# if 'a' in 'bor':
#     print('foo')
# elif 1/0:
#     print("This won't happen")
# elif var:
#     print("This won't either")

gender = "female"
offering = "food"


# salutation = 

# txt = "hello there" + " Mr/Mrs" +" adelabi, thank you for the gift/food you gave it was so nice/sweet. I enjoy/enjoyed eating/using it."
txt = f"hello there {'Mr' if gender == 'male' else 'Mrs'} adelabi, thank you for the {offering} you gave it was so {'nice' if offering == 'gift' else 'sweet'}. I {'enjoy' if offering == 'gift' else 'enjoyed'} {'using' if offering == 'gift' else 'eating'} it."

print(txt)

text = "Hello {Mr} {Adams}, we realized that you recently signed up for our weight loss program, we see that you a {130}kgs and {5}ft tall which gives you a BMI of {23} and by standards is {good}, hence we recommend the {sustainence} package for you today. buy now at {200}naira."

"""
BMI from 18.5 up to 25 kg/m2 may indicate optimal weight

BMI lower than 18.5 suggests the person is underweight

BMI 25 up to 30 may indicate the person is overweight,""" 