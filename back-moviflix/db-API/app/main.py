from fastapi import FastAPI,Depends
from .routers import movies
from .database.connection import connect_to_mongo,close_mongo_connection,get_database

app = FastAPI()

version = "v1" # Bonne pratique pour API-REST/Microservices : préfixe de version pour facilement migrer vers d'autres versions du back 
route_prefix= "/api/{}".format(version) # Les routes disponibles dans routers auront pour préfixe : /api/{version}/

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(movies.router,prefix= route_prefix,dependencies=[Depends(get_database)])
