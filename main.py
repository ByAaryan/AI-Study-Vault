from core import *

def main():
    while True:
        print("Welcome to the Application!\n"
        "1. Make a note\n"
        "2. View Notes\n"
        "3. Delete Note\n"
        "4. Exit\n")

        choose = input("Choose an option (1-4): ")

        if choose == '1':
            gen_content()
        elif choose == '2':
            view_notes()
        elif choose == '3':
            delete_note()
        elif choose == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
