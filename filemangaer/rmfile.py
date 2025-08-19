# rm file
import os 
def rmfile_user ():
    flag = True 
    while flag:
        try:
            massage_user_input = input("name file: ".title())
            x = os.rmdir(massage_user_input)
        except FileNotFoundError:
            pass
        if massage_user_input == "q":
            flag = False
            break
