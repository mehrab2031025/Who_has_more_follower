import random
from game_data import data
from art import logo
from art import vs





print(logo)
a = random.randint(0, len(data) - 1)
a_name = data[a]["name"]
a_description = data[a]["description"]
a_country = data[a]["country"]

b = random.randint(0, len(data) - 1)
b_name = data[b]["name"]
b_description = data[b]["description"]
b_country = data[b]["country"]

print(f"Compare A: {a_name}, a {a_description}, from {a_country}.\n")
print(vs)
print(f"Against B: {b_name}, a {b_description}, from {b_country}.")
user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
score = 0
next_round = True
if user_choice == 'A':
    user_choice = data[a]["follower_count"]
    if user_choice >= data[b]["follower_count"]:
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        next_round = False

else:
    user_choice = data[b]["follower_count"]
    if user_choice >= data[b]["follower_count"]:
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        next_round = False

while next_round:
    print("\n" * 100)
    print(logo)
    print(f"You are right! Current score: {score}.")
    a = b
    a_name = data[a]["name"]
    a_description = data[a]["description"]
    a_country = data[a]["country"]

    b = random.randint(0, len(data) - 1)
    b_name = data[b]["name"]
    b_description = data[b]["description"]
    b_country = data[b]["country"]

    print(f"Compare A: {a_name}, a {a_description}, from {a_country}.\n")
    print(vs)
    print(f"Against B: {b_name}, a {b_description}, from {b_country}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_choice == 'A':
        user_choice = data[a]["follower_count"]
        if user_choice >= data[b]["follower_count"]:
            score += 1
            print(f"You are right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            next_round = False

    else:
        user_choice = data[b]["follower_count"]
        if user_choice >= data[b]["follower_count"]:
            score += 1
            print(f"You are right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            next_round = False