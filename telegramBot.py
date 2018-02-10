import time
import sys
import subprocess
from subprocess import call
import csv
import telepot
from telepot.loop import MessageLoop
import config as cfg

#----------------------------------
#VARIABLES
#----------------------------------

#location where the sensor readout script is located
adafruitScript = cfg.adafruitScript

#location where the temperature log is located
temperatureLog = cfg.logLocation

#colum titles of the log file
columnTitles = cfg.columnTitles

#----------------------------------
# custom csv dialect
#----------------------------------
class excel_semicolon(csv.excel):
    delimiter = ';'

#-----------------------------------
# MESSAGE: stats response
#-----------------------------------
def stats(chat_id):
    
    lines_count = sum(1 for line in open(temperatureLog))-1
    telegram_bot.sendMessage(chat_id, str("Aktuell habe ich schon %s Datensaetze gesammelt. " % str(lines_count)) + u'\U0001f4CA')

#-----------------------------------
# MESSAGE: send_log response
#-----------------------------------
def sendLog(chat_id):
    
    telegram_bot.sendMessage(chat_id, str("Hier ist die Temperaturaufzeichnung! Einfach in Excel oeffnen."))
    telegram_bot.sendDocument(chat_id, document=open(temperatureLog))

#-----------------------------------
# MESSAGE: clear_log response
#-----------------------------------
def clearLog(chat_id):
    
    #clear file
    open(temperatureLog, 'w').close()
    
    #add header line again
    with open(temperatureLog, 'a') as f:
        writer = csv.writer(f, dialect=excel_semicolon)
        writer.writerow(columnTitles)
    telegram_bot.sendMessage(chat_id, str("Erledigt! Der Temperatur-Log wurde geleert. ") + u'\U0001f44d')

#-----------------------------------
# main function for message handling
#-----------------------------------
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print("Received " + str(command) + " from " + str(chat_id))

    if (chat_id not in cfg.allowedUserIds):
        telegram_bot.sendMessage(chat_id, str("Neee, fuer dich tu ich garnix!"))
        print("Feind abgewehrt!")
        return

    if command.find("Hi") != -1 or command.find("hi") != -1 or command.find("Hallo") != -1:
        telegram_bot.sendMessage(chat_id, str("Hi, wie geht's`? ") + u'\U0001F60A')
    elif command == '/temp':
        telegram_bot.sendMessage(chat_id, subprocess.check_output([sys.executable, adafruitScript, "22", "4"]))
    elif command == '/stats':
        stats(chat_id)
    elif command.find("warm") != -1:
        telegram_bot.sendMessage(chat_id, subprocess.check_output([sys.executable, adafruitScript, "22", "4"]))
    elif command == '/send_log':
        sendLog(chat_id)
    elif command == '/clear_log':
        clearLog(chat_id)     
	elif command == '/shutdown':
        telegram_bot.sendMessage(chat_id, str("Alles, klar! Mach's gut! ") + u'\U0001F60A')
		call(["sudo shutdown now"])
    else:
        telegram_bot.sendMessage(chat_id, str("Sorry, das habe ich nicht verstanden!"))

#---------------------------------
#---------------------------------
telegram_bot = telepot.Bot(cfg.botTokenKey)
print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running'

while 1:
    time.sleep(10)
