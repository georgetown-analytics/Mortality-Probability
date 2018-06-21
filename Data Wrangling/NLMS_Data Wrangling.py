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
cur.execute('''CREATE TABLE IF NOT EXISTS NLMS
            (Record INTEGER PRIMARY KEY, Age INTEGER, Race INTEGER, Sex INTEGER, MarStat INTEGER, HispOr INTEGER, AdjInc INTEGER, Educ INTEGER, PlofBirth INTEGER, Wt INTEGER, HhId INTEGER, HhNum INTEGER, RelTRf INTEGER, Occ INTEGER, MajOcc INTEGER, Ind INTEGER, MajInd INTEGER, Esr INTEGER, Urban INTEGER, SMSAST INTEGER, IndDea INTEGER, Cause113 INTEGER, Follow INTEGER, DayOD INTEGER, Hosp INTEGER, HospD INTEGER, SSNYN INTEGER, Vt INTEGER, HIStat INTEGER, HIType INTEGER, PovPct INTEGER, StateR INTEGER, RCOW INTEGER, Tenure INTEGER, Citizen INTEGER, Health INTEGER, IndAlg INTEGER, Smok100 INTEGER, AgeSmk INTEGER, SmokStat INTEGER, SmokHome INTEGER, CurrTobUse INTEGER, EverUse INTEGER)''') 
			 
