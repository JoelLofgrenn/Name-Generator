
import random
from time import sleep
import re

try:
    # Open Text file and reads it into the 
    with open('usernames.txt', 'r') as file:
        usernames = [line.strip() for line in file]
except FileNotFoundError:
    print("Filen 'usernames.txt' hittades inte. Kontrollera att den finns i samma mapp som programmet")
    quit()

# Items that are important to the code like Lists and counters
user_len_list = []

user_char_list = []

user_options_counter = 0

while True:
    # User Question for len of the username
    try:
        user_len = int(input("Ange Längden på namnet (5, 6, 2) : \t"))
        if user_len <= 0:
            print("Längden måste vara större än 0")
            continue
        break
    except ValueError:
        print("Du måste ange ett Heltal")

# For loop to check the txt file if there are usernames that matches the lengh of the user question
for i in usernames:
    if user_len == len(i):
        user_options_counter += 1
        user_len_list.append(i)
    
# Checking if the user_len_list is empty or not
if len(user_len_list) == 0:
    print(f"Det finns inge namn som har {user_len} bokstav(er)!")
    quit()
else:
    print("Vänligen Vänta...")

try:
    # User question for what char the username should start with
    user_choice = input("Ange vilken bokstav namnet ska börja på (t.ex. A) :\t ").lower()
    if len(user_choice) > 1:
        print("Du ska bara skriva en bokstav i taget!")
except ValueError:
    print("Något har gått snett, vänligen kör programmet igen...")
    quit()

# Checking if the user has entered null as answer and then making no filter otherwise it check the user_len_list if matches with user choices
try:
    if user_choice == "":
        print("Inget val gjort – använder alla från längd-filtret.\n")
        user_char_list = user_len_list
    else:
        for i in user_len_list:
            if re.match(f'{user_choice}.*',i): 
                user_char_list.append(i)
except ValueError:
    print(f"Det finns inget namn som börjar på {user_choice} med {user_len} bokstäver")

# Using random.choice to choose one random name in the list
if len(user_char_list) >= 1:
    chosen_name = random.choice(user_char_list)
else:
    print("Inget namn har kunnat genererats, vänligen starta programmet på nytt...")
    quit()

# Ask if numbers should be added to the username
add_numbers = input("Vill du lägga till siffror i slutet av namnet? (ja/nej): ").lower()

# If the user choose numbers its take number between 10-999
if add_numbers in ["ja", "j", "yes", "y"]:
    chosen_name += str(random.randint(10, 999))

# Prints The Results
print("\nDitt genererade användarnamn är:", chosen_name)
            
