import requests
import numpy as np
import json
from Countrydetails import countries
#pip install countrydetails

country = countries.all_countries()
capitals_data = country.capitals()



for country, capital in capitals_data.items():
	if(len(capital) == 0):
		continue
	print(f"{capital} is the capital of {country}")
