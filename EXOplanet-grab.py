###PYTHON 3.9##
##SESSION MODULES##
import requests
import json
from tabulate import tabulate

class exoPlanetCall:
    def __init__(self, address):
        self.address = address
 
   
    def call(self):
        req = requests.get("{}".format(self.address))
        convertedReq = req.json()
        return convertedReq
    
class queryObj:
    def __init__(self, radius, mass, year):
         self.query = "pl_rade {} 2+and+pl_masse {} 1+and+pl_orbper {} 365&format=json".format(radius, mass, year)
         
    def makeQuery(self):
        address = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_masse,ra,dec+from+ps+where+{}".format(self.query)
        return address
        

print("Welcome to the Earth-like object finder! Using the confirmed Exoplanet archive!")
radius = input("find planets larger diameter than Earth? '>' for larger, '<' for smaller: ")
mass = input("more or less mass than Earth? '>' for greater, '<' for lesser: ")
year = input("how about the planets year length, compared to Earth?'>' for longer, '<' for shorter: ")

obj = queryObj(radius, mass, year)
address = obj.makeQuery()
session = exoPlanetCall(address)
print(tabulate(session.call()))
