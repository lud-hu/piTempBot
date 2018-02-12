# piTempBot
This is a little collection of python scripts for running a Telegram bot on a Raspberry Pi which records temperature, humidity etc.
<!--- with a little web interface--->

## Features

*  records Temperature and Humidity (more to come)
*  saves it into csv file
*  running a Telegram bot which can tell you the current measurements and send you the log data
<!---*  has a little web interface to show you the statisics (currently in progress)--->

## little Documentation

### Temperature & Humidity Logging

The recording of the data is based on the DHT22 temperature and humidity sensor which is connected to the GPIO port of the Raspberry Pi. The Adafruit library is executing the measurement, my little python script "csvTempLogger.py" pulls the data and saves it to the csv log file.
You can find a (german) instruction on how to set up the DHT22 sensor on the Pi here: https://tutorials-raspberrypi.de/raspberry-pi-luftfeuchtigkeit-temperatur-messen-dht11-dht22/

In order to have some log data recorded every 5 minutes you have to put the python script on the crontab list of your Pi:
```
*/5 * * * * /usr/bin/python /home/pi/piTempBot/csvTempLogger.py
```

### config file

You can set the most important settings with the file liste below. If you locate your project on /home/pi/piTempBot/ you just have to adapt the Telegram Token Key and the Telegram User IDs (white list).

Save this in the projects root folder as "config.py":
```
###################################################################
#HARDWARE SETTINGS

#version of used sensor
hardwareVersion = '22' # '22' for DHT22, '11' for DHT11

#used GPIO Port on Raspberry Pi
gpioPort = '4'

###################################################################
#FILE LOCATION SETTINGS

#location where the sensor readout script is located
adafruitScript = '/Adafruit_Python_DHT/examples/AdafruitDHT.py'

#location where temperature script is stored
tempScriptLocation = '/home/pi/piTempBot/getTempValue.py'


###################################################################
#CSV FILE SETTINGS

#location where the csv log file is stored
logLocation = '/home/pi/temperaturlog.csv'

#colum titles of the log file
columnTitles = ['Tag','Zeit','Temperatur','Luftfeuchtigkeit'] #day, time, temperature, humidity

###################################################################
#TELEGRAM BOT SETTINGS

#Telegram Bot Token Key
botTokenKey = 'xxx'

#Telegram User White List (other users can not use the bot)
allowedUserIds = [xxx,xxx] # user1, user2

###################################################################
#NETATMO SETTINGS

#login credentials for netatmo
credentials = {
	"password":"myNetatmoDevPasswor",
	"username":"my.mail@mail.com",
	"client_id":"1234567890",
	"client_secret":"1234567890"
}

#region to scan for netatmo weather stations
#look here for more information: https://dev.netatmo.com/en-US/resources/technical/reference/weatherapi/getpublicdata
region = {
	"lat_ne" : 50.0,
	"lat_sw" : 50.0,
	"lon_ne" : 10.0,
	"lon_sw" : 10.0,
}
```

### Telegram Bot

The Telegram bot logic is located in "telegramBot.py". The commands for telling the bot what to do are defined here. A detailed instruction of how to set up a Telegram bot on a Raspberry Pi is located here: https://circuitdigest.com/microcontroller-projects/raspberry-pi-telegram-bot

In order to make the bot startup at a reboot of your Pi you have to add this line to the crontab list of your Pi:
```
@reboot /home/pi/piTempBot/startTelegramBot.py
```

You can set a list of Telegram user IDs in the "config.py" file that are allowed to talk to the Telegram bot. Otherwise it would be publicly available for everyone.
