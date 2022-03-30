from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from .routers import movies
from .routers import users
from .routers import groups
import logging
from logging.config import dictConfig

loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
print("Available loggers: ")
print(loggers)

for logg in loggers:
    print(f"{logg} : {logg.handlers}")

local_logger = logging.getLogger("uvicorn")


logging_file = "./app/logs/fastapi_mongodb.log"
logging_level = logging.INFO
logging_format = logging.Formatter(fmt="%(levelname)s | %(asctime)s | %(name)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

logging_fh = logging.handlers.RotatingFileHandler(logging_file, maxBytes=1024, backupCount=3)
logging_fh.setLevel(logging_level)
logging_fh.setFormatter(logging_format)

root_logger = logging.getLogger()
root_logger.addHandler(logging_fh)
root_logger.setLevel(20)

from .database.connection import connect_to_mongo,close_mongo_connection,get_database
from .database.init import connAndInit

app = FastAPI()
local_logger.info("FastAPI started")

@app.on_event("startup")
async def startup_event():
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    print("Available loggers after startup: ")
    print(loggers)

    for logg in loggers:
        print(f"{logg} : {logg.handlers}")
    
    print("rootloggershandlers")
    print(root_logger.handlers)

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


