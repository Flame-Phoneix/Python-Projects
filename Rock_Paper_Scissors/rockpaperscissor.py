import random
ROCK = "r"
PAPER = "p"
SCISSORS = "s"
emojis = {ROCK:"🪨",PAPER:"📃", SCISSORS:"✂️"}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper or Scissor? (r/p/s): ").lower()    
        if user_choice not in choices:
            print("invalid choice")
        else:
            return user_choice
        
def display_choice(user_choice, computer_choice, emojis):
    print(f"You chose {emojis.get(user_choice)}")
    print(f"computer chose {emojis.get(computer_choice)}")


def compare(ch, c_ch):
    if ch == c_ch:
        print("Draw")
    elif (ch == ROCK and c_ch == SCISSORS) or (ch == PAPER and c_ch == ROCK) or (ch == SCISSORS and c_ch == PAPER):
        print("You Won!!")
    else:
        print("You Lost!!")
        
def play_game():
    while True:

        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choice(user_choice, computer_choice, emojis)

        compare(user_choice, computer_choice)
        con = input("Do you want to continue? (y/n): ").lower()
        if con == "n":
            print("Thank you for playing")
            break


play_game()