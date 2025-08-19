#file data
from pathlib import Path
import json 

def file_data():

    masir = Path("data/data.json")
    masage = "hello"
    s= {}
    s["massage"] = masage
    j = json.dumps(s , indent= 4 , sort_keys= True)
    a = masir.write_text(j)

file_data()