while True:
    user_city = input(' Please enter the city name: ')

    linecounter = 0
    total_valuation = 0

    with open('unicorns2021.txt', 'r') as f:
        for line in f:
            data = line.strip().split(';')

        if data[4 == user_city]:
            valuation = float(data[1][1:])
            total_valuation += valuation

            linecounter += 1

    if linecounter > 0:
        average_valuation = total_valuation / linecounter
        print(f'the average valuation of companies from {user_city} is ${average_valuation:.2f} billion')
    else:
        print(f'no companies found from {user_city} in the data set ')
