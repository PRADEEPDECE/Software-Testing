# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:55:20 2023

@author: prade
"""

import requests
from bs4 import BeautifulSoup
url ="https://www.91mobiles.com/latest-mobiles-in-india?utm_source=google&utm_medium=cpc&utm_campaign=&campaignid=20847217911&adgroupid=&utm_term=&device=c&gclid=CjwKCAiAg9urBhB_EiwAgw88mdPloP_lX9RiouldbFUYKlQ7zpdX4NYyilUiHhd3HLw1-TiVsWrepRoCbCMQAvD_BwE"
response = requests.get(url)
list_name=[]
soup = BeautifulSoup(response.content,"html.parser")
element_name =soup.find_all('a',class_='hover_blue_link name gaclick')
list_name =[element.text.strip() for element in element_name]
for name in list_name:
    print(name)