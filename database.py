#Esta es nuestra conexión con MongoDB, donde vamos a colocar la URL que nos da la página. 

from pymongo import MongoClient
#Tienes que instalar pymongo desde la terminal, ingresa "pip install pymongo" y listo. 

client = MongoClient("mongodb+srv://RamosFloresAlexis:ramos123@cluster0.7sghwib.mongodb.net/?appName=Cluster0")

#Aquí va el nombre de su base de datos. 
db = client['sample_mflix']