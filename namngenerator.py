
import random
from time import sleep
import re

# Open Text file and reads it into the 
with open('usernames.txt', 'r') as file:
    usernames = [line.strip() for line in file]

# Items that are important to the code like Lists and counters
user_len_list = []

user_char_list = []

user_options_counter = 0


# User Question for len of the username
try:
    user_len = int(input("Ange Längden på namnet (5, 6, 2) : \t"))
except ValueError:
    print("Du måste ange ett Heltal")
    quit()

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

# User question for what char the username should start with
user_choice = input("Ange vilken bokstav namnet ska börja på (t.ex. A) :\t ").lower()

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

# Checking if user_char_list has more then 1 item in it and then choosing one random item from the list.   
if len(user_char_list) >= 1:
    print(random.choice(user_char_list))
else:
    print("Inget namn har kunnat genererats, Vänligen starta programmet och skapa ett nytt användarnamn...")

            