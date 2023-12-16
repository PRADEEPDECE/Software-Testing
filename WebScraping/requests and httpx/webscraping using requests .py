# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:49:02 2023

@author: prade
"""

import time 
import requests 


def fetch_urls(): 
	urls=[ 
		"https://en.wikipedia.org/wiki/Badlands", 
		"https://en.wikipedia.org/wiki/Canyon", 
		"https://en.wikipedia.org/wiki/Cave", 
		"https://en.wikipedia.org/wiki/Cliff", 
		"https://en.wikipedia.org/wiki/Coast", 
		"https://en.wikipedia.org/wiki/Continent", 
		"https://en.wikipedia.org/wiki/Coral_reef", 
		"https://en.wikipedia.org/wiki/Desert", 
		"https://en.wikipedia.org/wiki/Forest", 
		"https://en.wikipedia.org/wiki/Geyser", 
		"https://en.wikipedia.org/wiki/Mountain_range", 
		"https://en.wikipedia.org/wiki/Peninsula", 
		"https://en.wikipedia.org/wiki/Ridge", 
		"https://en.wikipedia.org/wiki/Savanna", 
		"https://en.wikipedia.org/wiki/Shoal", 
		"https://en.wikipedia.org/wiki/Steppe", 
		"https://en.wikipedia.org/wiki/Tundra", 
		"https://en.wikipedia.org/wiki/Valley", 
		"https://en.wikipedia.org/wiki/Volcano", 
		"https://en.wikipedia.org/wiki/Artificial_island", 
		"https://en.wikipedia.org/wiki/Lake"
	] 

	res = [requests.get(addr).status_code for addr in urls] 

	print(set(res)) 




start = time.time() 
fetch_urls() 
end = time.time() 

print("Total Consumed Time",end-start)
