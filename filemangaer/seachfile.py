# search
import os
def seach_file_user ():
    flag = True
    while flag:
        try:
            seach_file_user_input = input("search file: ")
            if seach_file_user_input == "q":
                flag = False
        except ValueError:
            print("error !".upper())
            
        x = os.path.exists(seach_file_user_input)
        if x :
            print("this file")
        else:
            print("not file")
                