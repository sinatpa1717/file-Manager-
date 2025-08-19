#test code remove 

from code_remove_file import remove_file

def test_code_remove():
    assert remove_file (remove_file_user_input="sina.txt")
    assert remove_file (remove_file_user_input="str.txt")
    assert remove_file (remove_file_user_input="r.txt")

def test_code_number():
    assert remove_file (remove_file_user_input=1)
    assert remove_file (remove_file_user_input=44)

def test_code_d():
    assert remove_file (remove_file_user_input="sina@.txt")
    assert remove_file (remove_file_user_input="r$.py") 

def tes_cdoe_khali ():
    assert remove_file (remove_file_user_input="")
    assert remove_file (remove_file_user_input=" ")

    

