from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime
from pydantic.json_schema import GetJsonSchemaHandler
from pydantic_core import CoreSchema
from typing import Any, Dict

# Clase auxiliar para manejar ObjectId de MongoDB
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> Dict[str, Any]:
        json_schema = handler(core_schema)
        json_schema.update(type="string")
        return json_schema

# Modelo para las estadísticas de los partidos
class MatchStats(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")  # Alias para _id de MongoDB
    match_id: str
    team_id: str
    opponent_id: str
    goals_for: int
    goals_against: int
    win: bool
    date: datetime

    class Config:
        populate_by_name = True  # Cambiado de `allow_population_by_field_name`
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,  # Convertir ObjectId a cadena cuando se convierte a JSON
            datetime: lambda dt: dt.isoformat(),  # Convertir datetime a ISO 8601
        }
