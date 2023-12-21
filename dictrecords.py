# This is a function that make a text file from dictionary record of unicorns txt file

def dicrecords():
    import json

    fileunicorns = open("unicorns2021.txt", 'rt')
    filedictunicorns = open("unicorndict.txt", 'wt')
    dicline = {
        "company": "",
        "valuation": "",
        "datajoint": "",
        "country": "",
        "city": "",
        "industry": "",
        "investors": list([])
    }
    dicttext = ''
    for xline in fileunicorns:
        company = ''
        companybool = False

        valuation = ''
        valuationbool = False

        datejoint = ''
        datebool = False

        country = ''
        countrybool = False

        city = ''
        citybool = False

        industry = ''
        industrybool = False

        investors = list([])
        xinvestor = ''
        investbool = False

        for xchar in xline:
            if (xchar == ';'):
                if companybool:
                    if valuationbool:
                        if datebool:
                            if countrybool:
                                if citybool:
                                    if industrybool:
                                        print('****ERROR***')
                                    else:
                                        industrybool = True
                                else:
                                    citybool = True
                            else:
                                countrybool = True
                        else:
                            datebool = True
                    else:
                        valuationbool = True
                else:
                    companybool = True
            elif companybool:
                if valuationbool:
                    if datebool:
                        if countrybool:
                            if citybool:
                                if industrybool:
                                    if xchar == ',' or xchar == '\n':
                                        investors.append(xinvestor)
                                        xinvestor = ''
                                    else:
                                        xinvestor += xchar
                                else:
                                    industry += xchar
                            else:
                                city += xchar
                        else:
                            country += xchar
                    else:
                        datejoint += xchar
                else:
                    valuation += xchar
            else:
                company += xchar

        dicline.update({
            "company": company,
            "valuation": valuation,
            "datajoint": datejoint,
            "country": country,
            "city": city,
            "industry": industry,
            "investors": investors})
        dicttext += json.dumps(dicline) + '\n'

    filedictunicorns.write(dicttext)
    fileunicorns.close()
    filedictunicorns.close()


    return 0