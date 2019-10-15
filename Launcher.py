from Algorithms import Caesar,Affine,Substitution
import os
selected_alphabet="TR"
selected_algorithm=Caesar

def main_menu():
    global selected_algorithm
    global select_alphabet

    print("Cryptology algorithms")
    print("Selected algorithm:"+selected_algorithm.__name__)
    print("Selected alphabet:"+selected_alphabet)
    print("\n1.Change Algorithm")
    print("2.Change Alphabet")
    print("3.Crypt a text")
    print("4.Decrypt a text")
    print("5.Exit")

    menu_selection=input("Please select an menu item:")
    if menu_selection=="1":
        select_algorithm()
        main_menu()
    if menu_selection=="2":
        select_alphabet()
        main_menu()
    if menu_selection=="3":
        selected_algorithm.encrypt_menu(selected_algorithm)
        main_menu()
    if menu_selection=="4":
        selected_algorithm.decrypt_menu(selected_algorithm)
        main_menu()
    if menu_selection=="5":
        exit()

def select_algorithm():
    global selected_algorithm
    print("1.Caesar Algorithm (Sezar şifrelemesi)")
    print("2.Affine Algorithm (Doğrusal şifreleme)")
    print("3.Substitution Algorithm (Yerine Koyma şifrelemesi)")
    selection=input("Please select an algorithm:")
    if selection=="1":
        selected_algorithm = Caesar
    elif selection=="2":
        selected_algorithm = Affine
    elif selection=="3":
        selected_algorithm = Substitution
    os.system('cls')
def select_alphabet():
    global selected_alphabet
    selected_alphabet=input("'TR' for Turkish alphabet\n'EN' for English alphabet\nPlease select an alphabet:")
    selected_algorithm.setLang(selected_algorithm,selected_alphabet)
    os.system('cls')
if __name__ == "__main__":
    os.system('cls')
    main_menu()