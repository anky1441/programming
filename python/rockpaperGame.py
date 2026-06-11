import random
Ai_choice=random.randint(1,3)
chance=0
while True:
    chance=chance+1
    print("press-")
    print("1.) -----------ROCK----------")
    print("2.) ----------PAPPER----------")
    print("3.) ----------SCISSOR---------")
    Your_Choice=int(input("enter your choice from above details-->>>"))
    print("choice of AI from Above details is---",Ai_choice)
    if Your_Choice==Ai_choice:
        print("oh!its draw")
    elif Your_Choice==1 and Ai_choice==2:
        print("OH! YOU LOSE,AI WON")
    elif Your_Choice==1 and Ai_choice==3:
        print("WOW! YOU WON,AI LOSS in",chance,"chances")
        break
    elif Your_Choice==2 and Ai_choice==1:
        print("WOW! YOU WON,AI LOSS in",chance,"chances") 
        break
    elif Your_Choice==2 and Ai_choice==3:
        print("OH! YOU LOSE,AI WON")
    elif Your_Choice==3 and Ai_choice==1:
        print("OH! YOU LOSE,AI WON")
    elif Your_Choice==3 and Ai_choice==2:
        print("WOW! YOU WON,AI LOSS in",chance,"chances")
        break
    else:
        print("!!!!wrong choices!!!")