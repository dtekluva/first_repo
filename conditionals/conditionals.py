# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0		
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


feeling_good = input("Have you been feeling good? : ")

if feeling_good == "yes":
    print("Bye !!")

elif feeling_good == "no":

    having_headache = input("Have you been having a headache ? : ")

    if having_headache == "no":
        print("Drink water !!")
        
    elif having_headache == "yes":
        stressed_lately = input("Have you been stressed lately? : ")

        if stressed_lately == "yes":
            print("Have some rest !!")
            
        elif stressed_lately == "no":
            fever = input("Have you been feverish? : ")
            if fever == "yes":
                print(" Call NCDC!!")
                
            elif fever == "no":
                print("Sorry can't help you now.!")