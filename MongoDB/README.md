Here are all the necessary files to create a mongo database with 'patients' and 'genes' collections using 'ROSMAP_RNASeq_entrez.csv',
#'patients.csv', 'ROSMAP_RNASeq_disease_label.csv', 'entrez_ids_genesymbol.csv', and PPI.csv data sets.

Install mongo API for python: 
http://api.mongodb.com/python/current/installation.html

PyMongo documentation:
https://api.mongodb.com/python/current/


To create a 'patients' collection run 'populate_patients_MONGO.py'.



!!!!!OLD OLD OLD!!!!!!!
PATIENT DOCUMENT TEMPLATE:
Allows to:
	1) query mean and std of gene expression associated with a particular disease
	2) query patient info
*************************************************************************************
{
    "patient": {
        "patient_id": value,
         "age": value,
         "gender": value,
         "education": value,
         "diagnosis": {
             "number": value,
             "interpretation": value
          },
          "gene_values": [{"entrez": value_1, "value": value_1, "gene_symbol": value_1},...
                          {"entrez": value_n, "value": value_n, "gene_symbol": value_n}]
   }
}


GENE DOCUMENT TEMPLATE:
Allows to:
	1) query n-order interactions of a gene
	2) query gene info
*************************************************************************************
{
	“gene”: {
		“entrez_id”: “value”,
		“gene_symbol”: “value”,
		“gene_name”: “value”,
		“interactions”: [“value_1”,…”value_n”]
	}	
}
!!!!!!!!!!!!!
