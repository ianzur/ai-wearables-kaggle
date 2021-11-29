
from pathlib import Path
from pprint import pprint

path = path = Path.cwd() / "data" / "video" / "train" / "train"


keys = []

for p in path.iterdir():

    # eg. "CLOCKWISE, UP, ..."
    if p.is_dir():

        label = p.stem.lower()

        for example in p.iterdir():
                                
            if example.is_dir():
                key = example.stem
                keys.append(key)
                image_list = sorted(list(example.glob("*.jpg")), key=lambda i: i.stem.split("_")[-1])
                
                pprint(image_list)
                
                break
                
       

my_dict = {i:keys.count(i) for i in keys}
print(my_dict)
print(keys)
unique_keys = set(keys)
print(len(keys), len(unique_keys))
