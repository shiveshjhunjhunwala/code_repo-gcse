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
    print("the average days is: ", temp_pets_df["DaysInCentre"].sum()/len(temp_pets_df["DaysInCentre"]))
    
    #print(f"inside veiw_available_pets {choice}")

def registration(adopters_df, csv_path="adopters.csv"):
    name = input("Full name (at least 2 words): ").strip()
    home_type = input("Home type (Flat, House, Farm): ").strip().lower()
    experience = input("Experience (None, Some, Expert): ").strip().lower()
    pet_size = input("Preferred pet size (Small, Medium, Large, Any): ").strip().lower()
    energy_level = input("Preferred energy level (Low, Medium, High, Any): ").strip().lower()

    if not (
        len(name.split()) >= 2 and
        home_type in ['flat', 'house', 'farm'] and
        experience in ['none', 'some', 'expert'] and
        pet_size in ['small', 'medium', 'large', 'any'] and
        energy_level in ['low', 'medium', 'high', 'any']
    ):
        print("error.")
        return adopters_df

    if adopters_df.empty:
        new_no = 1
    else:
        last_id = adopters_df["AdopterID"].str[1:].astype(int).max()
        new_no = last_id + 1

    new_id = "A" + str(new_no).zfill(3)

    new_row = {
        "AdopterID": new_id,
        "Name": name,
        "HomeType": home_type,
        "Experience": experience,
        "PetSize": pet_size,
        "EnergyLevel": energy_level
    }

    adopters_df = pd.concat([adopters_df, pd.DataFrame([new_row])], ignore_index=True)
    adopters_df.to_csv(csv_path, index=False)

    print("you are now registered in! Your ID is:", new_id)
    return adopters_df




def adopter_login(adopters_df):
    user_ID = input("ID must be exactly 4 characters (letter A + 3 digits)")
    if user_ID in set(adopters_df["AdopterID"]):
        print("Nice! You are now logged in: ", adopter_menu())
    else:
        print("ERROR")
        print(main_menu())

def staff_menu():
    password = "pawsadopt2024"
    count = 3
    staff_password = input("what is your password: ")
    if staff_password == password:
        print("staff options")

def adopter_menu():
    choice = input("where do you want to access: ")
    if choice == '1':    
        print("View My Compatibility Matches: ")

    if choice == '2':
        print('Reserve a Pet')

    if choice == '3':
        print("View My Reserved/Adopted Pets")

    if choice == '4':
        print("Logout")
    

    

def main():
    pets_df = pets_csv()
    adopters_df = adopters_csv()
    choice = main_menu()

    if choice == '1':    
        view_available_pets(1, pets_df)

    if choice == '2':
        adopters_df = registration(adopters_df, "adopters.csv")

    if choice == '3':
        adopter_login(adopters_df)

    if choice == '4':
        staff_menu()

    if choice == '5':
        adopter_menu()

    if choice == '6':
        print("Stopping program...")
        quit()
    
main()
