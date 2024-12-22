from fastapi import FastAPI, HTTPException
from models import Player, PlayerResponse
from database import player_collection


from bson import ObjectId
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# Funcióna ertir el ObjectId de MongoDB a string
def str_object_id(id: ObjectId) -> str:
    return str(id)

@app.post("/players/", response_model=PlayerResponse)
async def create_player(player: Player):
    # Convertir el objeto Player a diccionario para insertarlo en MongoDB
    player_dict = player.dict()
    result = player_collection.insert_one(player_dict)
    # Devolver la respuesta con el ID del jugador insertado
    return PlayerResponse(
        id=str_object_id(result.inserted_id),
        name=player.name,
        team_id=player.team_id,
        goals=player.goals,
        assists=player.assists
    )

@app.get("/players/{player_id}", response_model=PlayerResponse)
async def get_player(player_id: str):
    player = player_collection.find_one({"_id": ObjectId(player_id)})
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return PlayerResponse(
        id=str_object_id(player["_id"]),
        name=player["name"],
        team_id=player["team_id"],
        goals=player["goals"],
        assists=player["assists"]
    )

@app.get("/players/", response_model=list[PlayerResponse])
async def get_players():
    players = player_collection.find()
    return [
        PlayerResponse(
            id=str_object_id(player["_id"]),
            name=player["name"],
            team_id=player["team_id"],
            goals=player["goals"],
            assists=player["assists"]
        ) for player in players
    ]
