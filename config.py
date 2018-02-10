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
