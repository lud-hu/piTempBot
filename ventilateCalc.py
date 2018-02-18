import math

# a lot of weird constants for the calculations:
constant1 = 6.112
constant2 = 17.62
constant3 = 243.12
constant4 = 461.5
constant5 = 273.15


def convertToFloat(string):
    return float(string.replace(",","."))

#-----------------------------------
# calculates the absolute humidities of in- and outdoor air
# returns the delta between (abs humidity indoor - abs humidity outdoor)
#
# if deltaAbsHum is > 0 it makes sense to ventilate the room (indoor humidity would decrease)
# if deltaAbsHum is < 0 you would increase the indoor humidity after ventilating
#-----------------------------------
def calc(innerTemp, innerHum, outerTemp, outerHum):

    innerTemp = convertToFloat(innerTemp)
    innerHum = convertToFloat(innerHum)
    outerTemp = convertToFloat(outerTemp)
    outerHum = convertToFloat(outerHum)

    #calc saturated vapor pressure
    #https://en.wikipedia.org/wiki/Vapour_pressure_of_water
    innerSDD = constant1 * math.exp((constant2*innerTemp)/(constant3+innerTemp))
    outerSDD = constant1 * math.exp((constant2*outerTemp)/(constant3+outerTemp))

    #calc vapor pressure
    innerDD =  innerHum/100 * innerSDD
    outerDD =  outerHum/100 * outerSDD

    #calc absolute Humidity
    innerAbsHum = (innerDD/(constant4*(constant5+innerTemp)))*100000
    outerAbsHum = (outerDD/(constant4*(constant5+outerTemp)))*100000

    return round(innerAbsHum - outerAbsHum, 3)