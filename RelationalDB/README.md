# BigData-Project1

## Requirements:
- mysql - install using the command `sudo apt-get install python-mysqldb` or `yum install mysql-python`
- python - install using the commands `sudo apt-get install python3`

- create a mysql user called 'bigdata' with passwd 'bigdata' - or if you already have a user you would like to use just go into the file and change the credentials to connect. Make sure you user has the permission to create/access the database "ADKnowledgeBase" if your user does not, then log into the root of your MySQL and use the command ```GRANT ALL PRIVELEGES ON `ADKnowledgeBase`.* TO 'user'@'localhost';```

- Run `big-data-relational.py` this will create and populate your tables
