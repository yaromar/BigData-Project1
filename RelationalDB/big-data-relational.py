#!/usr/bin/python
import MySQLdb
import csv
import cgitb

#enable error logging 
cgitb.enable(display = 0, logdir = "../logdir")

ADdb = MySQLdb.connect(host = 'localhost', user = 'bigdata', passwd = 'bigdata')

cursor = ADdb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS ADKnowledgeBase;")
cursor.execute("CREATE TABLE IF NOT EXISTS ADKnowledgeBase.Patients(patient_id varchar(255), age int, gender char(1), education varchar(255));")
cursor.execute("ALTER TABLE ADKnowledgeBase.Patients ADD PRIMARY KEY(patient_id);")
cursor.execute("CREATE TABLE IF NOT EXISTS ADKnowledgeBase.PPI(a int, b int);")
cursor.execute("CREATE TABLE IF NOT EXISTS ADKnowledgeBase.EntrezGeneSymbols( entrez_id int, gene_symbol varchar(255), gene_name varchar(255));")
cursor.execute("ALTER TABLE ADKnowledgeBase.EntrezGeneSymbols ADD PRIMARY KEY(entrez_id);")

#create patient table
#%s for strings %d for ints 
csv_data = csv.reader(file('patients.csv'))

#skip first row
firstline = True;
for row in csv_data:
	if firstline:
		firstline = False
		continue
	else:
		cursor.execute('INSERT INTO ADKnowledgeBase.Patients(patient_id,age,gender,education) VALUES("row[0]","row[1]","row[2]","row[3]");')

#create entrezGeneSymbols table
csv_data = csv.reader(file('entrez_ids_genesymbol.csv'))

firstline = True;
for row in csv_data:
	if firstline:
		firstline = False
		continue
	else:
		cursor.execute('INSERT INTO ADKnowledgeBase.EntrezGeneSymbols(entrez_id, gene_symbol, gene_name) VALUES("row[0]","row[1]","row[2]");')

#create PPI table
csv_data = csv.reader(file('PPI.csv'))

for row in csv_data:
	cursor.execute('INSERT INTO ADKnowledgeBase.PPI(a,b) VALUES("row[0]","row[1]");')

ADdb.commit()
#closes connection
cursor.close()
 
