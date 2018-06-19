from Seven_Segement import SevenSegement #import Seven_Segement.py
import random
import os
import sys

# 設定每一個七節管(Wpi)
print("init")
seg1 = SevenSegement(7,0,2,3,12,13,14)
seg2 = SevenSegement(21,22,23,24,25,29,28)
seg3 = SevenSegement(27,26,11,10,6,5,4)

#Game Start
def gameStart():
    print("start")
    randNum1 = random.randint(0,9)
    randNum2 = random.randint(0,9)
    randNum3 = random.randint(0,9)   
    seg1.call7Segment(randNum1) # String to int
    seg2.call7Segment(randNum2) # 隨機產生0~9
    seg3.call7Segment(randNum3)
    if(randNum1 == randNum2==randNum3): #如果顯示數字都相同
        print("bingo!!!")
        #放勝利音樂
        os.system('mpg321 /home/pi/SlotMachineFile/I.mp3');


def closeSegement(): #關閉所有7節管
    print("close")
    seg1.closeAllLight()
    seg2.closeAllLight()
    seg3.closeAllLight()

