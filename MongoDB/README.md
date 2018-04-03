Here are all the necessary files to create and use a mongo database with 'genes' collection using 'ROSMAP_RNASeq_entrez.csv' dataset.
The python script gene_stats.py retrieves average and standard deviation values of genes grouped by disease.

Install mongo API for python: 
http://api.mongodb.com/python/current/installation.html

PyMongo documentation:
https://api.mongodb.com/python/current/

To create 'genes' collection run: 
mongoimport -d projectone -c genes --type csv --headerline --file ROSMAP_RNASeq_entrez.csv


GENES COLLECTION DOCUMENT TEMPLATE:
{
	“gene”: {
		"PATIENT_ID": "value",
		“DIAGNOSIS”: “value”,
		“1”: “value”,
		“2”: “value”,
		...
		"n": value *
	}	
}
*where n is the last entrez id
