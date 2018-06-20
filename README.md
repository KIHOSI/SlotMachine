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

1. Use your mobile to connect the (website)[192.168.43.65:8080], and you can see some number showing in this website.
This website is catching your mobile **gyroscope sensor** and **accelerometer sensor** and get your action. When you shake your mobile "enough", It will inovke Node.js server.

2. Node.js server will inovke python script, showing some random number (ranged from 0 to 9, including 0 and 9) on seven segement separately. There are three seven segements.

3. When these three seven segements shows same number (ex. 777), it will play music from raspberry pi. And you have to use 3.5mm earphone to listen music. (In this project, I use "Taeyeon - I(Inst.)" music. This song is really great ^__^/

4.If you don't want to play this game, just click "Game Over" button, and it will stop showing numbers on seven segements!

## How It Works

Ok, let's get into the main topic!
I suppose you have just set up a raspberry pi and can connect your rpi with ssh and vnc, so I will introduce after that steps.

### Use Conda
Conda is an open source package management system and environment management system for installing multiple versions of software packages and their dependencies and switching easily between them. (URL)[https://anaconda.org/anaconda/conda]

In this project, we use (berryconda)[https://github.com/jjhelmus/berryconda], is based on conda.


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

### Blink Seven Segemnet
Before doing this step, you have to know (Seven-segement Display)[https://en.wikipedia.org/wiki/Seven-segment_display] and connect correct dupont lines to correct ports.

In this part, I use ```python``` language and ```wiringpi``` python language to blink seven-segement.
