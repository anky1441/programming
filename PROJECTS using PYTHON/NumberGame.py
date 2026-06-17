import random
random_number=random.randint(1,100)
tries=0
while True:
    tries=tries+1
    guess_Number=int(input("enter your guess number from 1 to 100--->>>"))
    if random_number==guess_Number:
        print("Congratulations!! you Have Won the game in",tries,"tries")
        break
    elif random_number>guess_Number:
        print("Oh! WRONG GUESS Go little bit higher")
    elif random_number<guess_Number:
        print("Oh! WRONG GUESS Go little bit lower")