#create me a program that can guess a number between 1 and 100
#the program should ask the user to guess a number
#the program should tell the user if the guess is too high or too low
#the program should tell the user if the guess is correct
#the program should tell the user how many guesses it took to get the correct answer
import random
num = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100: "))
count = 1
while guess != num:
    if guess < num:
        print("Too low")
        guess = int(input("Guess again: "))
        count += 1
    elif guess > num:
        print("Too high")
        guess = int(input("Guess again: "))
        count += 1
print("You got it in", count, "tries")
