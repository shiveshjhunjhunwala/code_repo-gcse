import pandas as pd
def adopters_csv():
    adopters_df = pd.read_csv("adopters.csv")
    adopters_df.head()
    return adopters_df
    
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
    temp_pets_df = pets_df
    temp_pets_df = temp_pets_df.sort_values(by="DaysInCentre", ascending = False)
    temp_pets_df = temp_pets_df[temp_pets_df["Status"] == "Available"]
    print("")
    print(temp_pets_df)
    #print(f"inside veiw_available_pets {choice}")

def registration(adopters_df):
    name = input("full name (must be at least 2 words)")
    home_type =  input("Home type (Flat, House, or Farm only)")
    experience = input("Experience level (None, Some, or Expert)")
    pet_size = input("Preferred pet size (Small, Medium, Large, or Any)")
    energy_level = input("Preferred energy level (Low, Medium, High, or Any)")
    if len(name.split(" ")) > 0 and home_type in ['flat', 'house', 'farm'] and  experience in ['none', 'some', 'expert'] and pet_size in ['small', 'medium', 'large', 'any'] and energy_level in ['low' , 'medium' , 'high' , 'any']:
        
    else:
        print('false')
         



def adopter_login(adopters_df):
    user_ID = input("ID must be exactly 4 characters (letter A + 3 digits)")
    if user_ID in set(adopters_df["AdopterID"]):
        print("found")
    else:
        print("ERROR")
        print(main_menu())

def staff_menu():
    password = "pawsadopt2024"
    count = 3
    staff_password = input("what is your password: ")
    if staff_password == password:
        print("staff options")
    

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
        adopter_login(adopters_df)
    if choice == '4':
        staff_menu()
    if choice == '5':
        print("Stopping program...")
        quit()
    
main()
