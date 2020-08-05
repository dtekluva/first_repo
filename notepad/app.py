import datetime

logged_in_user = False

while True:

    task = input("\nWelcome to the wackiest notepad ever \nPlease enter : \n# su for signup\n# si for signin\n# wr to add journal\n# r to read journal\n# del to delete jornal\n# stats to get stats\n\n> : ")


    if task == "su":
        ############# Sign UP ##############

        firstname = input("Please enter your name : ")
        surname = input("Please enter your surname : ")
        username = input("Please enter your username : ")

        password = input("Please enter your password : ")
        confirm_password = input("Please re-enter your password : ")

        while password != confirm_password:

            print("Sorry you passwords dont match !!\n")
            password = input("Please enter your password : ")
            confirm_password = input("Please re-enter your password : ")


        file = open("notepad/db.csv", "a")

        file.write(f"{firstname},{surname},{username},{password}\n")
        file.close()

    elif task == "si":
        ############ Sign in ###############

        input_username = input("Please enter your username : ")
        input_password = input("Please enter your password : ")

        file = open("notepad/db.csv", "r")

        for line in file.readlines():
            saved_username, saved_password = line.replace("\n","").split(",")[2:]
            
            if saved_username.lower() == input_username.lower():
                if input_password == saved_password:
                    print(f"Welcome {saved_username}")
                    logged_in_user = saved_username ## ASSIGN THE USERNAME AS LOGGED IN USER GLOBALLY
                    break
        else:
            print("Sorry you may not have an account, Please sign up.")

    elif task == "wr":

        if logged_in_user:
            ############# write journal ##############

            title = input("Please enter a Title : ")
            body = input("Please enter your mind : ")
            today = datetime.datetime.now()
            date = f"{today.day}-{today.month}-{today.year}"

            file = open("notepad/journals.csv", "a")

            file.write(f"{logged_in_user},{title},{body},{date}\n")
            file.close()
        else:

            print("Sorry you need to be logged in first.!!")


    elif task == "r":

        if logged_in_user:

            ############# read jornal ##############
            journals_found = []

            file = open("notepad/journals.csv", "r")

            for line in file.readlines():
                username, title, body, date = line.split(",")
                
                if logged_in_user == username:

                    journals_found.append({
                                            "title":title,
                                            "body":body
                                        })
            print()
            for index, journal in enumerate(journals_found):
                print(index+1, journal["title"])
            print()
            selected_option = int(input("Above are your notes pick one \n> "))

            print("\n###########################")
            print(journals_found[selected_option-1]["title"].upper())
            print("###########################\n")
            print(journals_found[selected_option-1]["body"])
            print("\n###########################")
            print("###########################\n")

        else:

            print("Sorry you need to be logged in first.!!")


    elif task == "del":

        if logged_in_user:
            ############# delete jornal ##############
            journals_found = []

            file = open("notepad/journals.csv", "r")

            for line in file.readlines():
                username, title, body, date = line.split(",")
                
                if logged_in_user == username:

                    journals_found.append({
                                            "title":title,
                                            "body":body
                                        })
            file.close()


            print()



            for index, journal in enumerate(journals_found):
                print(index+1, journal["title"])
            print()
            selected_option = int(input("Select a jornal to delete \n> "))

            new_db = []
            file = open("notepad/journals.csv", "r")

            for line in file.readlines():
                username, title, body, date = line.split(",")

                if logged_in_user == username and title == journals_found[selected_option-1]["title"]:
                    continue
                new_db.append(line)

            file.close()

            file = open("notepad/journals.csv", "w")

            for journal in new_db:
                file.write(journal)
            file.close()
        
        else:

            print("Sorry you need to be logged in first.!!")


    elif task == "stats":

        if logged_in_user:
            ########### overview #########
            journals_found = []

            file = open("notepad/journals.csv", "r")

            for line in file.readlines():
                username, title, body, date = line.split(",")
                
                if logged_in_user == username:

                    journals_found.append({
                                            "title":title,
                                            "body":body
                                        })

            print("Total notes : ", len(journals_found))

        else:

            print("Sorry you need to be logged in first.!!")