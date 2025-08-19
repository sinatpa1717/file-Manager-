#mkdir 
import os 
def mkdir_user_file():
    flag = True    
    while flag:
        try:
            name_file_user = input("name file: ".title())
            if  name_file_user == "q":
                flag = False
                break

            for i in os.mkdir(f"{name_file_user}"):
                print(i)

        except TypeError:
            pass
        except FileExistsError:
            print("error !".upper())
        except UnboundLocalError:
            pass