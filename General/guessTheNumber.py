import random

secret_number = random.randint(1,20)
print("I'm thinking of number between 1 and 20")

for i in range(1,7):
    guess = int(input("Take a guess:"))

    if guess > secret_number:
        print("Your guess is too high!")
    elif guess < secret_number:
        print("Your guess is too low!")
    else:
        break

if guess == secret_number:
    print("You took", i , "chances to predict the number", sep=' ')
else:
    print("The secret number is", secret_number, sep=' ')