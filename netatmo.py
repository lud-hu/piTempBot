from netatmo_client.client import NetatmoClient
import config as cfg
import json

def getValues():
	scopes = ('read_station', 'read_thermostat', 'write_thermostat', 'read_camera')

	client = NetatmoClient(cfg.credentials["client_id"], cfg.credentials["client_secret"])

	client.request_token_with_client_credentials(cfg.credentials["username"], cfg.credentials["password"], *scopes)

	# currently just receiving the JSON, not doing anything with it
	result = client.public.get_public_data(cfg.region["lat_ne"], cfg.region["lon_ne"], cfg.region["lat_sw"], cfg.region["lon_sw"])
	print json.dumps(result)

	temperatures = []
	humidities = []
	pressures = []
	rains_live = []
	rains_60min = []
	rains_24h = []

	#result is list  
	for station in result:
	  #station is a dict
	  
	  for modulemac, modulename in station['module_types'].items():
		#here are all modules of this station listed
		  #NAModule1: Outdoor module (temp, humidity)
		  #NAModule3: Rain Gauge
		
		#temp, humidity and pressure
		if (modulename == "NAModule1"):
		  #grab temp an humidity data for this station and append it to the list
		  try:
			temperatures.append(station['measures'][modulemac]['res'].values()[0][0])
			humidities.append(station['measures'][modulemac]['res'].values()[0][1])
		  except:
			#if there is no data for this station, put blanks in
			temperatures.append(None)
			humidities.append(None)
			#print("temp or humidity data missing in the feed for: " + str(modulemac))
			
		  #grab pressure data
		  #"_id" is used instead of the modulemac
		  try:
			pressures.append(station['measures'][station['_id']]['res'].values()[0][0])
		  except:
			pressures.append(None)
			#print("pressure data missing in the feed for: " + str(modulemac))
		
		#rain
		elif (modulename == "NAModule3"):
		  #grab rain data
		  try:
			rains_live.append(station['measures'][modulemac]['rain_live'])
		  except:
			rains_live.append(None)
			
		  try:
			rains_60min.append(station['measures'][modulemac]['rain_60min'])
		  except:
			rains_60min.append(None)
		  
		  try:
			rains_24h.append(station['measures'][modulemac]['rain_24h'])
		  except:
			rains_24h.append(None)

	try:
	  meanTemp = sum(map(float, filter(None, temperatures)))/len(filter(None, temperatures))
	except:
	  meanTemp = 0

	try:
	  meanHumidity = sum(filter(None, humidities))/len(filter(None, humidities))
	except:
	  meanHumidity = 0
	  
	try:
	  meanPressure = sum(filter(None, pressures))/len(filter(None, pressures))
	except:
	  meanPressure = 0
	  
	try:
	  meanRainLive = sum(filter(None, rains_live))/len(filter(None, rains_live))
	except:
	  meanRainLive = 0

	try:
	  #calc seperately to avoid rounding issues
	  mysum = sum(rains_24h)
	  mylen = len(rains_24h)
	  meanRain24h = mysum/mylen
	except:
	  meanRain24h = 0

	return ('{0:0.1f},{1:0.1f},{2:0.1f},{3:0.1f},{4:0.1f}'
	  .format(meanTemp, meanHumidity, meanPressure, meanRainLive, meanRain24h))