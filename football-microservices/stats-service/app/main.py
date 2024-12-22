from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models import MatchStats
from bson.objectid import ObjectId
from typing import List
from datetime import datetime

app = FastAPI()

# Conexión con MongoDB
#client = MongoClient("mongodb://localhost:27017")
client = MongoClient("mongodb://mongodb:27017")


db = client["football_db"]
stats_collection = db["stats"]

# Crear estadísticas de un partido
@app.post("/stats/", response_model=MatchStats)
async def create_stats(stats: MatchStats):
    stats_dict = stats.dict(by_alias=True)
    stats_dict["date"] = stats.date or datetime.utcnow()  # Establecer fecha si no se proporciona
    result = stats_collection.insert_one(stats_dict)
    stats_dict["_id"] = result.inserted_id
    return stats_dict

# Obtener todas las estadísticas
@app.get("/stats/", response_model=List[MatchStats])
async def get_stats():
    stats = list(stats_collection.find())
    return stats

# Obtener estadísticas de un partido específico por ID
@app.get("/stats/{stats_id}", response_model=MatchStats)
async def get_stat_by_id(stats_id: str):
    stats = stats_collection.find_one({"_id": ObjectId(stats_id)})
    if stats is None:
        raise HTTPException(status_code=404, detail="Stats not found")
    return stats

# Actualizar estadísticas de un partido
@app.put("/stats/{stats_id}", response_model=MatchStats)
async def update_stat(stats_id: str, stats: MatchStats):
    stats_dict = stats.dict(by_alias=True)
    result = stats_collection.find_one_and_update(
        {"_id": ObjectId(stats_id)}, {"$set": stats_dict}, return_document=True
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Stats not found")
    return result

# Eliminar estadísticas de un partido
@app.delete("/stats/{stats_id}")
async def delete_stat(stats_id: str):
    result = stats_collection.delete_one({"_id": ObjectId(stats_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Stats not found")
    return {"message": "Stats deleted successfully"}
