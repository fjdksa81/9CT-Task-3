import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('friendship_groups.csv')
friendship_group_labels = ('North of the School', 'South of the School', 'Central Coast / Around the School')
day_1_labels = ("Knew people going in", "Knew nobody going in")
respondant_location_labels = ("North Sydney", "South Sydney or more South", "Central Sydney", "Central Coast", "Hunter Valley")
def year_averages():
  while (True):
    print("=== Choose Your Option ===")
    print("1. Year 9")
    print("2. Year 10")
    yeargroup_choice = input("Select an Option: ")
    if yeargroup_choice == "1":
         print("=== Choose Your Option ===")
         print("1. Display area averages (where people are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         print("3. Display friend group averages (where friend group members are from)")
         year9_choice = input("Select an Option: ")
         if year9_choice == "1":
             year9_school_area = (9, 3, 0, 16, 1)
             plt.pie(year9_school_area, labels=respondant_location_labels, autopct='%.1f%%', startangle=90)
             plt.title("Where do respondants live?")
             plt.show()
             break
         elif year9_choice == "2":
             year9_day_1 = (22, 11)
             plt.pie(year9_day_1, labels=day_1_labels, autopct='%.1f%%', startangle=90)
             plt.title("Did respondants know people day 1 year 7?")
             plt.show()
             break
         elif year9_choice == "3":
             year9_friendship_averages = (5.06, 2.57, 4.09)
             plt.pie(year9_friendship_averages, labels=friendship_group_labels, autopct='%.1f%%', startangle=90)
             plt.title("What is the average makeup of a respondant's friendgroup")
             plt.show()
             break
         else:
             print("Please input a valid character.")
             pass
         break
    elif yeargroup_choice == "2":
         print("=== Choose Your Option ===")
         print("1. Display area averages (where people are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         print("3. Display friend group averages (where friend group members are from)")
         year10_choice = input("Select an Option: ")
         if year10_choice == "1":
             year10_school_area = (13, 1, 2, 14, 2)
             plt.pie(year10_school_area, labels=respondant_location_labels, autopct='%.1f%%', startangle=90)
             plt.title("Where do respondants live?")
             plt.show()
             break
         elif year10_choice == "2":
             fig, ax = plt.subplots()
             year10_day_1 = (23, 7)
             plt.pie(year10_day_1, labels=day_1_labels, autopct='%.1f%%', startangle=90)
             plt.title("Did respondants know people day 1 year 7?")
             plt.show()
             break
         elif year10_choice == "3":
             year10_friendship_averages = (4.76, 2.36, 4.3)
             plt.pie(year10_friendship_averages, labels=friendship_group_labels, autopct='%.1f%%', startangle=90)
             plt.title("What is the average makeup of a respondant's friendgroup")
             plt.show()
             break
         else:
             print("Please input a valid character.")
             pass
         break
    else: 
        print ("Please use the two options provided")
        pass
def area_averages():
  while (True):
    print ("=== Choose Your Option ===")
    print ("1. North Sydney")
    print ("2. South Sydney or more South")
    print ("3. Central Sydney")
    print ("4. Central Coast")
    print ("5. Hunter Valley")
    areachoice = input("Select an Option: ")
    if areachoice == "1":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         north_sydney_choice = input("Select an Option: ")
         if north_sydney_choice == "1":
             north_sydney_friendship_averages = (5.22, 2.99, 3.77)
             plt.pie(north_sydney_friendship_averages, labels=friendship_group_labels, autopct='%.1f%%', startangle=90)
             plt.title("What is the average makeup of a respondant's friendgroup")
             plt.show()
             break
         elif north_sydney_choice == "2":
             north_sydney_day_1 = (19, 3)
             plt.pie(north_sydney_day_1, labels=day_1_labels, autopct='%.1f%%', startangle=90)
             plt.title("Did respondants know people day 1 year 7?")
             plt.show()
             break
         else:
             print("Please input a valid character.")
         break
    elif areachoice == "2":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         south_sydney_choice = input("Select an Option: ")
         if south_sydney_choice == "1":
             south_sydney_friendship_averages = (4.75, 3.25, 3.75)
             plt.pie(south_sydney_friendship_averages, labels=friendship_group_labels, autopct='%.1f%%', startangle=90)
             plt.title("What is the average makeup of a respondant's friendgroup")
             plt.show()
             break
         elif south_sydney_choice == "2":
             south_sydney_day_1 = (2, 2)
             plt.pie(south_sydney_day_1, labels=day_1_labels, autopct='%.1f%%', startangle=90)
             plt.title("Did respondants know people day 1 year 7?")
             plt.show()
             break
         else:
             print("Please input a valid character.")
         break
    elif areachoice == "3":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         central_sydney_choice = input("Select an Option: ")
         if central_sydney_choice == "1":
             central_sydney_friendship_averages = (2, 6, 3.5)
             plt.pie(central_sydney_friendship_averages, labels=friendship_group_labels, autopct='%.1f%%', startangle=90)
             plt.title("What is the average makeup of a respondant's friendgroup")
             plt.show()
             break
         elif central_sydney_choice == "2":
             central_sydney_day_1 = (2, 0)
             plt.pie(central_sydney_day_1, labels=day_1_labels, autopct='%.1f%%', startangle=90)
             plt.title("Did respondants know people day 1 year 7?")
             plt.show()
             break
         else:
             print("Please input a valid character.")
         break
    elif areachoice == "4":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         central_coast_choice = input("Select an Option: ")
         if central_coast_choice == "1":
             central_coast_friendship_averages = (4.81, 2.03, 4.63)
             plt.pie(central_coast_friendship_averages, labels=friendship_group_labels, autopct='%.1f%%', startangle=90)
             plt.title("What is the average makeup of a respondant's friendgroup")
             plt.show()
             break
         elif central_coast_choice == "2":
             central_coast_day_1 = (20, 11)
             plt.pie(central_coast_day_1, labels=day_1_labels, autopct='%.1f%%', startangle=90)
             plt.title("Did respondants know people day 1 year 7?")
             plt.show()
             break
         else:
             print("Please input a valid character.")
         break
    elif areachoice == "5":
         print("=== Choose Your Option ===")
         print("1. Display friend group averages (where friend group members are from)")
         print("2. Display day 1 averages (were people lonely day 1 year 7)")
         hunter_valley_choice = input("Select an Option: ")
         if hunter_valley_choice == "1":
             hunter_valley_friendship_averages = (3.33, 2.33, 4.66)
             plt.pie(hunter_valley_friendship_averages, labels=friendship_group_labels, autopct='%.1f%%', startangle=90)
             plt.title("What is the average makeup of a respondant's friendgroup")
             plt.show()
             break
         elif hunter_valley_choice == "2":
             hunter_valley_day_1 = (1, 1)
             plt.pie(hunter_valley_day_1, labels=day_1_labels, autopct='%.1f%%', startangle=90)
             plt.title("Did respondants know people day 1 year 7?")
             plt.show()
             break
         else:
             print("Please input a valid character.")
             
    else:
         print ("please input a valid number")
         pass
def whole_school_averages():
    while (True):
      print("=== Choose Your Option ===")
      print("1. Display area averages (where people are from)")
      print("2. Display day 1 averages (were people lonely day 1 year 7)")
      print("3. Display friend group averages (where friend group members are from)")      
      whole_school_choice = input("Select an Option: ")
      if whole_school_choice == "1":
        whole_school_area = (22, 4, 2, 32, 4)
        plt.pie(whole_school_area, labels=respondant_location_labels, autopct='%.1f%%', startangle=90)
        plt.title("Where do respondants live?")
        plt.show()
        break
      elif whole_school_choice == '2':
        whole_year_day_1 = (45, 19)
        plt.pie(whole_year_day_1, labels=day_1_labels, autopct='%.1f%%', startangle=90)
        plt.title("Did respondants know people day 1 year 7?")
        plt.show()
        break
      elif whole_school_choice == '3':
        whole_year_friendship_averages = (4.91, 2.47, 4.19)
        plt.pie(whole_year_friendship_averages, labels=friendship_group_labels, autopct='%.1f%%', startangle=90)
        plt.title("What is the average makeup of a respondant's friendgroup")
        plt.show()
        break
      else:
        print ("Please input a proper number")
        pass
      break
def view_visualisations():
  while (True):
    print("=== Choose Your Option ===")
    print("1. Show entire school averages")
    print("2. Filter by year averages")
    print("3. Filter by area averages")
    visualisation_choice = input("Select an Option: ")
    if visualisation_choice == "1":
        whole_school_averages()
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