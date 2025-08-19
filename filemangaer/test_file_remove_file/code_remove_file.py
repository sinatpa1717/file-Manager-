#code remove 
import os 

def remove_file(remove_file_user_input):
        try:
                x = os.remove(f"{remove_file_user_input}") 
                if remove_file_user_input:
                        return True
                
                elif isinstance(remove_file_user_input , int):
                        return False
                else:
                        return False 
                                         
        except FileNotFoundError:
                return "error".upper()
        

