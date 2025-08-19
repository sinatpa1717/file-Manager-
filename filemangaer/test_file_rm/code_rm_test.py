#test code rm file
from code_rm import code_rm

def test_code_rm():
    assert code_rm (rm_file="sina")
    assert code_rm (rm_file="str")
    assert code_rm (rm_file="r")

def test_code_number_rm():
    assert code_rm (rm_file=1)
    assert code_rm (rm_file=44)

def test_code_d_rm():
    assert code_rm (rm_file="sina@")
    assert code_rm (rm_file="r$") 

def tes_cdoe_khali_rm ():
    assert code_rm (rm_file="")
    assert code_rm (rm_file=" ")

    
