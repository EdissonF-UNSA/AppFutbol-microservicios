from typing import Any, Dict
from pydantic_core import CoreSchema
from pydantic.json_schema import GetJsonSchemaHandler
from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId


# Clase auxiliar para manejar ObjectId de MongoDB
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid ObjectId: {v}")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> Dict[str, Any]:
        json_schema = handler(core_schema)
        json_schema.update(type="string")
        return json_schema


#Modelo para los equipos
class Team(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")  # Alias para _id de MongoDB
    name: str
    location: str
    player_ids: List[str] = []  # Lista de ids de jugadores

    class Config:
        # Configuración para permitir el uso de nombres de campo en lugar de alias
        populate_by_name = True  # Cambiado de `allow_population_by_field_name`
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}  # Convertir ObjectId a cadena cuando se convierte a JSON
