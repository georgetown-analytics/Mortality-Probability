# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:31:04 2018

@author: iguk
"""
import csv
import plotly
import sqlite3
%matplotlib inline
import numpy as np
import pandas as pd
from ipywidgets import widgets
import matplotlib.pyplot as plt
from IPython.html.widgets import *

f = open('11.csv','r') 

# Skip the header row
next(f, None)
reader = csv.reader(f)

sql = sqlite3.connect('NLMS.db')
cur = sql.cursor()

# Concatenating all files together and adding 'Year' column to create time series for visualization
-------------------------------------------------------------------------------------
cur.execute('''CREATE TABLE IF NOT EXISTS NLMS_11
            (Record INTEGER PRIMARY KEY, Age INTEGER, Race INTEGER, Sex INTEGER, MarStat INTEGER, HispOr INTEGER, AdjInc INTEGER, Educ INTEGER, PlofBirth INTEGER, Wt INTEGER, HhId INTEGER, HhNum INTEGER, RelTRf INTEGER, Occ INTEGER, MajOcc INTEGER, Ind INTEGER, MajInd INTEGER, Esr INTEGER, Urban INTEGER, SMSAST INTEGER, IndDea INTEGER, Cause113 INTEGER, Follow INTEGER, DayOD INTEGER, Hosp INTEGER, HospD INTEGER, SSNYN INTEGER, Vt INTEGER, HIStat INTEGER, HIType INTEGER, PovPct INTEGER, StateR INTEGER, RCOW INTEGER, Tenure INTEGER, Citizen INTEGER, Health INTEGER, IndAlg INTEGER, Smok100 INTEGER, AgeSmk INTEGER, SmokStat INTEGER, SmokHome INTEGER, CurrTobUse INTEGER, EverUse INTEGER)''') 
			 
for row in reader:
	cur.execute("INSERT OR REPLACE INTO NLMS_11 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
	
f.close()
sql.commit()

cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Year' INTEGER")
cur.execute("PRAGMA table_info(NLMS_11)")
print(cur.fetchall())
for tbl in cur.execute('UPDATE NLMS_11 SET Year = 1990'):
    print(tbl)
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Year=""'):
    print(selected)
    
# Exporting wrangled data to a new CSV file
data = cur.execute("SELECT * FROM NLMS_6b_New")

with open('11_Viz_Data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Year', 'IndDea', 'Cause', 'Age', 'Race', 'Sex', 'MarStat', 'HispOr', 'AdjInc', 'Educ', 'PlofBirth', 'HhNum', 'Occ', 'MajOcc', 'Ind', 'MajInd', 'Esr', 'Urban', 'SMSAST', 'SSNYN', 'Vt', 'HIStat', 'HIType', 'PovPct', 'StateR', 'Tenure', 'Citizen', 'Health', 'Smok100', 'AgeSmk', 'SmokStat', 'SmokHome', 'CurrTobUse', 'EverUse'])
    writer.writerows(data)









