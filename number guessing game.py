import random
playing = True
number = str(random.randint(10,20))
print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time")
print("The game ends when you get 1 hero!")
while playing:
    guess = input("give me your best guess \n")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break

    else:
        print("you guess isn't quite right,try again \n")