import random
import time
from turtle import ycor
from colorama import Fore, Back, Style, init

cMoney = 1000
yCard = 0
drawing = True
ws = 0

while True:
    bCard = random.randint(12,20)
    print(Fore.GREEN + f"${str(cMoney)}")
    try:
        bMoney = input(Fore.WHITE + "How much money do you want to bet?\n")
        if int(bMoney) < 1:
            print(Fore.RED + "Amount less than one.")
            break
        if int(bMoney) > cMoney:
            print(Fore.RED + "Amount over your current money.")
            break
    except ValueError:
        print(Fore.RED + "Not a valid amount.")
        break
    bMoney = int(bMoney)
    yCard = yCard + random.randint(1,10)
    print(f"Your Score: {str(yCard)}")
    while drawing == True:
        inp = input("Would you like to draw again?\n")
        if inp.lower() == "no":
            drawing = False
            break
        yCard = yCard + random.randint(1,10)
        print(f"Your Score: {str(yCard)}")
        time.sleep(0.5)
    print(f"Bot Score: {str(bCard)}")
    if bCard > yCard:
        ws = 0
        print("You Lost")
        cMoney = cMoney - bMoney
    else:
        if yCard > 21:
            ws = 0
            print("You Lost")
            cMoney = cMoney - bMoney
        else:
            ws = ws + 1
            print(f"You Won, Winning Streak: {str(ws)}!")
            bMoney = bMoney * 2
            cMoney = cMoney + bMoney
    
    drawing = True
    yCard = 0