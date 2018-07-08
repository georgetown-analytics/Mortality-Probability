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
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Age_Cat' TEXT")
for tbl in cur.execute('UPDATE NLMS_11 SET Age_Cat = CASE WHEN Age<22 THEN "<22" WHEN Age BETWEEN 22 AND 35 THEN "22-35" WHEN Age BETWEEN 36 AND 45 THEN "36-45" WHEN Age BETWEEN 46 AND 55 THEN "46-55" WHEN Age BETWEEN 56 AND 65 THEN "56-65" WHEN Age BETWEEN 66 AND 75 THEN "66-75" WHEN Age BETWEEN 76 AND 85 THEN "76-85" WHEN Age > 85 THEN ">85" ELSE "" END'):
    print(tbl)
for tbl in cur.execute('UPDATE NLMS_11 SET SEX = CASE WHEN SEX = 1 THEN "M" WHEN SEX = 2 THEN "F" ELSE "" END'):
    print(tbl)
for check in cur.execute('SELECT COUNT(*) FROM NLMS_11 WHERE SEX IN (1,2)'):
    print(check)
for tbl in cur.execute('UPDATE NLMS_11 SET RACE = CASE WHEN RACE = 1 THEN "W" WHEN RACE = 2 THEN "B" WHEN RACE = 3 THEN "AmIn" WHEN RACE = 4 THEN "As/PI" WHEN RACE = 5 THEN "OthNnWh" ELSE "" END'):
    print(tbl)
for check in cur.execute('SELECT COUNT(*) FROM NLMS_11 WHERE RACE IN (1,2,3,4,5)'):
    print(check)
for tbl in cur.execute('UPDATE NLMS_11 SET MARSTAT = CASE WHEN MARSTAT = 1 THEN "M" WHEN MARSTAT IN (2,3,4,5) THEN "NM" ELSE "" END'):
    print(tbl)
for check in cur.execute('SELECT COUNT(*) FROM NLMS_11 WHERE MARSTAT IN (1,2,3,4,5)'):
    print(check)
for tbl in cur.execute('UPDATE NLMS_11 SET StateR = CASE WHEN MARSTAT = 1 THEN "M" WHEN MARSTAT IN (2,3,4,5) THEN "NM" ELSE "" END'):
    print(tbl)
for check in cur.execute('SELECT COUNT(*) FROM NLMS_11 WHERE MARSTAT IN (1,2,3,4,5)'):
    print(check)
    
    
    
    
    
    
    
# Exporting wrangled data to a new CSV file
data = cur.execute("SELECT * FROM NLMS_11_New")

with open('11_Viz_Data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Year', 'IndDea', 'Cause', 'Age', 'Race', 'Sex', 'MarStat', 'HispOr', 'AdjInc', 'Educ', 'PlofBirth', 'HhNum', 'Occ', 'MajOcc', 'Ind', 'MajInd', 'Esr', 'Urban', 'SMSAST', 'SSNYN', 'Vt', 'HIStat', 'HIType', 'PovPct', 'StateR', 'Tenure', 'Citizen', 'Health', 'Smok100', 'AgeSmk', 'SmokStat', 'SmokHome', 'CurrTobUse', 'EverUse'])
    writer.writerows(data)









sql.close()