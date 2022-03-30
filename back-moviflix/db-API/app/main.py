from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from .routers import movies
from .routers import users
from .routers import groups


from .database.connection import connect_to_mongo,close_mongo_connection,get_database
from .database.init import connAndInit

app = FastAPI()

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


version = "v1" # Bonne pratique pour API-REST/Microservices : préfixe de version pour facilement migrer vers d'autres versions du back 
route_prefix= "/API/{}".format(version) # Les routes disponibles dans routers auront pour préfixe : /api/{version}/

app.add_event_handler("startup", connAndInit)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(movies.router,prefix= route_prefix,dependencies=[Depends(get_database)])

app.include_router(users.router,prefix= route_prefix,dependencies=[Depends(get_database)])

app.include_router(groups.router,prefix= route_prefix,dependencies=[Depends(get_database)])


