# 1) variables and input/output
birth_year = int(input("enter the year you were born: "))
print("you will turn " + str(2025 - birth_year) + " in 2025")

# 2) if/else
import random
number = random.randint(1, 100)
guess_count = 0
while True:
    guess = int(input("guess the number: "))
    guess_count = guess_count + 1
    if guess < number:
        print("too low!")
    elif guess > number:
        print("too high!")
    else:
        print("correct! it took", str(guess_count), "guesses.")
        break

# 3) lists
groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]
print(groceries)
while True:
    item = input("enter an item to remove (or 'stop' to end): ")
    if item == "stop":
        break
    if item in groceries:
        groceries.remove(item)
    print("updated list:", groceries)

# 4) roulette wheel

import random
import time

#function to generate a wheel
def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spin_wheel(spaces):
    return random.choice(spaces)


def play_game():
    money = 1000
    spaces = generate_wheel()

    while True:
        print("you have $" + str(money) + ".")
        bet = input("How much do you want to bet?")
        bet = int(bet)
        color = input("What color do you want to bet on?")

        print("The wheel is spinning. Good luck!")
        time.sleep(2)
        landed = spin_wheel(spaces)
        print("It landed on " + landed + ".")

        if landed == color:
            money = money + bet
            print("Congrats! You now have $" + str(money) + ".")
        else:
            money = money - bet
            print("Sorry! You now have $" + str(money) + ".")

        play_again = input("Do you want to play again?")
        if play_again == "no":
            print("Thank you for playing!")
            break

play_game()


# 5) menu
menu = {"pizza": 1.99, "soda": 0.69, "WINGSTOP TRIPLE CHOCOLATE CHUNK COOKIE": 2.49}

def add_to_menu(item, price):
    menu[item] = price

add_to_menu("hot dog", 1.50)
print(menu)