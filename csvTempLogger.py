import time
import datetime
import sys
import subprocess
import csv
import config as cfg
import netatmo

#location where the csv log file is stored
logLocation = cfg.logLocation

#location where temperature scrpt is stored
tempScriptLocation = cfg.tempScriptLocation

class excel_semicolon(csv.excel):
    delimiter = ';'

def convertToStringWithComma(content):
    return str(float(content)).replace(".", ",")

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

#get indoor temp and humidity
currentTemp = subprocess.check_output([sys.executable, tempScriptLocation, "22", "4"])

#parse temp and humidity
temp,humidity = currentTemp.split(",")

#get outdoor data
outdoorData = netatmo.getValues()
outdoorTemp,outdoorHumidity,pressure,rain,rain24h = outdoorData.split(",")

#csv logging
fields=[
	date,
	time,
	convertToStringWithComma(temp),
	convertToStringWithComma(humidity),
	convertToStringWithComma(outdoorTemp),
	convertToStringWithComma(outdoorHumidity),
	convertToStringWithComma(pressure),
	convertToStringWithComma(rain),
	convertToStringWithComma(rain24h)]
	
with open(logLocation, 'a') as f:
    writer = csv.writer(f, dialect=excel_semicolon)
    writer.writerow(fields)
print("wrote csv file successfully: " + date + ";" + time + ";" + temp + ";" + humidity)
