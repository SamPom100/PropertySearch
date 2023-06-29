from cook import *
from lien import *

#ENTER ADDRESS
houseNumber = "1049"
streetName = "Pontiac Rd"
city = "Wilmette"
zipCode = "60091"
unitNumber = ""

propertySearch(houseNumber, streetName, city, zipCode, unitNumber)

print("\n\n\n")

lienSearch(houseNumber, streetName, city, zipCode)