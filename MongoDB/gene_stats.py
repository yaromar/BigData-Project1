#CLASS: CSCI493 (Big Data)
#Assignment: Project 1
#Version: 2.0
#Date: 04/02/18
#Students: Yaroslav Markov and Victoria Zhong

#########################
#This script uses mongo API for python to retrieve average and standard deviation 
#of gene values grouped by disease.
#The dataset used: 'ROSMAP_RNASeq_entrez.csv'.
#Created the genes collection with:  mongoimport -d projectone -c genes --type csv --file ROSMAP_RNASeq_entrez.csv --headerline
#
#The documents have PATIENT_ID, DIAGNOSIS, and all entrez_ids as their fields.
#########################


from pymongo import MongoClient

client = MongoClient()
db = client.project_one  #connects to db project_one

#result = db.patients.delete_many({})

gene = input('Enter entrez id of the gene: ')
gene = str(gene)

#creates a pipeline that calculates average and std values of given gene, aggregates and sorts the results by disease.
#######################
pipe = [{'$group': {'_id': '$DIAGNOSIS', 'average': {'$avg': '$'+gene}, 'stdDev': {'$stdDevPop': '$'+gene} } },
        {'$sort': {'_id': 1}}
]
#######################

#prints the results
#######################
cursor = db.genes.aggregate(pipeline=pipe)
for document in cursor:
    print("Diagnosis: " + str(document['_id']) + ", average: " + str(document['average']) + ", std: " + str(document['stdDev']))

#######################
