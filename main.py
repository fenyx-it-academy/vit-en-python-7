# vit-en-python-7

import dictrecords
import city_average_valuation

print("***For average of the valuations of a city, You should enter the name of a city from the Unicorn***")
a = dictrecords.dicrecords()
try:
    if a == 0:
        city = input("Please enter a city name: ")
        average = city_average_valuation.average_valuation(city)
    else:
        print("***ERROR***")

    msg = """The average of the valuations of the city "{}" is {} billion dollars"""

    print(msg.format(city, round(average, 2)))
except:
    print("<<<***You entered a wrong city***>>>")


