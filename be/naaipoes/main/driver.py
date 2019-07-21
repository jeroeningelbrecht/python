import requests

response = requests.get('https://love-calculator.p.rapidapi.com/getPercentage',
                            params={'fname': 'Jeroen', 'sname': 'Taike'},
                            headers={
                                "X-RapidAPI-Host": "love-calculator.p.rapidapi.com",
                                "X-RapidAPI-Key": "372b5df5a5msh57621ecd1ee8240p15dfcajsnf976b3cd425e"
                            }
                        )

print(response)
