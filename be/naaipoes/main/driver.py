import requests

response = requests.get('https://love-calculator.p.rapidapi.com/getPercentage',
                            params={'fname': 'Jeroen', 'sname': 'Taike'},
                            headers={
                                "X-RapidAPI-Host": "love-calculator.p.rapidapi.com",
                                "X-RapidAPI-Key": ""
                            }
                        )

print(response)
