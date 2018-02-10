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
*/5 * * * * /usr/bin/python /home/pi/scripts/csvTempLogger.py
```

### config file

You can set the most important settings in the "config.py" file. If you locate your project on /home/pi/scripts/ you just have to adapt the Telegram Token Key and the Telegram User IDs (white list).

### Telegram Bot

The Telegram bot logic is located in "telegramBot.py". The commands for telling the bot what to do are defined here. A detailed instruction of how to set up a Telegram bot on a Raspberry Pi is located here: https://circuitdigest.com/microcontroller-projects/raspberry-pi-telegram-bot

In order to make the bot startup at a reboot of your Pi you have to add this line to the crontab list of your Pi:
```
@reboot /home/pi/scripts/startTelegramBot.py
```

You can set a list of Telegram user IDs in the "config.py" file that are allowed to talk to the Telegram bot. Otherwise it would be publicly available for everyone.
