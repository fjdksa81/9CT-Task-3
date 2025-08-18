import pandas as pd
dataset = pd.read_csv('friendship_groups.csv')
def year_averages():
  while (True):
    print("=== Choose Your Option ===")
    print("1. Year 9")
    print("2. Year 10")
    yeargroup_choice = input("Select an Option")
    if yeargroup_choice == "1":
         #with only year 9
         break
    elif yeargroup_choice == "2":
         #only year 10
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
        #north sydney data pandas
        break
    elif areachoice == "2":
        #south sydney data
        break
    elif areachoice == "3":
        #central sydney data
        break
    elif areachoice == "4":
        #central coast data
        break
    elif areachoice == "5":
        #hunter valley data
        break
    elif areachoice == "6":
        #newcastle data
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