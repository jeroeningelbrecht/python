import requests
from os import environ

names = ['Taike', 'Hayo', 'Pallavi', 'Lea', 'Bernard']

for name in names:
    response = requests.get('https://love-calculator.p.rapidapi.com/getPercentage',
                        params={'fname': 'Jeroen', 'sname': name},
                        headers={
                            "X-RapidAPI-Host": "love-calculator.p.rapidapi.com",
                            "X-RapidAPI-Key": environ.get("API_KEY")
                        }
                        )
    if response.status_code == 200:
        print('ok', response.text)
    else:
        print('nok', response.status_code)
