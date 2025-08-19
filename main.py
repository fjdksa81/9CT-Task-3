from data_function import (
    year_averages,
    area_averages,
    view_visualisations,
    view_data
)

def user_interface():
    while True:
       print("=== Choose Your Option ===")
       print("1. View Dataset")
       print("2. View visualisations")
       print("3. Exit Program")
       ui_choice = input("Select and Option: ")

       if ui_choice  == "1":
           view_data()
       elif ui_choice == "2":
           view_visualisations()
       elif ui_choice == "3":
           break
       else:
           print ("Please put in a number 1-3")
           pass
       
if __name__ == "__main__":
    user_interface()