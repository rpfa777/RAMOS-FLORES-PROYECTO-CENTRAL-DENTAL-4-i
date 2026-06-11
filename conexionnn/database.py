from pymongo import MongoClient

# Se quitaron los < > y se cambió el # por %23
client = MongoClient("mongodb+srv://RamosFloresAlexis:Walker%232009@cluster0.7sghwib.mongodb.net/?appName=Cluster0")

# Aquí va el nombre de su base de datos. 
db = client['Central Dental']