from pydantic import BaseModel
from typing import Optional

class Player(BaseModel):
    name: str
    team_id: str  # Referencia al equipo (ID del equipo)
    goals: int = 0
    assists: int = 0

# Modelo para responder a las solicitudes con solo el ID del jugador
class PlayerResponse(BaseModel):
    id: str
    name: str
    team_id: str
    goals: int
    assists: int
