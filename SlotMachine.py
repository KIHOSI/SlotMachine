from Seven_Segement import SevenSegement #import Seven_Segement.py
import random

# 設定每一個七節管(Wpi)       
seg1 = SevenSegement(7,0,2,3,12,13,14)
seg2 = SevenSegement(21,22,23,24,25,29,28)
seg3 = SevenSegement(27,26,11,10,6,5,4)

while True:
    pinNum = input("請輸入你想顯示的數字(離開請輸入'exit'):")
    if pinNum == "exit":
        seg1.closeAllLight()
        seg2.closeAllLight()
        seg3.closeAllLight()
        break
    else:    
        seg1.call7Segment(random.randint(0,9)) # String to int
        seg2.call7Segment(random.randint(0,9)) # 隨機產生0~9
        seg3.call7Segment(random.randint(0,9))
#seg.call7Segment(0)
#seg.closeAllLight()
#seg.openLight(3)