# run code user
from mkdir import mkdir_user_file
from rmfile import rmfile_user
from remove_file import remove_file_user
from pwdfilem import pwd_user
from cdfile import cd_file_user
from seachfile import seach_file_user
from ls import os_code
from statcode import stat_code
import os 

def run_command_user():
    massage = "esc terminal [esc]"
    print(massage)
    flag = True 
    while flag:
        try:
            run_command_user_input = input(": ").strip().lower()
            if run_command_user_input == "mkdir":
                mkdir_user_file()
            elif run_command_user_input == "rm":
                rmfile_user()
            elif run_command_user_input == "remove":
                remove_file_user()
            elif run_command_user_input == "pwd":
                pwd_user()
            elif run_command_user_input == "cd":
                cd_file_user()
            elif run_command_user_input == "search":
                seach_file_user()
            elif run_command_user_input == "ls":
                os_code()
            elif run_command_user_input == "stat":
                stat_code()
                
        except TypeError:
            print("error !".upper())
        except KeyboardInterrupt:
            massage_userr = "esc?"
            print(massage_userr)
        except UnboundLocalError:
            massage_user = "esc?"
            print(massage_user)

        if run_command_user_input == "q":
            flag  = False

