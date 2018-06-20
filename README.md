# Raspberry Pi Slot Machine Game! 

This is a Iot class final project. It's a slot machine game used by raspberry pi.

![](https://i.imgur.com/idJTKBQ.jpg)

## Equipment List
- Raspberry Pi 3
- Micro SD Card
- Seven-segment * 3
- 3.5mm audio earphone
- Raspberry Pi Extension T Board
- Breadboard
- Dupont Line Male To Male * 24
- Power cable

## Program Language
- Python3
- Node.js
- HTML5
- AJAX

## How To Use
[Demo Video](https://drive.google.com/file/d/1DY_vKu5d-Dqso9tiCLdpYzbAYrO7x64q/view?usp=sharing)

1. Use your mobile to connect the [website](192.168.43.65:8080), and you can see some number showing in this website.
This website is catching your mobile **gyroscope sensor** and **accelerometer sensor** and get your action. When you shake your mobile "enough", It will inovke Node.js server.

2. Node.js server will inovke python script, showing some random number (ranged from 0 to 9, including 0 and 9) on seven segement separately. There are three seven segements.

3. When these three seven segements shows same number (ex. 777), it will play music from raspberry pi. And you have to use 3.5mm earphone to listen music. (In this project, I use "Taeyeon - I(Inst.)" music. This song is really great ^__^/

4.If you don't want to play this game, just click "Game Over" button, and it will stop showing numbers on seven segements!

## How It Works

Ok, let's get into the main topic!
I suppose you have just set up a raspberry pi and can connect your rpi with ssh and vnc, so I will introduce after that steps.

### Use Conda
Conda is an open source package management system and environment management system for installing multiple versions of software packages and their dependencies and switching easily between them. [URL](https://anaconda.org/anaconda/conda)

In this project, we use [berryconda](https://github.com/jjhelmus/berryconda), is based on conda.


#### Install Berryconda
``` wget http://repo.continuum.io/berryconda/Berryconda3-latest-Linux-armv7l.sh # download berryconda file
    sudo md5sum Berryconda3-latest-Linux-armv7l.sh # (optional) check md5
    chmod +x Berryconda3-2.0.0-Linux-armv7l.sh # when you download file, change the authority to make this file executable
    sudo /bin/bash Berryconda3-latest-Linux-armv7l.sh # -> change default directory to /home/pi/berryconda3
```

**Notice:**
when you enter "sudo /bin/bash Berryconda3-2.0.0-Linux-armv7l.sh", remeber change your directory path.
```
  [/root/berryconda3] >>> /home/pi/berryconda3
```

Also change your path in .bashrc and reboot your rpi.
```
  sudo nano /home/pi/.bashrc # -> add: export PATH="/home/pi/berryconda3/bin:$PATH"
  sudo reboot -h now
```

And enter ```conda``` to check if conda is seted successfully.

#### Created conda virtual environment
Create your conda environment, and my conda environment's name is ```first_env```
```
  conda create --name myenv #enter name you want
```
When conda asks you to proceed, type ```y```
```
  proceed ([y]/n)?
```
And then inovke this environment.
```
    source activate first_env # inovke environment
    source deactivate # close environment
```

### Conda install 
You can install python package with conda. For example, if you want to install ```Scipy``` package:
```
    conda install scipy
```

### Blink Seven Segemnet
Before doing this step, you have to know [Seven-segement Display](https://en.wikipedia.org/wiki/Seven-segment_display) and [Raspberry Pi GPIO](https://pinout.xyz/), and connect correct dupont lines to correct ports.

![](https://i.imgur.com/9UeGIev.jpg)
![](https://i.imgur.com/7dqCi8Y.png)

In this part, I use ```python3``` language and ```wiringpi``` python language to blink seven-segement.
So you have to install them before.

```
    # update your package
    sudo apt-get update
    sudo apt-get upgrade
    # install python 3
    sudo apt-get install python3
    # install wiringpi
    pip install wiringpi
```

And I write two python file, ```SlotMachine.py``` and ```Seven_Segement.py```. 

SlotMachine.py
```
from Seven_Segement import SevenSegement #import Seven_Segement.py
import random
import os
import sys

# Set every segement number(Wpi)
print("init")
seg1 = SevenSegement(7,0,2,3,12,13,14)
seg2 = SevenSegement(21,22,23,24,25,29,28)
seg3 = SevenSegement(27,26,11,10,6,5,4)

#Game Start
def gameStart():
    print("start")
    #randNum1 = random.randint(0,9)
    #randNum2 = random.randint(0,9)
    #randNum3 = random.randint(0,9)   
    randNum1 = randNum2 = randNum3 = 7
    seg1.call7Segment(randNum1) # String to int
    seg2.call7Segment(randNum2) # generate random number 0~9
    seg3.call7Segment(randNum3)
    if(randNum1 == randNum2==randNum3): #If numbers are same
        print("bingo!!!")
        # play victory music
        os.system('mpg321 /home/pi/SlotMachineFile/I.mp3');


def closeSegement(): # close all seven-segements
    print("close")
    seg1.closeAllLight()
    seg2.closeAllLight()
    seg3.closeAllLight()


```

Seven_Segement.py
```
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

    # show number on seven-segement
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

    # open part of seven-segement
    def openLight(self,num):
        wiringpi.pinMode(num,1) # Set num to 1 ( OUTPUT )
        wiringpi.digitalWrite(num,1) # Write 1 ( HIGH ) to num
        wiringpi.digitalRead(num) # Read num

    # close part of seven-segement
    def closeLight(self,num):
        wiringpi.pinMode(num,1) # Set num to 1 ( OUTPUT )
        wiringpi.digitalWrite(num,0) # Write 0 (Low) to num
        wiringpi.digitalRead(num) # Read num

    # close all parts of seven-segment
    def closeAllLight(self):
        for i in self.closeAll:
            wiringpi.pinMode(i,1) # Set num to 1 ( OUTPUT )
            wiringpi.digitalWrite(i,0) # Write 0 (Low) to num
            wiringpi.digitalRead(i) # Read num
```

