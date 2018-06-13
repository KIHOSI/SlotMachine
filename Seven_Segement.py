import wiringpi
wiringpi.wiringPiSetup() # For Wpi pin numbering

class SevenSegement():
    def __init__(self,a,b,c,d,e,f,g):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.showZero = [a,b,c,d,e,f]
        self.showOne = [b,c]
        self.showTwo = [a,b,d,e,g]
        self.showThree = [a,b,c,d,g]
        self.showFour = [b,c,f,g]
        self.showFive = [a,c,d,f,g]
        self.showSix = [a,c,d,e,f,g]
        self.showSeven = [a,b,c]
        self.showEight = [a,b,c,d,e,f,g]
        self.showNine = [a,b,c,d,f,g]
        self.closeAll = [a,b,c,d,e,f,g]
        print("success")

    # 函式要放前面，不然後面沒辦法定義
    # 依據想顯示的數字，呼叫對應七節管位置
    def call7Segment(self,num):
        self.closeAllLight()
        if num == 0:
            for i in self.showZero:
                self.openLight(i)
        elif num == 1:
            for i in self.showOne:
                self.openLight(i)
        elif num == 2:
            for i in self.showTwo:
                self.openLight(i)        
        elif num == 3:
            for i in self.showThree:
                self.openLight(i)
        elif num == 4:
            for i in self.showFour:
                self.openLight(i)
        elif num == 5:
            for i in self.showFive:
                self.openLight(i)
        elif num == 6:
            for i in self.showSix:
                self.openLight(i)
        elif num == 7:
            for i in self.showSeven:
                self.openLight(i)
        elif num == 8:
            for i in self.showEight:
                self.openLight(i)
        elif num == 9:
            for i in self.showNine:
               self.openLight(i)        
        else:
            print("顯示錯誤!!!!")

    # 開啟7節管控燈位置
    def openLight(self,num):
        wiringpi.pinMode(num,1) # Set num to 1 ( OUTPUT )
        wiringpi.digitalWrite(num,1) # Write 1 ( HIGH ) to num
        wiringpi.digitalRead(num) # Read num

    # 關閉指定7節管控燈位置
    def closeLight(self,num):
        wiringpi.pinMode(num,1) # Set num to 1 ( OUTPUT )
        wiringpi.digitalWrite(num,0) # Write 0 (Low) to num
        wiringpi.digitalRead(num) # Read num

    # 關掉所有的數字顯示
    def closeAllLight(self):
        for i in self.closeAll:
            wiringpi.pinMode(i,1) # Set num to 1 ( OUTPUT )
            wiringpi.digitalWrite(i,0) # Write 0 (Low) to num
            wiringpi.digitalRead(i) # Read num