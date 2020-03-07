The main [Picoh Python package](https://github.com/ohbot/picoh-python) now supports Windows so please use that package from now on. All future development will be on [Picoh Python](https://github.com/ohbot/picoh-python). 


# Ohbot for Python (Windows Version)

<a href="http://whoosh.co.uk/ohbothelp/images/eyes.gif" target="_blank"><img src="http://whoosh.co.uk/ohbothelp/images/eyes.gif" border="0" width = "30%"/></a>


Background
-----

These instructions allow you to program your Ohbot using Python on a Windows PC.

More information about Ohbot can be found on [ohbot.co.uk.](http://www.ohbot.co.uk)


Setup
--------

Download a Python installer from [here.] (https://www.python.org/downloads/release/python-364/) On Windows the Ohbot library currently only works with Python versions up to 3.6.

We chose version 3.6 Windows x86-64 executable installer.

<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/screenshot4.jpg" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/screenshot4.jpg" border="0" width = "65%"/></a>

Tick the option to Add Python 3.6 to PATH then click on Install Now.

Once install is complete type “Command” into the Windows search box.  Right click on <b>Command Prompt </b> and select <b>Run as administrator.</b>

<br>

<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/image2-24.tif" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/image2-24.tif" border="0" width = "35%"/></a>

<br>

This will open a command prompt window. 

Type the folloing:

``pip install ohbotWin``

To upgrade to the latest version of the library run the following in the console:
```sudo pip3 install ohbotWin --upgrade```

Installing more voices (optional)
--------

The Ohbot Python library will default to using SAPI voices which are the voices that are available through Windows Control Panel:Speech Propeties.

You can change this to espeak or espeak-ng by calling ohbot.setSynthesiser (“espeak”) or ohbot.setSynthesizer (“espeak-ng”).

Install the espeak library from [here.](http://espeak.sourceforge.net/download.html)


Install espeak and then copy the espeak.exe file in Windows File Explorer from 

C:\Program Files (x86)\eSpeak\command_line

To 

C:\Program Files\Python36

To use the espeak-ng library install it from [here.](https://github.com/espeak-ng/espeak-ng#binaries)

Install espeak-ng and then copy the espeak-ng.exe and espeak-ng.dll files in Windows File Explorer from 

C:\Program Files\eSpeak NG

To 

C:\Program Files\Python36

That should be it for the setup.

Dependencies
----------

The ``pip install ohbotWin`` command will install the following libraries:


| Library    | Use         | Terminal command to install  |Link |
| ---------- |-------------| -----------------------------|-----|
| ohbotWin   | Interface with Ohbot          | ```pip install ohbotWin```  |[ohbot](https://github.com/ohbot/ohbotWin-python/) 
| serial    | Communicate with serial port| ```pip install pyserial```  |[pyserial](https://github.com/pyserial/pyserial/) |
| lxml    | Import settings file          | ```pip install lxml```  |[lxml](https://github.com/lxml/lxml) |
| comtypes    | Required for serial communication      | ```pip install comtypes```  | [comtypes](https://github.com/enthought/comtypes) |


To upgrade to the latest version of the library run the following in the console:
```pip install ohbotWin -- upgrade```



Ohbot library files (these will be installed with the `pip install ohbotWin` command above):

| File    | Use         |
| ---------- |------------|
| ohbot.py   | Ohbot package |
| MotorDefinionsv21.omd    | Motor settings file |

_Note: The text to speech module will generate an audio file, ‘ohbotspeech.wav’ and a text file ‘phonemes.txt’ inside your working folder._

---

Hardware
-----

Required:


* PC Running Windows.
* Ohbot
* USB Y Cable
* A 5 volt 1 amp USB power supply (for Ohbot)
* Speakers/headphones.


Setup:


Plug the middle of USB Y cable into the PC and the other large USB plug into the power adaptor. Then plug the mini USB into Ohbot.

---

Starting Python Programs
--------

Go to the Windows Menu and run IDLE from the Python folder:


<a href="https://github.com/ohbot/ohbotWin-python/blob/master/images/image3-26.tif" target="_blank"><img src="https://github.com/ohbot/ohbotWin-python/blob/master/images/image3-26.tif" border="0" width = "35%"/></a>


Select <b>New</b> from the <b>File menu.</b>

Go to the [hellworldohbot](https://github.com/ohbot/ohbotWin-python/blob/master/examples/helloworldohbot.py) example on Github, copy the code and paste it into the new Python window.

Select <b>Run Module</b> from the <b>Run</b> menu.

Ohbot should speak and move.

More example programs can be found [here.](https://github.com/ohbot/ohbotWin-python/tree/master/examples)


Functions
-------

ohbot.init(portName)
----------

Called internally looking for a port with name containing "USB Serial Device" but if your port is different you can call it and override this port name. It returns True if the port is found and opened successfully, otherwise it returns false. This is likely with a versions of Windows in languages other than English. 

ohbot.move(m, pos, speed=3)
----------


| Name| Range| Description | Default |
| --- |------|-------------|---------|
| m   | 0-6 (int)  | Motor Number| - |
| pos | 0-10 (int)  | Desired Position| - |
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

| Name| Range| Description | Default |
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
ohbot.setSynthesizer(synth)
----------

| synth | Full Name |
|----|-------- |
| “sapi” | SAPI speech |
| “espeak-ng” | espeak-ng speech |
| “espeak” | espeak speech |


For Example:
```python
ohbot.setSynthesizer("espeak")
```

Note that the SAPI speech uses the voices available in Control Panel:Text to Speech.   It can’t use Cortana voices.


ohbot.setVoice(voice)
------

Use ohbot.setVoice() to set the voice depending on the synthesizer:

<b>Using SAPI</b>

Use any of the following arguments:

| Name| Description|
| --- |------|
| -a0 to -a100   | amplitude |
| -r-10 to r10   | rate |
| -v any part of the name of a SAPI voice (eg. -vHazel or -vZira) | voice |

For Example:
```python
ohbot.setVoice("-a82 -r12 -vzira")

```

<b>Using ESPEAK</b>

http://espeak.sourceforge.net/commands.html<br>

| Name| Description|
| --- |------|
| -v followed by a letter code|look in program files\espeak\espeak-data\voices to see what's available|
|   +m1 to m7   | male voices |
|   +f1 to f4   | remale voices |
|   +croak or whisper   | tone |
|   -a0 to a200   | amplitude |
|   -s80 to s500   | speed |
|   -p0 to p99   | pitch |


Examples:<br>

| Command | Result |
| ------ | ------- |
| ``ohbot.setVoice("-ven+croak")`` | English croaky voice |
| ``ohbot.setVoice("-vzh+m2 -s26")`` | Chinese male voice, Fast |
| ``ohbot.setVoice("-vfr+f1 -p99 -s180")`` | French female whisper voice, medium speed and high pitched |

More examples can be found in our [voices example program.](https://github.com/ohbot/ohbotWin-python/blob/master/examples/voices.py)

<b>Using ESPEAK-NG</b>

Supports some of the ESPEAK parameters but some are missing.



