import pandas as pd
def adopters_csv():
    adopters_df = pd.read_csv("adopters.csv")
    adopters_df.head()
    return adopters_df
    #print(adopters_df.head())
    
def pets_csv():    
    pets_df = pd.read_csv("pets.csv")
    pets_df.head()
    return pets_df
    #print(pets_df.head())
def main_menu():
    print("1. View Available Pets")
    print("2.Register as New Adopter")
    print("3.Adopter Login")
    print("4.Staff Menu")
    print("5. Quit")
    choice_user = input("where do you want to access: ")
    #print(f"inside main menu {choice_user}")
    return choice_user
    
def view_available_pets(choice,pets_df):
    print(pets_df.head())
    #print(f"inside veiw_available_pets {choice}")

def registration():
     name = input("full name (must be at least 2 words)")
     home_type =  input("Home type (Flat, House, or Farm only)")
     experience = input("Experience level (None, Some, or Expert)")
     pet_size = input("Preferred pet size (Small, Medium, Large, or Any)")
     energy_level = input("Preferred energy level (Low, Medium, High, or Any)")

def login_page():
    adopters_df = adopters_csv()
    login = input("what is your ID: ")

def main():
    pets_df = pets_csv()
    adopters_df = adopters_csv()
    choice = main_menu()
    if choice == '1':    
        view_available_pets(1, pets_df)
    #print(f"inside main {choice}")
    if choice == '2':
        registration()
    if choice == '3':
        login_page()
    if choice == '4':
        pass
    if choice == '5':
        pass  

    
    
main()
