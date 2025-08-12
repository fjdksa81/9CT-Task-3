


def user_interface():
    while True:
       print("=== Choose Your Option ===")
       print("1. View Data")
       print("2. View visualisations")
       print("3. Exit Program")
       ui_choice = input("Select and Option: ")

       if ui_choice  == "1":
           pamdas
       elif ui_choice == "2":
           print("=== Choose Your Option ===")
           print("1. Show entire school averages")
           print("2. Filter by year average")
           print("3. Show area averages")
           visualisation_choice = input("Select an Option")
           if visualisation_choice == "1":
               panamsa
           elif visualisation_choice == "2":
               print("=== Choose Your Option ===")
               print("1. Year 9")
               print("2. Year 10")
               yeargroup_choice = input("Select an Option")
               if yeargroup_choice == "1":
                   panmbas
               if yeargroup_choice == "2":
                   panmbas
           else:
               print ("=== Choose Your Option ===")
               print ("1. North Sydney")
               print ("2. South Sydney or more South")
               print ("3. Central Sydney")
               print ("4. Central Coast")
               print ("5. Hunter Valley")
               print ("6. Newcastle or further North")
               areachoice = input("Select an Option")
               if areachoice == "1":
                   pandas
               elif areachoice == "2":
                   pandas
               elif areachoice == "3":
                   pandas
               elif areachoice == "4":
                   pandas
               elif areachoice == "5":
                   pandas
               else:
                   pandas

    





                   
