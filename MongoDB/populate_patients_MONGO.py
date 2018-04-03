################################OLD########################

#CLASS: CSCI493 (Big Data)
#Assignment: Project 1
#Version: 1.0
#Date: 03/14/18
#Students: Yaroslav Markov and Victoria Zhong

#########################
#This script uses mongo API for python to parse 'ROSMAP_RNASeq_entrez.csv',
#'patients.csv', 'ROSMAP_RNASeq_disease_label.csv', and 'entrez_ids_genesymbol.csv',
#convert them into JSON documents, and populate 'patients' collection with them.
#
#The documents have the following structure:
#{
#    "patient_id": value,
#    "age": value,
#    "gender": value,
#    "education": value,
#    "diagnosis": {
#       "number": value,
#       "interpretation": value
#    },
#    "gene_values": [{"entrez": value_1, "value": value_1, "gene_symbol": value_1},...
#                    {"entrez": value_n, "value": value_n, "gene_symbol": value_n}]
#}
#########################


from pymongo import MongoClient

client = MongoClient()
db = client.project_one  #creates a database project_one


with open('../ROSMAP_RNASeq_entrez.csv') as PDG, open('../patients.csv') as PAGE, open('../ROSMAP_RNASeq_disease_label.csv') as NI, open('../entrez_ids_genesymbol.csv') as EGG:
    entrez_reference = []
    for PDGline in PDG:
        if 'PATIENT_ID' in PDGline:
#creates a list of sorted entrez_id as they appear in the header of 'ROSMAP_RNASeq_entrez.csv'
#########################
            for value in PDGline.split(','):
                value = value.strip()
                if value != 'PATIENT_ID' and value != 'DIAGNOSIS':
                    entrez_reference.append(value)
#########################
        else:
#gets patient's id and diagnosis number from 'ROSMAP_RNASeq_entrez.csv'
#########################
            patient_id = PDGline.split(',')[0]
            diagnosis_num = PDGline.split(',')[1]
########################
            diagnosis_inter = 'NA'
            gender = 'NA'
            education = 'NA'
            entrez = 'NA'
            gene_symbol = 'NA'
            gene_value = 0

#gets patient's age, gender, and education from 'patients.csv' using patient_id
########################
            for PAGEline in PAGE:
                if patient_id == PAGEline.split(',')[0]:
                    age = PAGEline.split(',')[1]
                    gender = PAGEline.split(',')[2]
                    education = PAGEline.split(',')[3].strip()
            PAGE.seek(0, 0)
########################

#gets patient's disease from 'ROSMAP_RNASeq_disease_label.csv' using diagnosis number
########################
            for NIline in NI:
               if diagnosis_num == NIline.split()[0]:
                   diagnosis_inter = NIline.split()[1]
            NI.seek(0, 0)
########################

#inserts a non-complete document into 'patients' collection
########################
            result = db.patients.insert_one(
                {
                    "patient_id": patient_id,
                    "age": age,
                    "gender": gender,
                    "education": education,
                    "diagnosis": {
                        "number": diagnosis_num,
                        "interpretation": diagnosis_inter
                    }
                }
            )
########################

#adds gene info to each created document
########################################
            i = 0
            j = 0
            for value in PDGline.split(','):
                if i < 2:
                    i = i + 1  #skips the first two columns in 'ROSMAP_RNASeq_entrez.csv' that correspond to patient_id and diagnosis number  
                else:
                    for EGGline in EGG:
#gets gene's symbol from 'entrez_ids_genesymbol.csv' using gene's entrez_id
#######################
                        if entrez_reference[j] == EGGline.split(',')[0]:
                            gene_symbol = EGGline.split(',')[1]
                    EGG.seek(0, 0)
#######################

#adds gene's entrez_id, symbol, and value in the current patient as an embedded document to "gene_values" array field
#######################                    
                    value = value.strip()
                    db.patients.update({"patient_id": patient_id}, {"$addToSet": {"gene_values": {"entrez": entrez_reference[j], "value": value, "gene_symbol": gene_symbol} }})
                    j = j + 1
#######################
########################################

#prints the whole db
#######################
#    cursor = db.patients.find()
#    for document in cursor:
#        print(document)
#######################
