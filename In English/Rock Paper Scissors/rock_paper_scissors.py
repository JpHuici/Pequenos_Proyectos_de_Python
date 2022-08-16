import random


def play():


    print("===================")
    print("Welcome to the game!")
    print("===================")

    str_user = input("Choose an option: 'rock', 'paper', or 'scissors:' \n").lower() # User select an option, he can use lowercase or uppercase.
    str_computer = random.choice(['rock','paper','scissors']) # The computer select an option,randomly.
    str_choice = (f"The computer choose {str_computer} and you choose {str_user}.") # Show the selected options of each one.
    print(str_choice)

    if str_user == str_computer: # If they select the same option.
        return "I´ts a tie!"

    if computer_wins(str_computer, str_user): # If computer beat user.
        return "Oh, you lost!"

    return "Congrats,you win!" # If user beat computer.


def computer_wins(str_computer, str_user):
    # The function returns "True" if the opponent(str_computer) wins.
    # Rock wins to scissors (rock > scissors).
    # Scissors wins to paper (scissors > paper).
    # Paper wins to rock (paper > rock).
    if ((str_computer == "rock" and str_user == "scissors") 
        or (str_computer == "scissors" and str_user == "paper") 
        or (str_computer == "paper" and str_user =="rock")):
        return True
    else:
        return False


print(play())