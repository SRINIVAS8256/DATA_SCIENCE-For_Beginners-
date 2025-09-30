import random
jackpot=random.randint(1,100)

guess=int(input("guess the number"))
while(guess != jackpot):
    if(guess>jackpot):
        print("guess lower")
    else:
        print("guess higher")

    guess = int(input("guess the number"))
print("you win",jackpot)