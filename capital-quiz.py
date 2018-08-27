import random
import urllib.request
import json

url = 'https://restcountries.eu/rest/v2/all'
jsondata = json.loads(urllib.request.urlopen(url).read())


def quiz(countries):
    points = 0
    while True:
        first = True
        yourCountry = random.choice(countries)
        randCountries = [yourCountry['capital'],
                         random.choice(countries)['capital'],
                         random.choice(countries)['capital']]
        randCountries.sort()

        print(f"What's the capital in {yourCountry['name']}? Type HELP to get 3 options. You'll get 1 point instead of 5. The country is located in {yourCountry['subregion']} width a population of {format(yourCountry['population'], ',')}, and an area of {format(yourCountry['area'], ',')} km². They use {yourCountry['currencies'][0]['symbol']} {yourCountry['currencies'][0]['name']} to pay with, and speak {' and '.join([x['name'] for x in yourCountry['languages']])}.")

        while True:
            answer = input().lower().strip()
            if answer == yourCountry['capital'].lower().strip():
                points += 5 if first else 1
                break
            elif answer in ['help', 'h', 'options']:
                print('The answer will be one of these options three:',
                      ', '.join(randCountries))
                first = False
            elif answer in ['q', 'quit', 'e', 'exit']:
                return
            else:
                print("That's not it, it was", yourCountry['capital'])
                break

        againInput = input(f'You have {points} points. Want to go again? ')
        print('')
        if not againInput.lower() in ['yes', 'y']:
            return

    return


quiz(jsondata)
