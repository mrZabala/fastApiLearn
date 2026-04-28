from enum import Enum

class StatusMovie(str, Enum):
    CREATED = "Creado",
    UPDATED = "Editado",
    DELETED = "Eliminado"