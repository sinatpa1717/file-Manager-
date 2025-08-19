import os 

def stat_code():
    masir_file_inpu_user = input("name file: ".title())
    x = os.stat(masir_file_inpu_user)
    print(x)
    
