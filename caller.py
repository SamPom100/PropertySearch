from cook import *
from lien import *

#ENTER ADDRESS
houseNumber = "8259"
streetName = "S INGLESIDE AVE"
city = "Chicago"
zipCode = "60619"
unitNumber = ""

propertySearch(houseNumber, streetName, city, zipCode, unitNumber)

print("\n\n\n")

lienSearch(houseNumber, streetName, city, zipCode)