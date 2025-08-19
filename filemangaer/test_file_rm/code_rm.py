# code rm file 
import os 

def code_rm(rm_file):
    try:
        if isinstance (rm_file , int):
            return False
        
        os.rmdir(rm_file)
        return True
        
    except FileNotFoundError:
        return "error".upper()
    
