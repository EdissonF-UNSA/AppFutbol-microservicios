from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models import Team
from bson.objectid import ObjectId
from typing import List

app = FastAPI()

# Conexión con MongoDB
#client = MongoClient("mongodb://localhost:27017")
client = MongoClient("mongodb://mongodb:27017")

db = client["football_db"]
team_collection = db["teams"]

# Crear un equipo
@app.post("/teams/", response_model=Team)
async def create_team(team: Team):
    team_dict = team.dict(by_alias=True)
    result = team_collection.insert_one(team_dict)
    team_dict["_id"] = result.inserted_id
    return team_dict

# Obtener todos los equipos
@app.get("/teams/", response_model=List[Team])
async def get_teams():
    teams = list(team_collection.find())
    return teams

# Obtener un equipo por ID
@app.get("/teams/{team_id}", response_model=Team)
async def get_team(team_id: str):
    team = team_collection.find_one({"_id": ObjectId(team_id)})
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

# Actualizar un equipo
@app.put("/teams/{team_id}", response_model=Team)
async def update_team(team_id: str, team: Team):
    team_dict = team.dict(by_alias=True)
    result = team_collection.find_one_and_update(
        {"_id": ObjectId(team_id)}, {"$set": team_dict}, return_document=True
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return result

# Eliminar un equipo
@app.delete("/teams/{team_id}")
async def delete_team(team_id: str):
    result = team_collection.delete_one({"_id": ObjectId(team_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team deleted successfully"}
