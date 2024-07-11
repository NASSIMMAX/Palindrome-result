# here is
import time as tm
import os
from colorama import Fore, Style


nums = input("enter a number : ".capitalize())
seqNum = 0
run = True
while run:
    os.system('cls')

    def main(num):
        Xnum = [int(x) for x in str(num)]
        Xnum.reverse()
        # ---------------
        revNum = str(Xnum)[1:-1].replace(",", "").replace(' ', "")
        return int(revNum)

    eRevNum = main(nums)
    seqNum += 1
    calaculNum = 0

    def calcul(rn):
        global calaculNum
        calaculNum = rn + int(nums)
        print(f"{Fore.RED}Sequence :{Style.RESET_ALL} {seqNum}")
        print(f"""

              {nums}
            + {rn}
            -----------
            = {Fore.BLUE} {calaculNum} {Style.RESET_ALL}
            """)

    calcul(eRevNum)
    nums = calaculNum

    def findPal(sumNum):
        listNumsRes = [int(i) for i in str(sumNum)]
        fNums = listNumsRes[:2]
        LNums = listNumsRes[-2:]
        LNums.reverse()
        if fNums == LNums:
            print(f"{Fore.GREEN}PALINDROME RESULT FOUND!{Style.RESET_ALL}")
            tm.sleep(2)
            btn = input('press enter to restart >>'.capitalize())
            if btn == "":
                os.system('cls')
                global nums
                global seqNum
                nums = input("enter a number : ".capitalize())
                seqNum = 0
            elif btn == "exit":
                global run
                run = False

    findPal(calaculNum)

    tm.sleep(1)
