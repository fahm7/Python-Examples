import math
import requests

print (math.factorial(10))
print(math.fsum([13.0,34.0,56.8]))

#$ pip3 install pytz
#Installing collected packages: pytz
#Successfully installed pytz-2018.3
#$ pip3 install pytz
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
#print(response.text)
print(type(response.text))