for row in reader:
	cur.execute("INSERT OR REPLACE INTO NLMS VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
	
f.close()
sql.commit()
# -------------------------------------------------------------------------------------

#for row in cur.execute('SELECT * FROM NLMS'):
	#print(row)*/ - Printting an antire table. Perform only when needed, since it takes long time.

for top in cur.execute('SELECT * FROM NLMS LIMIT 5'):
    print(top)
    
for total in cur.execute('SELECT COUNT(Record) FROM NLMS'):
    print(total)
# Total of 1,835,072
    
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE (Age <>"" AND Race <>"" AND Sex <>"" AND MarStat <>"" AND HispOr <>"" AND Educ <>"" AND PlofBirth <>"" AND HhNum <>"" AND Occ <>"" AND Ind <>"" AND Esr <>"" AND Urban <>"" AND SSNYN <>"" AND Vt <>"" AND HIStat <>"" AND PovPct <>"" AND StateR <>"" AND Tenure <>"" AND Citizen <>"" AND Health <>"")'):
    print(selected)
# Total of 177,684 records without NULLs in selected columns, with only 2,613 deaths (0.015%)
    
# Updating Sex to binary value (1=Male, 0=Female) 
for tbl in cur.execute('UPDATE NLMS SET Sex=0 WHERE Sex=2'):
    print(tbl)    
# Checking whether update was done - query should return no records  
for top in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE Sex=2'):
    print(top)
    
# Updating Race =0 for records with missing data
for tbl in cur.execute('UPDATE NLMS SET Race=0 WHERE Race=""'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE Race =""'):
    print(selected)
    
# Updating HisOr =0 for records with missing data
for tbl in cur.execute('UPDATE NLMS SET HispOr=0 WHERE HispOr=""'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE HispOr =""'):
    print(selected)
    
# Updating Marital Status =0 for records where Age <= 15
for tbl in cur.execute('UPDATE NLMS SET MarStat=0 WHERE (Age <=15 AND MarStat="")'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE (Age <=15 AND MarStat ="")'):
    print(selected)
    
# Updating Education =0 for records where Age <= 14
for tbl in cur.execute('UPDATE NLMS SET Educ=0 WHERE (Age <=14 AND Educ="")'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE (Age <=14 AND Educ ="")'):
    print(selected)
    
# Updating Veteran =0 for records where Age <= 18
for tbl in cur.execute('UPDATE NLMS SET Vt=0 WHERE (Age <=18 AND Vt="")'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE (Age <=18 AND Vt ="")'):
    print(selected)
    
# Updating Urban to binary value (1=Urban, 0=Rural) 
for tbl in cur.execute('UPDATE NLMS SET Urban=0 WHERE Urban=2'):
    print(tbl)    
# Checking whether update was done - query should return no records  
for top in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE Urban=2'):
    print(top)

# Updating Esr =0 for records where Age <= 13
for tbl in cur.execute('UPDATE NLMS SET Esr=0 WHERE (Age <=13 AND Esr="")'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE (Age <=13 AND Esr ="")'):
    print(selected)
    
# Updating Ind =0 for records where Age <= 13
for tbl in cur.execute('UPDATE NLMS SET Ind=0 WHERE (Age <=13 AND Ind="")'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE (Age <=13 AND Ind ="")'):
    print(selected)
    
# Updating Occ =0 for records where Age <= 14
for tbl in cur.execute('UPDATE NLMS SET Occ=0 WHERE (Age <=14 AND Occ="")'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE (Age <=14 AND Occ ="")'):
    print(selected)
    
# Updating Health =0 for all missing records
for tbl in cur.execute('UPDATE NLMS SET Health=0 WHERE Health=""'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE Health=""'):
    print(selected)

# Updating Citizen =0 for all missing records
for tbl in cur.execute('UPDATE NLMS SET Citizen=0 WHERE Citizen=""'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE Citizen=""'):
    print(selected)
    
# Updating PovPct =0 for all missing records
for tbl in cur.execute('UPDATE NLMS SET PovPct=0 WHERE PovPct=""'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE PovPct=""'):
    print(selected)
    
# Updating Tenure =0 for all missing records
for tbl in cur.execute('UPDATE NLMS SET Tenure=0 WHERE Tenure=""'):
    print(tbl)
# Checking whether update was done - query should return no records  
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE Tenure=""'):
    print(selected)
    
# Checking total patient count after imputing data
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE (Age <>"" AND Race <>"" AND Sex <>"" AND MarStat <>"" AND HispOr <>"" AND Educ <>"" AND PlofBirth <>"" AND HhNum <>"" AND Occ <>"" AND Ind <>"" AND Esr <>"" AND Urban <>"" AND SSNYN <>"" AND Vt <>"" AND HIStat <>"" AND PovPct <>"" AND StateR <>"" AND Tenure <>"" AND Citizen <>"" AND Health <>"")'):
    print(selected)
# Total of 894,220 records without NULLs in selected columns, with only 30,554 deaths (0.03%)
    
# Checking total patient count after imputing data WITHOUT Health Insurance Status variables + Age >=22
for selected in cur.execute('SELECT COUNT(Record) FROM NLMS WHERE (Age >=22 AND Race <>"" AND Sex <>"" AND MarStat <>"" AND HispOr <>"" AND Educ <>"" AND PlofBirth <>"" AND HhNum <>"" AND Occ <>"" AND Ind <>"" AND Esr <>"" AND Urban <>"" AND SSNYN <>"" AND Vt <>"" AND PovPct <>"" AND StateR <>"" AND Tenure <>"" AND Citizen <>"" AND Health <>"") AND IndDea=1'):
    print(selected)
# Total of 860,236 records without NULLs in selected columns, with only 44,201 deaths (0.05%)

# Creating new table with wrangled data only
cur.execute('''CREATE TABLE IF NOT EXISTS NLMS_Updated
            (Record INTEGER PRIMARY KEY, IndDea INTEGER, Age INTEGER, Race INTEGER, Sex INTEGER, MarStat INTEGER, HispOr INTEGER, Educ INTEGER, PlofBirth INTEGER, HhNum INTEGER, Occ INTEGER, Ind INTEGER, Esr INTEGER, Urban INTEGER, SSNYN INTEGER, Vt INTEGER, PovPct INTEGER, StateR INTEGER, Tenure INTEGER, Citizen INTEGER, Health INTEGER)''')

cur.execute('''INSERT OR Replace INTO NLMS_Updated
            (Record, IndDea, Age, Race, Sex, MarStat, HispOr, Educ, PlofBirth, HhNum, Occ, Ind, Esr, Urban, SSNYN, Vt, PovPct, StateR, Tenure, Citizen, Health)
            SELECT Record, IndDea, Age, Race, Sex, MarStat, HispOr, Educ, PlofBirth, HhNum, Occ, Ind, Esr, Urban, SSNYN, Vt, PovPct, StateR, Tenure, Citizen, Health FROM NLMS WHERE (Age >=22 AND Race <>"" AND Sex <>"" AND MarStat <>"" AND HispOr <>"" AND Educ <>"" AND PlofBirth <>"" AND HhNum <>"" AND Occ <>"" AND Ind <>"" AND Esr <>"" AND Urban <>"" AND SSNYN <>"" AND Vt <>"" AND PovPct <>"" AND StateR <>"" AND Tenure <>"" AND Citizen <>"" AND Health <>"")''')

for top in cur.execute('SELECT * FROM NLMS_Updated LIMIT 5'):
    print(top)
    
# Exporting wrangled data to a new CSV file
data = cur.execute("SELECT * FROM NLMS_Updated")

with open('11_Updated_Data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Record', 'IndDea', 'Age', 'Race', 'Sex', 'MarStat', 'HispOr', 'Educ', 'PlofBirth', 'HhNum', 'Occ', 'Ind', 'Esr', 'Urban', 'SSNYN', 'Vt', 'PovPct', 'StateR', 'Tenure', 'Citizen', 'Health'])
    writer.writerows(data)
    
sql.close()