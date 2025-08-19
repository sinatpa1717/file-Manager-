import os 

def mkdir_test_code_file_t(name_file_user):
    try:
        if not name_file_user:
            return "error"

        os.mkdir(name_file_user)

        if isinstance(name_file_user, int):
            return False
        else:   
            return os.path.exists(name_file_user)
    
    except TypeError:
        return "error"
    except AssertionError:
        return False
    except FileNotFoundError:
        return "error"  

