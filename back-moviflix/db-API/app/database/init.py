import requests
import asyncio
from fastapi import Depends
from ..models.movie import MovieIns, UpdatedMovie
from ..models.actor import Actor
from ..crud.movies import add_movie,fetch_incomplete_movies,update_movie
from .connection import get_database,connect_to_mongo

apiKey = "k_4k4scm18"

def get_top_250_movies(apikey):
    req = requests.get(f"https://imdb-api.com/fr/API/Top250Movies/{apikey}")
    return req.json()["items"]

def get_movie(apikey,movieIdImdb):
    link = f"https://imdb-api.com/fr/API/Title/{apikey}/{movieIdImdb}/FullActor,Posters,Images,Trailer"
    req = requests.get(link) 
    return req.json()

def json_to_updated_movie(movieJSON):
    jsonGenres = movieJSON["genreList"]
    jsonDirectors = movieJSON["directorList"]
    jsonPicturesUrl = movieJSON["images"]["items"]
    jsonActors = movieJSON["actorList"]
    genresCustom = []
    directorsCustom = []
    picturesUrlCustom = []
    actorsCustom = []

    for genre in jsonGenres:
        genresCustom.append(genre["value"])

    for director in jsonDirectors:
        directorsCustom.append(director["name"])

    for pictureUrl in jsonPicturesUrl:
        picturesUrlCustom.append(pictureUrl["image"])

    for jsonActor in jsonActors:
        actor = Actor(
                name=jsonActor["name"],
                asCharacter=jsonActor["asCharacter"],
                imgActorUrl=jsonActor["image"]
                )
        actorsCustom.append(actor)


    updatedMovie = UpdatedMovie(
        duration = movieJSON["runtimeMins"],
        movieCoverUrl =movieJSON["image"],
        genres = genresCustom,
        directors = directorsCustom,
        year = movieJSON["year"],
        synopsis = movieJSON["plotLocal"],
        trailerUrl = movieJSON["trailer"]["linkEmbed"],
        moviePicturesURL = picturesUrlCustom[0:10],
        actors = actorsCustom[0:10]
    )
    return updatedMovie

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

def json_to_ids(moviesJSON):
    movieImdbIds = []
    for item in moviesJSON:
        title= (str(item["_id"]),item["imdbID"])
        movieImdbIds.append(title)
    return movieImdbIds

async def get_incomplete_movies():
    database = await get_database()
    result = await fetch_incomplete_movies(database)
    return result

async def get_imdb_info(movieIds):
    moviesToUpdate = [(get_movie(apiKey,imdbTitle)) for (id,imdbTitle) in movieIds]
    result = map(json_to_updated_movie,moviesToUpdate)
    return list(result)
    


async def update_incomplete_movies(number):
    database = await get_database()
    incompleteMovies =  await get_incomplete_movies()
    incompleteMovieIds = json_to_ids(incompleteMovies)[0:number]
    imdbInfos = await get_imdb_info(incompleteMovieIds)
    await asyncio.gather(*[update_movie(database,imdbInfos[i],incompleteMovieIds[i][0])for i in range(len(incompleteMovieIds))])

async def add_to_db(movies):
    database = await get_database()
    await asyncio.gather(*[add_movie(database,movie) for movie in movies])


async def initDB():
    top250movies = get_top_250_movies(apiKey)
    movies = json_to_movies(top250movies)
    await add_to_db(movies)

async def connAndInit():
    await connect_to_mongo()
    #await update_incomplete_movies(25)    
    #print(json_to_updated_movie(get_movie(apiKey,movieTest)))
    #await initDB() ## LIGNE A DECOMMENTER UNE FOIS POUR L'INITIALISATION DE LA DB