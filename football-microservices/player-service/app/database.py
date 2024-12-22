from pymongo import MongoClient
from pymongo.collection import Collection
import os

# Conexión con MongoDB (usando una URL de MongoDB por defecto)
MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017/football")
#MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/football")


client = MongoClient(MONGO_URL)

# Base de datos y colección
db = client.get_database()  # Usará la base de datos predeterminada
player_collection = db.players  # Colección de jugadores
