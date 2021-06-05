from os import environ as env # Import a library called OS from which we import environ so we do not need to hardcode values (the mongo srv string)
from pymongo import MongoClient # Import a library pymongo from which we import class MongoClient


def connect(): # Define a function called connect, which will connect to the database and later used in other files.
    """ Connect to MongoDB using srv string (which is stored as an environmental variable). """ # Docstring
    return MongoClient(env.get("MONGODB_CONNECTION_STRING")) # creates a new instance from mongo client and returns the new instance of MongoClient

#env.get("MONGODB_CONNECTION_STRING") == mongodb+srv://tom:parole123@banking-app-python.zfwkg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority