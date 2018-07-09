# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:03:24 2018

@author: iguk
"""

import sqlite3
import csv

# Open the csv data file
f = open('11.csv','r') 

# Skip the header row
next(f, None)
reader = csv.reader(f)

sql = sqlite3.connect('NLMS.db')
cur = sql.cursor()

# Create the table if it doesn't already exist - this code has to be executed only once
# -------------------------------------------------------------------------------------
cur.execute('''CREATE TABLE IF NOT EXISTS NLMS_11
            (Record INTEGER PRIMARY KEY, Age INTEGER, Race INTEGER, Sex INTEGER, MarStat INTEGER, HispOr INTEGER, AdjInc INTEGER, Educ INTEGER, PlofBirth INTEGER, Wt INTEGER, HhId INTEGER, HhNum INTEGER, RelTRf INTEGER, Occ INTEGER, MajOcc INTEGER, Ind INTEGER, MajInd INTEGER, Esr INTEGER, Urban INTEGER, SMSAST INTEGER, IndDea INTEGER, Cause113 INTEGER, Follow INTEGER, DayOD INTEGER, Hosp INTEGER, HospD INTEGER, SSNYN INTEGER, Vt INTEGER, HIStat INTEGER, HIType INTEGER, PovPct INTEGER, StateR INTEGER, RCOW INTEGER, Tenure INTEGER, Citizen INTEGER, Health INTEGER, IndAlg INTEGER, Smok100 INTEGER, AgeSmk INTEGER, SmokStat INTEGER, SmokHome INTEGER, CurrTobUse INTEGER, EverUse INTEGER)''') 
			 
for row in reader:
	cur.execute("INSERT OR REPLACE INTO NLMS_11 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
	
f.close()
sql.commit()
# -------------------------------------------------------------------------------------

#for row in cur.execute('SELECT * FROM NLMS_11'):
	#print(row)*/ - Printting an antire table. Perform only when needed, since it takes long time.

for top in cur.execute('SELECT * FROM NLMS_11 LIMIT 5'):
    print(top)
    
for total in cur.execute('SELECT COUNT(Record) FROM NLMS_11'):
    print(total)
# Total of 1,835,072

#-------------------------------Sex---------------------------------------------    
# Updating Sex to binary value (1=Male, 0=Female) 
for tbl in cur.execute('UPDATE NLMS_11 SET Sex=0 WHERE Sex=2'):
    print(tbl)    
# Checking whether update was done - query should return no records  
for top in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Sex=2'):
    print(top)
    
#-------------------------------Race--------------------------------------------    
# Updating Race =0 for records where Race <>1 (NonWhite)
for tbl in cur.execute('UPDATE NLMS_11 SET Race=0 WHERE Race <>1'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Race IN (2,3,4,5)'):
    print(selected)
    
#-------------------------------HispOrigin------------------------------------
# Updating HisOr =1
for tbl in cur.execute('UPDATE NLMS_11 SET HispOr=1 WHERE HispOr IN (1,2)'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE HispOr ="2"'):
    print(selected)
# Updating HisOr =0
for tbl in cur.execute('UPDATE NLMS_11 SET HispOr=0 WHERE HispOr<>1'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE HispOr IN (2,3)'):
    print(selected)
    
#------------------------------Age Bins-------------------------------
# Creating new columns for Age bins
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Age_Cat21' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Age_Cat35' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Age_Cat45' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Age_Cat55' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Age_Cat65' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Age_Cat75' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Age_Cat85' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Age_Cat86Pl' INTEGER")
# Verifying if column was added
cur.execute("PRAGMA table_info(NLMS_11)")
print(cur.fetchall())

# Updating Age_Cat21
for tbl in cur.execute('UPDATE NLMS_11 SET Age_Cat21 = CASE WHEN Age<22 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Age_Cat21=1'):
    print(selected)

# Updating Age_Cat35
for tbl in cur.execute('UPDATE NLMS_11 SET Age_Cat35 = CASE WHEN Age BETWEEN 22 AND 35 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Age_Cat35=1'):
    print(selected)
    
# Updating Age_Cat45
for tbl in cur.execute('UPDATE NLMS_11 SET Age_Cat45 = CASE WHEN Age BETWEEN 36 AND 45 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Age_Cat45=1'):
    print(selected)

# Updating Age_Cat55
for tbl in cur.execute('UPDATE NLMS_11 SET Age_Cat55 = CASE WHEN Age BETWEEN 46 AND 55 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Age_Cat55=1'):
    print(selected)
    
# Updating Age_Cat65
for tbl in cur.execute('UPDATE NLMS_11 SET Age_Cat65 = CASE WHEN Age BETWEEN 56 AND 65 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Age_Cat65=1'):
    print(selected)
    
# Updating Age_Cat75
for tbl in cur.execute('UPDATE NLMS_11 SET Age_Cat75 = CASE WHEN Age BETWEEN 66 AND 75 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Age_Cat75=1'):
    print(selected)
    
# Updating Age_Cat85
for tbl in cur.execute('UPDATE NLMS_11 SET Age_Cat85 = CASE WHEN Age BETWEEN 76 AND 85 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Age_Cat85=1'):
    print(selected)
    
# Updating Age_Cat86Pl
for tbl in cur.execute('UPDATE NLMS_11 SET Age_Cat86Pl = CASE WHEN Age>85 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Age_Cat86Pl=1'):
    print(selected)

#-------------------------------Education------------------------------------
# Creating new columns for categorical Education variables
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Educ_Elem' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Educ_HS' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Educ_HSCompl' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Educ_Collg' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Educ_CollgCompl' INTEGER")
# Verifying if column was added
cur.execute("PRAGMA table_info(NLMS_11)")
print(cur.fetchall())

# Populating new Education columns w/ categorical variables
# Elementary
for tbl in cur.execute('UPDATE NLMS_11 SET Educ_Elem = CASE WHEN Educ<05 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Educ_Elem=1'):
    print(selected)

# Some High School
for tbl in cur.execute('UPDATE NLMS_11 SET Educ_HS = CASE WHEN Educ IN (5,6,7) THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Educ_HS=1'):
    print(selected)

# Completed High School
for tbl in cur.execute('UPDATE NLMS_11 SET Educ_HSCompl = CASE WHEN Educ=8 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Educ_HSCompl=1'):
    print(selected)
    
# Some College
for tbl in cur.execute('UPDATE NLMS_11 SET Educ_Collg = CASE WHEN Educ IN (9,10,11) THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Educ_Collg=1'):
    print(selected)
    
# Completed College
for tbl in cur.execute('UPDATE NLMS_11 SET Educ_CollgCompl = CASE WHEN Educ>11 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Educ_CollgCompl=1'):
    print(selected)

#------------------------------Urban--------------------------------------
# Updating Urban to binary value (1=Urban, 0=Rural) 
for tbl in cur.execute('UPDATE NLMS_11 SET Urban=0 WHERE Urban=2'):
    print(tbl)    
# Checking whether update was done - query should return no records  
for top in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Urban=2'):
    print(top)
    
#------------------------------Place of Birth-----------------------------------  
# Updating PlofBirth=1 (US Born), 0 (NonUS Born)
for tbl in cur.execute('UPDATE NLMS_11 SET PlofBirth = CASE WHEN PlofBirth>111 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE PlofBirth>111'):
    print(selected)

#------------------------------Marital Status-----------------------------------  
# Updating Marital Status =0 for records where MarStat >1
for tbl in cur.execute('UPDATE NLMS_11 SET MarStat=0 WHERE MarStat >1'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE MarStat>1'):
    print(selected)

#------------------------------Tenure-------------------------------------------
# Updating Tenure =0
for tbl in cur.execute('UPDATE NLMS_11 SET Tenure=0 WHERE Tenure<>1'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Tenure IN (2,3)'):
    print(selected)
    
#------------------------------Employment---------------------------------------
# Updating Esr =0 for records where Esr <>1
for tbl in cur.execute('UPDATE NLMS_11 SET Esr=0 WHERE Esr<>1'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Esr IN (2,3,4,5)'):
    print(selected)
    
#------------------------------Poverty Level------------------------------------
# Creating new columns for categorical Poverty variables
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'InPoverty' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Poverty_Gr2' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Poverty_Gr3' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Poverty_Gr4' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'NotInPoverty' INTEGER")
# Verifying if column was added
cur.execute("PRAGMA table_info(NLMS_11)")
print(cur.fetchall())

# Updating InPoverty
for tbl in cur.execute('UPDATE NLMS_11 SET InPoverty = CASE WHEN PovPct<4 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE InPoverty=1'):
    print(selected)

# Updating Poverty_Gr2
for tbl in cur.execute('UPDATE NLMS_11 SET Poverty_Gr2 = CASE WHEN PovPct BETWEEN 4 AND 7 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Poverty_Gr2=1'):
    print(selected)

# Updating Poverty_Gr3
for tbl in cur.execute('UPDATE NLMS_11 SET Poverty_Gr3 = CASE WHEN PovPct BETWEEN 8 AND 11 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Poverty_Gr3=1'):
    print(selected)
    
# Updating Poverty_Gr4
for tbl in cur.execute('UPDATE NLMS_11 SET Poverty_Gr4 = CASE WHEN PovPct BETWEEN 12 AND 15 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Poverty_Gr4=1'):
    print(selected)
    
# Updating NotInPoverty
for tbl in cur.execute('UPDATE NLMS_11 SET NotInPoverty = CASE WHEN PovPct>15 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE NotInPoverty=1'):
    print(selected)
    
#------------------------------Place of Residence-------------------------------
# Creating new columns for categorical POR variables
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Res_NewEng' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Res_MidAtl' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Res_ENCentr' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Res_WNCentr' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Res_SAtl' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Res_ESCentr' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Res_WSCentr' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Res_Mountain' INTEGER")
cur.execute("ALTER TABLE NLMS_11 ADD COLUMN 'Res_Pacific' INTEGER")
# Verifying if column was added
cur.execute("PRAGMA table_info(NLMS_11)")
print(cur.fetchall())

# Updating Res_NewEng
for tbl in cur.execute('UPDATE NLMS_11 SET Res_NewEng = CASE WHEN StateR<17 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Res_NewEng=1'):
    print(selected)
    
# Updating Res_MidAtl
for tbl in cur.execute('UPDATE NLMS_11 SET Res_MidAtl = CASE WHEN StateR BETWEEN 21 AND 23 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Res_MidAtl=1'):
    print(selected)
    
# Updating Res_ENCentr
for tbl in cur.execute('UPDATE NLMS_11 SET Res_ENCentr = CASE WHEN StateR BETWEEN 31 AND 35 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Res_ENCentr=1'):
    print(selected)
    
# Updating Res_WNCentr
for tbl in cur.execute('UPDATE NLMS_11 SET Res_WNCentr = CASE WHEN StateR BETWEEN 41 AND 47 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Res_WNCentr=1'):
    print(selected)
    
# Updating Res_SAtl
for tbl in cur.execute('UPDATE NLMS_11 SET Res_SAtl = CASE WHEN StateR BETWEEN 51 AND 59 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Res_SAtl=1'):
    print(selected)
    
# Updating Res_ESCentr
for tbl in cur.execute('UPDATE NLMS_11 SET Res_ESCentr = CASE WHEN StateR BETWEEN 61 AND 64 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Res_ESCentr=1'):
    print(selected)
    
# Updating Res_WSCentr
for tbl in cur.execute('UPDATE NLMS_11 SET Res_WSCentr = CASE WHEN StateR BETWEEN 71 AND 74 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Res_WSCentr=1'):
    print(selected)

# Updating Res_Mountain
for tbl in cur.execute('UPDATE NLMS_11 SET Res_Mountain = CASE WHEN StateR BETWEEN 81 AND 88 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Res_Mountain=1'):
    print(selected)
    
# Updating Res_Pacific
for tbl in cur.execute('UPDATE NLMS_11 SET Res_Pacific = CASE WHEN StateR BETWEEN 91 AND 95 THEN 1 ELSE 0 END'):
    print(tbl)
# Checking whether update was done
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE Res_Pacific=1'):
    print(selected)
   
# Checking total patient count after creating categorical variables
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS_11 WHERE (Age <>"" AND Age_Cat21=0 AND Race <>"" AND Sex <>"" AND MarStat <>"" AND HispOr <>"" AND Educ <>"" AND PlofBirth <>"" AND Esr <>"" AND Urban <>"" AND SSNYN <>"" AND Vt <>"" AND PovPct <>"" AND StateR <>"" AND Tenure <>"") AND IndDea=0'):
    print(selected)
# Total of 1,261,033 records without NULLs in selected columns, with 157,125 deaths (12.5%)
    
# Creating new table with wrangled data only
cur.execute('''CREATE TABLE IF NOT EXISTS NLMS_11_New
            (Record INTEGER PRIMARY KEY, IndDea INTEGER NOT NULL, Age INTEGER NOT NULL, Age_Cat21 INTEGER NOT NULL, Age_Cat35 INTEGER NOT NULL, Age_Cat45 INTEGER NOT NULL, Age_Cat55 INTEGER NOT NULL, Age_Cat65 INTEGER NOT NULL, Age_Cat75 INTEGER NOT NULL, Age_Cat85 INTEGER NOT NULL, Age_Cat86Pl INTEGER NOT NULL, Race INTEGER NOT NULL, Sex INTEGER NOT NULL, MarStat INTEGER NOT NULL, HispOr INTEGER NOT NULL, Educ_Elem INTEGER NOT NULL, Educ_HS INTEGER NOT NULL, Educ_HSCompl INTEGER NOT NULL, Educ_Collg INTEGER NOT NULL, Educ_CollgCompl INTEGER NOT NULL, PlofBirth INTEGER NOT NULL, Urban INTEGER NOT NULL, SSNYN INTEGER NOT NULL, Vt INTEGER NOT NULL, Tenure INTEGER NOT NULL, InPoverty INTEGER NOT NULL, Poverty_Gr2 INTEGER NOT NULL, Poverty_Gr3 INTEGER NOT NULL, Poverty_Gr4 INTEGER NOT NULL, NotInPoverty INTEGER NOT NULL, Esr INTEGER NOT NULL, Res_NewEng INTEGER NOT NULL, Res_MidAtl INTEGER NOT NULL, Res_ENCentr INTEGER NOT NULL, Res_WNCentr INTEGER NOT NULL, Res_SAtl INTEGER NOT NULL, Res_ESCentr INTEGER NOT NULL, Res_WSCentr INTEGER NOT NULL, Res_Mountain INTEGER NOT NULL, Res_Pacific INTEGER NOT NULL)''')

cur.execute('''INSERT OR REPLACE INTO NLMS_11_New
            (Record, IndDea, Age, Age_Cat21, Age_Cat35, Age_Cat45, Age_Cat55, Age_Cat65, Age_Cat75, Age_Cat85, Age_Cat86Pl, Race, Sex, MarStat, HispOr, Educ_Elem, Educ_HS, Educ_HSCompl, Educ_Collg, Educ_CollgCompl, PlofBirth, Urban, SSNYN, Vt, Tenure, InPoverty, Poverty_Gr2, Poverty_Gr3, Poverty_Gr4, NotInPoverty, Esr, Res_NewEng, Res_MidAtl, Res_ENCentr, Res_WNCentr, Res_SAtl, Res_ESCentr, Res_WSCentr, Res_Mountain, Res_Pacific)
            SELECT Record, IndDea, Age, Age_Cat21, Age_Cat35, Age_Cat45, Age_Cat55, Age_Cat65, Age_Cat75, Age_Cat85, Age_Cat86Pl, Race, Sex, MarStat, HispOr, Educ_Elem, Educ_HS, Educ_HSCompl, Educ_Collg, Educ_CollgCompl, PlofBirth, Urban, SSNYN, Vt, Tenure, InPoverty, Poverty_Gr2, Poverty_Gr3, Poverty_Gr4, NotInPoverty, Esr, Res_NewEng, Res_MidAtl, Res_ENCentr, Res_WNCentr, Res_SAtl, Res_ESCentr, Res_WSCentr, Res_Mountain, Res_Pacific FROM NLMS_11 WHERE (Age <>"" AND Age_Cat21=0 AND Race <>"" AND Sex <>"" AND MarStat <>"" AND HispOr <>"" AND Educ <>"" AND PlofBirth <>"" AND Esr <>"" AND Urban <>"" AND SSNYN <>"" AND Vt <>"" AND PovPct <>"" AND StateR <>"" AND Tenure <>"")''')

# Verifying if all columns were created
cur.execute("PRAGMA table_info(NLMS_11_New)")
print(cur.fetchall())

for top in cur.execute('SELECT * FROM NLMS_11_New LIMIT 5'):
    print(top)
    
# Exporting wrangled data to a new CSV file
data = cur.execute("SELECT * FROM NLMS_11_New")

with open('11_Updated_Data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Record', 'IndDea', 'Age', 'Age_Cat21', 'Age_Cat35', 'Age_Cat45', 'Age_Cat55', 'Age_Cat65', 'Age_Cat75', 'Age_Cat85', 'Age_Cat86Pl', 'Race', 'Sex', 'MarStat', 'HispOr', 'Educ_Elem', 'Educ_HS', 'Educ_HSCompl', 'Educ_Collg', 'Educ_CollgCompl', 'PlofBirth', 'Urban', 'SSNYN', 'Vt', 'Tenure', 'InPoverty', 'Poverty_Gr2', 'Poverty_Gr3', 'Poverty_Gr4', 'NotInPoverty', 'Esr', 'Res_NewEng', 'Res_MidAtl', 'Res_ENCentr', 'Res_WNCentr', 'Res_SAtl', 'Res_ESCentr', 'Res_WSCentr', 'Res_Mountain', 'Res_Pacific'])
    writer.writerows(data)
    
sql.close()