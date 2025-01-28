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




### 4. Date Manipulations
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

input_date = input("Enter a date (dd/mm/yyyy): ")
date_obj = datetime.strptime(input_date, "%d/%m/%Y")

formatted_date = date_obj.strftime("%A %d %B %Y")
print(f"Formatted Date: {formatted_date}")

day_of_week = date_obj.strftime("%A")
print(f"Day of the Week: {day_of_week}")

new_date = date_obj + timedelta(days=15, hours=23)
print(f"New Date after adding 15 days and 23 hours: {new_date.strftime('%A %d %B %Y, %H:%M')}")

current_date = datetime.now()
six_months_later = current_date + relativedelta(months=6)
print(f"Date 6 months from now: {six_months_later.strftime('%A %d %B %Y')}")
```

---

### 5. Rock, Paper, Scissors Game

import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

options = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in options:
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    if result == "draw":
        print("It's a draw! Let's play again.")
    else:
        print(f"{result.capitalize()} wins!")
        break

