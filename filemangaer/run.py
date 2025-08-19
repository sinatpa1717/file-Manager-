#file manager 
#programing python
#aug ,16 ,2025 

from open_data import open_json_file
from runcommand import run_command_user

class Manger:
    def __init__(self, name):
        self.name = name 

class File_Manger (Manger):
    def __init__(self, name , a):
        super().__init__(name)
        self.a = a   

    def menu(self):
        flag =True
        while flag:
            massage = f"------welcome to file manger so------"
            print(massage.upper())
            massage1 = "--[1] show list command"
            print(massage1.title())
            massage2 = "--[2] run a command"
            print(massage2.title())
            massage3 = "esc terminal [q]"
            print(massage3.title())
            try:
                massage_user_input = input("Command: ").strip().lower()
                
            except ValueError:
                print("error !".upper())
            except TypeError:
                print("error !".upper())
            except KeyboardInterrupt:
                print("error !".upper())
            except UnboundLocalError:
                print("q ?")

            if massage_user_input == "1":
                open_json_file()
            elif massage_user_input == "2":
                run_command_user()
            elif massage_user_input == "q":
                flag = False

m = Manger(name="")
x = File_Manger(a="" , name="")
x.menu()