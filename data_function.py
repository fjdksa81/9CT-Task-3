import pandas as pd
dataset = pd.read_csv('friendship_groups.csv')
def year_averages():
  while (True):
    print("=== Choose Your Option ===")
    print("1. Year 9")
    print("2. Year 10")
    yeargroup_choice = input("Select an Option")
    if yeargroup_choice == "1":
         print("=== Choose Your Option ===")
         print("1. Display area averages (where people are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         print("3. Display friend group averages (where friend group members are from)")
         year9_choice = input("Select an Option")
         if year9_choice == "1":
             #matplotlib here
             pass
         elif year9_choice == "2":
             #matplotlib here
             pass
         elif year9_choice == "3":
             #matplotlib here
             pass
         else:
             print("Please input a valid character.")
         break
    elif yeargroup_choice == "2":
         print("=== Choose Your Option ===")
         print("1. Display area averages (where people are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         print("3. Display friend group averages (where friend group members are from)")
         year10_choice = input("Select an Option")
         if year10_choice == "1":
             #matplotlib here
             pass
         elif year10_choice == "2":
             #matplotlib here
             pass
         elif year10_choice == "3":
             #matplotlib here
             pass
         else:
             print("Please input a valid character.")
         break
    else: 
        print ("Please use the two options provided")

def area_averages():
  while (True):
    print ("=== Choose Your Option ===")
    print ("1. North Sydney")
    print ("2. South Sydney or more South")
    print ("3. Central Sydney")
    print ("4. Central Coast")
    print ("5. Hunter Valley")
    print ("6. Newcastle or further North")
    areachoice = input("Select an Option")
    if areachoice == "1":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         north_sydney_choice = input("Select an Option")
         if north_sydney_choice == "1":
             #matplotlib here
             pass
         elif north_sydney_choice == "2":
             #matplotlib here
             pass
         else:
             print("Please input a valid character.")
         break
    elif areachoice == "2":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         south_sydney_choice = input("Select an Option")
         if south_sydney_choice == "1":
             #matplotlib here
             pass
         elif south_sydney_choice == "2":
             #matplotlib here
             pass
         else:
             print("Please input a valid character.")
         break
    elif areachoice == "3":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         central_sydney_choice = input("Select an Option")
         if central_sydney_choice == "1":
             #matplotlib here
             pass
         elif central_sydney_choice == "2":
             #matplotlib here
             pass
         else:
             print("Please input a valid character.")
         break
    elif areachoice == "4":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         central_coast_choice = input("Select an Option")
         if central_coast_choice == "1":
             #matplotlib here
             pass
         elif central_coast_choice == "2":
             #matplotlib here
             pass
         else:
             print("Please input a valid character.")
         break
    elif areachoice == "5":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         hunter_valley_choice = input("Select an Option")
         if hunter_valley_choice == "1":
             #matplotlib here
             pass
         elif hunter_valley_choice == "2":
             #matplotlib here
             pass
         else:
             print("Please input a valid character.")
         break

    elif areachoice == "6":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         newcastle_choice = input("Select an Option")
         if newcastle_choice == "1":
             #matplotlib here
             pass
         elif newcastle_choice == "2":
             #matplotlib here
             pass
         else:
             print("Please input a valid character.")
         break


    else:
        print ("Please input a correct number")
        pass

def view_visualisations():
  while (True):
    print("=== Choose Your Option ===")
    print("1. Show entire school averages")
    print("2. Filter by year average")
    print("3. Show area averages")
    visualisation_choice = input("Select an Option")
    if visualisation_choice == "1":
        #pandas here
        break
    elif visualisation_choice == "2":
        year_averages()
        break
    elif visualisation_choice == "3":
        area_averages()
        break
    else:
        print("Please input a number")
        pass
         
def view_data():
    print(dataset)
    pass