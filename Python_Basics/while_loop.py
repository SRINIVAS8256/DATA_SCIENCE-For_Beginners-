import random
while(1):
    guess=int(input("guess the number"))
    ran=random.randint(1,10)
    if(ran==guess):
        print("u gotchu")
        break
    else:
        print("try again")