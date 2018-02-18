import time as t
import datetime
import sys
import subprocess
import csv
import config as cfg
import netatmo
import getTempValue

#location where the csv log file is stored
logLocation = cfg.logLocation

#location where temperature scrpt is stored
tempScriptLocation = cfg.tempScriptLocation

#-----------------------------------
# custom csv dialect for european excel compatibility
#-----------------------------------
class excel_semicolon(csv.excel):
    delimiter = ';'

#-----------------------------------
# replace all dots to commas in a string or in each string in a list
#-----------------------------------
def convertToStringWithComma(content):
    if isinstance(content, list):
        result = []
        for x in content:
            result.append(x.replace(".", ","))
        return result
    else:
        return content.replace(".", ",")

#-----------------------------------
# get indoor sensor values
#-----------------------------------
def getCurrentTime():
    ts = t.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    return date, time

#-----------------------------------
# get indoor sensor values
#-----------------------------------
def getIndoorValues():
    #get indoor temp and humidity
    currentTemp = getTempValue.getValues()
    currentTemp = currentTemp.split(",")
    currentTemp = convertToStringWithComma(currentTemp)
    return currentTemp

#-----------------------------------
# get outdoor values
#-----------------------------------
def getOutdoorValues():
    #get outdoor data
    outdoorData = netatmo.getValues()
    outdoorData = outdoorData.split(",")
    outdoorData = convertToStringWithComma(outdoorData)
    return outdoorData

#csv logging
fields = []
fields.extend(getCurrentTime())
fields.extend(getIndoorValues())
fields.extend(getOutdoorValues())

	 
with open(logLocation, 'a') as f:
    writer = csv.writer(f, dialect=excel_semicolon)
    writer.writerow(fields)
print("wrote csv file successfully: " + str(fields))
