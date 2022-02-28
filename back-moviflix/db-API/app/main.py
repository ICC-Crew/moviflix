from fastapi import FastAPI,Depends
from .routers import movies
from .database import connection

app = FastAPI()

version = "v1" # Bonne pratique pour API-REST/Microservices : préfixe de version pour facilement migrer vers d'autres versions du back 
route_prefix= "/api/{}".format(version) # Les routes disponibles dans routers auront pour préfixe : /api/{version}/


app.include_router(movies.router,prefix= route_prefix,dependencies=[Depends(connection.get_db)])

@app.get("/")
async def root():
    return {"message": "Welcome to DB-API :) !"}
