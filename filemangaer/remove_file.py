#remove file
import os 
def remove_file_user():
    flag = True
    while flag:
        try:
            remove_file_user_input = input("name file: ".title())
            if remove_file_user_input == "q":
                flag = False
            x = os.remove(f"{remove_file_user_input}")
        except FileNotFoundError:
            print("error !".upper())
