import random


def guess_the_number(x):

    print("====================")
    print("Welcome to the game!")
    print("====================")

    print(f"Select a number between 1 and {x} so the computer can try to guess it")

    int_lower_limit = 1
    int_upper_limit = x

    str_reply = ""
    while str_reply != "c":
        if int_lower_limit != int_upper_limit:
            prediction = random.randint(int_lower_limit, int_upper_limit)
        else:
            prediction = int_upper_limit    #or "= int_lower_limit", is the same.
        str_reply = input(f"My prediction is {prediction}. Press (H) if its too high, or press (L) if its too low. If its correct, press(C):").lower()

        if str_reply == "h":
            int_upper_limit = prediction - 1
        elif str_reply == "l":
            int_lower_limit = prediction + 1

    print(f"So your number was {prediction} uh? You make it pretty hard!")
    print("Thanks for playing!")


guess_the_number(50) # The computer will guess a number between 1 and 10(You can change the range)