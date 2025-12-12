import code

def main():
    while True:
        pets_df = code.pets_csv()
        adopters_df = code.adopters_csv()
        choice = code.main_menu()

        if choice == '1':    
            code.view_available_pets(1, pets_df)

        if choice == '2':
            adopters_df = code.registration(adopters_df, "adopters.csv")

        if choice == '3':
            code.adopter_login(adopters_df)

        if choice == '4':
            code.staff_menu(pets_df, csv_path="pets.csv")

        if choice == '5':
            print("Stopping program...")
            quit()
    
main()
