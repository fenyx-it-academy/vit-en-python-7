# This function is going to calculate average valuation of a city

def average_valuation(cityname):
    import json

    unidict = open("unicorndict.txt", 'rt')

    sumofvaluations = 0
    counter = 0
    for x in unidict:
        xline = json.loads(x)
        if xline["city"].lower() == cityname.lower():
            sumofvaluations += int(xline["valuation"][1:])
            counter += 1
        else:
            continue

    average = float(sumofvaluations) / counter

    return average
