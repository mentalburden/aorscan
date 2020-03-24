#!/usr/bin/python3

import json
import time
import random
import requests

#https://pkgstore.datahub.io/JohnSnowLabs/country-and-continent-codes-list/country-and-continent-codes-list-csv_json/data/c218eebbf2f8545f3db9051ac893d69c/country-and-continent-codes-list-csv_json.json
filepath = "cc.json"
continent = "Europe"
countrycodes = []
ccasn = 'http://www.cc2asn.com/data/'
ccasnend = '_ipv4'

def writer(cc,string):
        ccstr = cc + '-ranges.txt'
        file = open(ccstr, "w+")
        file.write(string)
        file.close()
        print("wrote " +ccstr)

def iptoasn(cc):
        cleancc = cc.replace("\n","")
        cleanstr = ccasn + cleancc + ccasnend
        randwait = random.randrange(1,4)
        r = requests.get(cleanstr)
        print(r.text)
        writer(cleancc,r.text)
        time.sleep(randwait)

def ccgen():
	counter = 0
	with open(filepath,"r") as file:
		data = json.load(file)
		for x in data:
			if x['Continent_Name'] == continent:
				countrycodes.append(x['Two_Letter_Country_Code'] )
				counter += 1

#main starts here
ccgen()
for x in countrycodes:
	iptoasn(x.lower())
print(countrycodes)
