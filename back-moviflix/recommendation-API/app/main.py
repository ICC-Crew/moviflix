from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import recommandation


app = FastAPI()

version = "v1" # Bonne pratique pour API-REST/Microservices : préfixe de version pour facilement migrer vers d'autres versions du back 
route_prefix= "/API/{}".format(version) # Les routes disponibles dans routers auront pour préfixe : /api/{version}/

# @app.get("/")
# def read_root():
#     return {"Hello": "recommendation API :)"}

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

app.include_router(recommandation.router,prefix=route_prefix)
