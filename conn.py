#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 04:07:32 2022

@author: pukar
"""


import web_scraper as gs
import pandas as pd

path = "/Users/pukar/Documents/web_scraper/chromedriver"

df= gs.get_jobs('data scientist', 20, False, path, 15)

df.to_csv('Uncleaned_DS_jobs.csv', index=False)