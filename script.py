
import math as m
import sys
from os import rename

import requests
from pandas import to_datetime

print (sys.version)
print(sys.executable)


def greet(whomm_to_greet):
    
    greeting = 'Hello, {}'.format(whomm_to_greet)
    return greeting


r = requests.get('http://www.google.com')
print(r.status_code)
print(greet('world'))
print(greet('Corey'))

print(to_datetime('2022-03-08'))
