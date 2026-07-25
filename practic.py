import random
import math
MIN_BET=1



def print_lines():
    m=[[],[],[]]
    n=0
    for i in range(3):
        for i in range(3):
            c=random.choice(l)
            m[n].append(c)
            print(c+" | ", end="")
        print("\n")
        n=n+1
    return m


l=["A","B","C"]





def deposit():
    while True:
        global amount
        amount=input("enter your deposit $:")
        if amount.isdigit():
            amount=float(amount)
            if amount>0:
                print(f"saved,your deposit is ${amount}")
                return amount
                break
            else:
                print("your capital is 0")
        else:
            print("print number")

def get_lines():
    while True:
        global lines
        lines=input("enten how much lines you got taken 1 - 3: ",)
        print("\n")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=3 :
                print(f"sucsessfull, you got {lines} lines","\n")
                return lines
                break
            else:
                print("enter greater than 1 and lesser or equal to 3")
        else:
            print("enter number")


def taking_money(balnce):
    while True:
        global bet
        bet=input(f"how much cash you would bet of {lines} lines :")
        print("\n")
        if bet.isalnum():
            bet=float(bet)
            if bet*lines<balnce:
                print(f"succsessfull, you take ${bet*lines} of {lines} lines for each ${bet}","\n")
                return bet
                break
            elif MIN_BET>bet:
                print(f"min bet is: {MIN_BET}")

            else:
                print(f"your balance not enought, balance:${balnce} ","\n")
        elif bet.isalpha():
            print("enter number!","\n")

def check_wins():
    win=0
    for n in range(lines):
        if list_lines[n][0]==list_lines[n][1] and list_lines[n][0]==list_lines[n][2]:
            win+=(bet*0.1)+bet

    return win 

def banck_account(balance,bet,won:int): 
    balance-=bet*lines
    if won>0:
        balance+=won
    return balance




def restart():
    global lines_
    amo=deposit()
    while True:
        print(amo)  
        def main():  
            nonlocal amo
            global t
            global list_lines
            global lines_


            lines_=get_lines()
            t=taking_money(amo)
            list_lines=print_lines()
            win=check_wins()
            print(amo)
            amo=banck_account(amo,t,win)
            
            print(f"balance:{amo} , win: {win}")
            return amo


        d=main()
        if d<=2:
            print(f"your balance it's over! go home!,balance:{amo}")
            break
        q=input("do u wanna quit ?,q-for quit :")
        if q.lower()=="q":
            print("see ya later")
            break

   
restart()