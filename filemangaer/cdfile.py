#c
import os
def cd_file_user():
    flag = True
    while flag:
        try:
            masir = input(":masir ")
            if masir == "q":
                flag = False
            os.chdir(masir)
        except FileNotFoundError:
            pass