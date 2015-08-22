# WeatherPi
A mini weather station with Raspberry Pi

A project for a Weather Station using Raspberry Pi that will display temperature, humidity and time using DHT22 and Adafruit 0.56 4-Digit 7-Segment Display.

####Equipment:
-Raspberry Pi

-DHT22 Sensor (although others such as DHT11 or AM2302 may be valid changing a little bit the code)

-Adafruit 0.56 4-Digit 7-Segment Display.

####Setup:

* Install Adafruit DHT library to controll the sensor:
  `sudo apt-get update`

  `sudo apt-get install build-essential python-dev python-openssl`

  `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`

  `cd Adafruit_Python_DHT`

  `sudo python setup.py install`

* Wire the sensor as seen [here] (https://learn.adafruit.com/downloads/pdf/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.pdf#__WKANCHOR_6). 
You can test the sensor using the temperature.py script that is inside the test folder.

* Configure Raspberry Pi for IC2: Perfectly explained [here] (https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi/configuring-your-pi-for-i2c).

* Wire the display as seen [here] (https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi/hooking-everything-up). Test the display using the test.py script.

* For the button, you need to install the RPi.GPIO library (make sure it's the latest release):

  `wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.11.tar.gz` 

  `tar -xvf RPi.GPIO-0.5.11.tar.gz`

  `cd RPi.GPIO-0.5.11`

  `sudo python setup.py install`

####Run it
`cd src`
  
`sudo ./run.py [T|H|C]` Write T if you want to start with Temperature mode, H for humidity mode and C for clock.

Push the button to switch between states.
