# ohbot for python (windows version)

<a href="http://whoosh.co.uk/ohbothelp/images/eyes.gif" target="_blank"><img src="http://whoosh.co.uk/ohbothelp/images/eyes.gif" border="0" width = "30%"/></a>


Background
These instructions allow you to program your Windows Ohbot or Raspberry Pi Ohbot using Python on a Windows PC.

More information about Ohbot can be found on [ohbot.co.uk](http://www.ohbot.co.uk)


Install latest version of Python from here.

[python.org](https://www.python.org/downloads/release/python-364/)

I chose version 3.6 Windows x86-64 executable installer.

During the Install make sure that the pip option is selected

<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/image1-22.png" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/image1-22.png" border="0" width = "80%"/></a>

Dependencies
----------

If you don't have pip3 (the python 3 package manager) installed, open terminal and execute the following:

```
sudo apt-get install python3-pip
```

Ohbot requires the following libraries be installed:



| Library    | Use         | Terminal command to install  |Link |
| ---------- |-------------| -----------------------------|-----|
| ohbotWin   | Interface with Ohbot          | ```pip install ohbotWin```  |[ohbot](https://github.com/ohbot/ohbotWin-python/) |
| serial    | Communicate with serial port| ```pip install pyserial```  |[pyserial](https://github.com/pyserial/pyserial/) |
| lxml    | Import settings file          | ```pip install lxml```  |[lxml](https://github.com/lxml/lxml) |
| comtypes    | Required for serial communication      | ```pip install comtypes```  |[lxml](https://github.com/lxml/lxml) |
| threading    | Run multiple threads     | Included in Python 3  |- |
| os    | Send commands to festival       | Included in Python 3  |- |
| time    | Run timers                    | Included in Python 3  |- |


Ohbot is tested with Python 3 running on a Raspberry Pi 3 Model B. 

To upgrade to the latest version of the library run the following in the console:
```pip3 install ohbotWin -- upgrade```



Ohbot library files (these will be installed with the `pip3 install ohbot` command above):

| File    | Use         |
| ---------- |------------|
| ohbot.py   | Ohbot package |
| MotorDefinionsv21.omd    | Motor settings file |

_Note: The text to speech module Festival will generate an audio file, ‘ohbotspeech.wav’ and a text file ‘phonemes.txt’ inside your working folder._

---

Hardware
-----

Required:


* Raspberry Pi
* Ohbot
* USB Y Cable
* USB Power Socket Adaptor
* Speakers/headphones with 3.5mm headphone jack


Setup:



Plug the middle of USB Y cable into Raspberry Pi and the other large USB plug into the power adaptor. Then plug the mini USB into Ohbot. Finally plug your speakers into your Raspberry Pi. 

---

Writing Programs
--------

1. Open Python 3 (IDLE)
2. Click File → New File
3. Save your file as a python script (.py) in a new folder called Ohbot somewhere on your Pi.

Import
-------

Make sure you import ohbot at the start of your program. 
```python
from ohbot import ohbot
```

---

Functions
-------

ohbot.init(portName)
----------

Called internally using portName = "ttyACM" but if your port is different you can call it and override this port name. It returns True if the port is found and opened successfully, otherwise it returns false. 

ohbot.move(m, pos, speed=3)
----------


| Name| Range| Description | Defualt |
| --- |------|-------------|---------|
| m   | 0-6 (int)  | Motor Number| - |
| pos | 0-10 (int)  | Desired Postition| - |
| speed | 0-10 (int) | Motor Speed| 3 |


For Example:
```python
ohbot.move(1,7)
```
or
```python
ohbot.move(2,3,1) 
```
or you can use a constant from the library to specify the motor:
```python
ohbot.move(ohbot.EYETURN,3,1) 
```
Motor index reference:

| m | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----| --- | --- |  --- |  --- |  --- |  --- |  --- |
| constant | HEADNOD | HEADTURN | EYETURN | LIDBLINK | TOPLIP | BOTTOMLIP | EYETILT | 
  

ohbot.say(text, untilDone=True, lipSync=True, hdmiAudio=False, soundDelay=0)
----------

| Name| Range| Description | Defualt |
| --- |------|-------------|---------|
| text   | 'A string with no punctuation'  | Words to say| - |
| untilDone | bool  | Return when finished speaking| True |
| lipSync | bool | Move lips in time with speech| True |
| hdmiAudio | bool | Fixes missing start of phrase when HDMI audio output is being used| False |
| soundDelay | float | Set to positive if lip movement is lagging behind sound and negative if sound is lagging behind lip movement| 0 |



For Example:
```python
ohbot.say('Hello I am Ohbot')

ohbot.say('Goodbye',False,False)

ohbot.say('Goodbye',False,False,True)

ohbot.say('Goodbye',soundDelay = 0.3)
```
---

ohbot.wait(seconds)
----------

Seconds - float or int required wait time. ohbot.wait(1.5)

| Name| Range| Description  |
| --- |------|-------------|
| seconds   | float or int  | Length of wait in seconds|



For Example:
```python
ohbot.wait(2)

ohbot.wait(0.5)
```

*Note: It is important to use ohbot.wait() commands between motor sequential commands for the same motor.*

For Example:
```python
ohbot.move(1,7,2)

ohbot.wait(2)

ohbot.move(1,4,2)
```
---

ohbot.eyeColour(r, g, b, swapRandG=False)
----------

Set the colour of Ohbot’s eyes. 

| Name| Range| Description  | Default |
| ---      |------|-------------| ------- |
| r        | 0-10 (int)  | Red| - |
| g        | 0-10 (int)  | Green| - |
| b        | 0-10 (int)  | Blue| - |
| swapRandG| bool | swap r and g value for some older Ohbots | False |


For Example:
```python
ohbot.eyeColour(2,3,8)
```
or 
```python
ohbot.eyeColour(2,3,8,True)
```

---

ohbot.reset()
----------

Resets Ohbot’s motors back to rest positions and turns off Ohbot’s eyes. Useful to start programs with this. You may need an ohbot.wait() after this to give time for the motors to move. 

For Example:
```python
ohbot.reset()
ohbot.move(1,7,2)
ohbot.wait(1)
ohbot.move(1,1)
...
```
---

ohbot.close()
----------

Call to detach all Ohbot’s motors which stops them using power, you can call ohbot.attach(m) or ohbot.detach(m) for individual motors.

For Example:
```python
ohbot.move(1,7,2)
ohbot.wait(1)
ohbot.move(1,1)

ohbot.close()
```
---

ohbot.readSensor(sensorNumber)
----------

Seconds - float or int required wait time. ohbot.wait(1.5)

| Name| Range| Description  |
| --- |------|-------------|
| sensorNumber   | 0-6 (int) | the pin the sensor is connected to |

returns the value as a float 0 - 10.

For Example:
```python
reading = ohbot.readSensor(3)

ohbot.move(ohbot.HEADTURN, reading)

```

**_Press fn + f5 to run your program_**



