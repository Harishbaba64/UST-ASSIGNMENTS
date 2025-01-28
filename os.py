import os

downloads_folder = os.path.expanduser("~/Downloads")

for item in os.listdir(downloads_folder):
    item_path = os.path.join(downloads_folder, item)
    if os.path.isfile(item_path):
        print(f"{item} - File")
    elif os.path.isdir(item_path):
        print(f"{item} - Folder")

###2. Print all ASCII letters defined in the `string` module
import string

print(string.ascii_letters)




###3. Randomly sample five letters using `random.sample` and `string.ascii_letters`

from random import sample
from string import ascii_letters

five_letters = ''.join(sample(ascii_letters, 5))
print(five_letters)
