import random


def guess_the_number(x):

    print("===================")
    print("Welcome to the game!")
    print("===================")
    print("Your goal is to guess the number that the computer created.")

    random_number = random.randint(1,x) #Random number between 1 and x

    prediction = 0

    while prediction != random_number:
        prediction = int(input(f"Guess the number between 1 and {x}: "))

        if prediction < random_number:
            print("Try again. Your number is too small!")
        elif prediction > random_number:  
            print("Try gain. Your number is too big!")  

    print(f"Congrats! You guess the number {random_number} correctly!!!")
    print("Thank you for playing!")        

guess_the_number(50)    