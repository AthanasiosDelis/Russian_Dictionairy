# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 12:01:34 2021

@author: Thanasis
"""

import inspect
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import numpy as np
import re
import json
import requests
import tkinter
import playsound
#try:
 #html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
url ='https://en.bab.la/translator/?fbclid=IwAR2_WetcRL9aGCyn0ntzc49bJq9M_tdCUQjYDkj6v619tR0uvZf9pVtxlnQ'

"""
except HTTPError as e:
 print(e)
except URLError as e:
 print('The server could not be found!')
else:
 print('It Worked!')
"""
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# Constants 
app_id  = "Your AppID"
app_key  = "Your Key"
headers = {'app_id': app_id, 'app_key': app_key}
language_code = "en-us" # Change language if you want to use 
#a different once

 # Pull data via URL
url = "https://od-api.oxforddictionaries.com/api/v2/entries/" \
 + language_code + "/" + getword.lower()

r_status = requests.get(url, headers=headers)

# This checks if the api is live or not <Response [200]>
print(r_status)

# Additional varibles for readability
r_mean = r_status
r_audio = r_mean

# Create a button widget
    # The get_word() 
b1 = Button(window,text="Get Meaning",command=get_word)
b1.grid(row=0,column=2)

   # The delete function is called when the button is pushed
b2 = Button(window,text="Clear",command=delete)
b2.grid(row=1,column=2)

   # The get_audio function is called when the button is 
pushed
b3 =Button(window,text="Pronunciations",command=get_audio)
b3.grid(row=4,column=1)

  # Create four empty text boxes t1

t1 = Text(window,height=2,width=45,font = ("Times New Roman",12) )
t1.grid(row=3,column=1, pady = 5, padx = 2.5)
t1.config(wrap=WORD)
# Logic to pull meaning of the word 
def get_word(): 
        #Multiple for loops increases the running time.

    for result in mean_json['results'][0]['lexicalEntries'][0]['entries']:
        for sense in result['senses']:
            mean_list.append(sense['definitions'][0])

    for i in mean_list:
        return (i)


 # Logic to pull audio file
def get_audio():
    for result in audio_json['results'][0]['lexicalEntries'][0]['entries']:
        for pronunciations in result['pronunciations']:
            audio_list.append(pronunciations)