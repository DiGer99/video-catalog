from pydantic import BaseModel


class FilmBase(BaseModel):
    id: int
    name: str
    description: str


class FilmModel(FilmBase):
    rating: int
