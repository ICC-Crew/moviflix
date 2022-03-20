import requests
import asyncio
from fastapi import Depends
from ..models.movie import MovieIns
from ..crud.movies import add_movie
from .connection import get_database,connect_to_mongo

def get_top_250_movies():
    req = requests.get("https://imdb-api.com/en/API/Top250Movies/k_9pfhf380")
    return req.json()["items"]

def json_to_movie(movieJSON):
    movie = MovieIns(
        fetched=0,
        imdbID = movieJSON["id"],
        title = movieJSON["title"]
    )
    return movie

def json_to_movies(moviesJSON):
    movies = []
    for item in moviesJSON:
        movie = json_to_movie(item)
        movies.append(movie)
    return movies

async def add_to_db(movies):
    database = await get_database()
    await asyncio.gather(*[add_movie(database,movie) for movie in movies])


async def initDB():
    top250movies = get_top_250_movies()
    movies = json_to_movies(top250movies)
    await add_to_db(movies)

async def connAndInit():
    await connect_to_mongo()
    #await initDB()