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




def adopter_login(adopters_df,pets_df):
    user_ID = input("ID must be exactly 4 characters (letter A + 3 digits)")
    if user_ID in set(adopters_df["AdopterID"]):
        print("YOU CAN NOW ACCESS ADOPTER PAGE")
        print(adopter_menu(,adopters_df, pets_df, user_ID))
    else:
        print("ERROR")
        print(main_menu())

def staff_menu(pets_df, csv_path="pets.csv"):
    password = "pawsadopt2024"
    count = 4
    staff_password = input("what is your password: ")
    if staff_password == password:
        print("STAFF OPTIONS")
        print(staff_actual_menu())
    else:
        count -=1
        second_attempt = input("what is your password: ")
        if second_attempt == password:
            print("STAFF OPTIONS")
            print(staff_actual_menu())
        else:
            third_attempt = input("Last attempt: what is the password: ")
            count -= 1
            if third_attempt == password:
                print("STAFF OPTIONS")
                print(staff_actual_menu())
            else:
                print("you have been sent to main menu again")
                return
    if count == 0:
        #print(main())
        return 
def staff_actual_menu():
            print("1. Add New Pet")
            print("2.Complete an Adoption")
            print("3.View All Pets (including adopted)")
            print("4.View Statistics")
            print("5. Remove a Pet")
            print("6. Logout")
            choice = input("where do you want to access: ")
            if choice == "1":
                name = input("Pet name: ").strip()
                pet_type = input("Pet type (Dog, Cat, Rabbit, Hamster): ").strip().title()
                age_input = input("Age (0-20): ").strip()
                size = input("Size (Small, Medium, Large): ").strip().title()
                energy = input("Energy level (Low, Medium, High): ").strip().title()
                fee_input = input("Adoption fee (£20-£300): ").strip()
                if name == "":
                    print("Error")
                    return
                if pet_type not in ["Dog", "Cat", "Rabbit", "Hamster"]:
                    print("Error")
                    return
                if not age_input.isdigit():
                    print("Error")
                    return
                age = int(age_input)
                if age < 0 or age > 20:
                    print("Error")
                    return
                if size not in ["Small", "Medium", "Large"]:
                    print("Error")
                    return
                if energy not in ["Low", "Medium", "High"]:
                    print("Error")
                    return
                if not fee_input.isdigit():
                    print("Error")
                    return
                fee = int(fee_input)
                if fee < 20 or fee > 300:
                    print("Error")
                    return
                pets = []
                with open("Pets.csv", "r") as file:
                    reader = pets.csv.reader(file)
                    for row in reader:
                        pets.append(row)

                if len(pets) <= 1:
                    new_no = 1
                else:
                    last_id = pets[-1][0]
                    number = int(last_id[1:])
                    new_no = number + 1

                pet_id = "P" + str(new_no).zfill(3)

                new_pet = [
                    pet_id,
                    name,
                    pet_type,
                    str(age),
                    size,
                    energy,
                    str(fee),
                    "Available",
                    "0"
                ]

                pets.append(new_pet)
            if choice == "2":
                pass
            if choice == "3":
                pass
            if choice == "4":
                pass
            if choice == "5":
                pass
            if choice == "6":
                print("logging out...")
                quit()



        

def adopter_menu(pets_df,user_ID):
    print("1. View My Compatibility Matches")
    print("2.Reserve a Pet")
    print("3.View My Reserved/Adopted Pets")
    print("4.Cancel a Reservation")
    print("5. Logout")
    
    choice = input("where do you want to access: ")
    if choice == '1':    
            pets_df=pets_df[pets_df['Status']=='Available']
    score=0
    df_adopter = df_adopter[df_adopter["AdopterID"]== user_ID]
    home_type=df_adopter.iloc[0]["HomeType"]
    size=df_adopter.iloc[0]["PreferredSize"]
    prefered_energy=df_adopter.iloc[0]["PreferredEnergy"]
    adopter_experience = df_adopter.iloc[0]["Experience"]
    pet_energy = pets_df.iloc[0]["Energy"]
    pet_age = pets_df.iloc [0]["Age"]
    rating=0
    print("Home is ", home_type)
    print("Prefered size", size)
    print("Energy",prefered_energy)
    df_with_score=pd.DataFrame(columns=['PetID', 'Score', 'Rating'])
    for i, r in pets_df.iterrows():
        score=0
        if r["Type"]=="Dog" and r["Size"]=="Large" and home_type=="Flat":
            score=score-20
        if r["Type"]=="Dog" and home_type=="Farm":
            score=score+15
        if (r["Type"]=="Rabbit" or r["Type"]=="Cat" or r["Type"]=="Hamster") and home_type=="Flat":
            score=score+10       
        if size==r["Size"]:
            score=score+20
        if size=="Any":
            score=score+10        
        if r["Energy"]==prefered_energy:
            score=score+20
        if prefered_energy=="Any":
            score=score+10
        if adopter_experience == "Expert":
            score = score + 15
        if adopter_experience == "Some":
            score = score + 10
        elif pet_energy == "High" and adopter_experience == "None":
            score = score - 15 
        if pet_age >= 6:
            score = score + 10
        if(score >=50):
            rating= "Excellent Match! 3 stars"
        if(score>=30 and score<50) :
            rating= "Good Match! 2 stars"
        if(score>=10 and score<30):
            rating= "Possible Match! 1 star"
        if(score<10):
            rating= "Not recommended! 0 star"
        global filter_df
        df_with_score.loc[i]=[r["PetID"], score, rating]
        filter_df = df_with_score.sort_values("Score", ascending = False)
    print("Now showing scores:") 
    print(filter_df)
    if choice == '2':
        print('Reserve a Pet')

    if choice == '3':
        print("View My Reserved/Adopted Pets")

    if choice == '4':
        print("Cancel a reservation")
    if choice == '5':
        print("logout")

    

    