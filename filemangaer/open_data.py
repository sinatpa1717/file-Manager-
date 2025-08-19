import json
from pathlib import Path
def open_json_file():
    with open (f"data/data.json" , "r") as f:
        x = json.load(f)
        print(json.dumps(x , indent= 4 , ensure_ascii=False))
