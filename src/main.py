from typing import Annotated
from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    status,
    Depends,
)
from schemas.films_schemas import FilmModel


app = FastAPI(title="Video Hosting")


FILMS = [
    FilmModel(
        id=1,
        name="Spider-man",
        description="About Spider-man film",
        rating=5,
    ),
    FilmModel(
        id=2,
        name="Iron man",
        description="About Iron man film",
        rating=5,
    ),
]


def get_film_from_id(film_id: int) -> FilmModel:
    movie = next(film for film in FILMS if film.id == film_id)

    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Film not found",
    )


@app.get("/")
def read_root(
    request: Request,
):
    url_docs = request.url.replace(
        path="docs",
        query={},
    )
    return {
        "message": "index page",
        "url": str(url_docs),
    }


@app.get(
    "/films/{film_id:int}/",
    response_model=FilmModel,
)
def get_film_from_id_view(
    film: Annotated[
        FilmModel,
        Depends(get_film_from_id),
    ],
):
    return film


@app.get(
    "/films/",
    response_model=list[FilmModel],
)
def get_film_from_id():
    return FILMS
