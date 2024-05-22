import pandas as pd
import numpy as np
import streamlit as st
from fastapi import FastAPI
import uvicorn

app = FastAPI()


# Debe devolver año con mas horas jugadas para dicho género
@app.get("/PlayTimeGenre/{genero}")
async def PlayTimeGenre(genero: str ):
    resultado=genero*3
    return{"Año de lanzamiento con más horas jugadas para Género X" : resultado}

@app.get("/UserForGenre/{genero}")
async def UserForGenre( genero : str ):
    return  {"Usuario con más horas jugadas para Género X" : "us213ndjss09sdf",
              "Horas jugadas":[{"Año": 2013, "Horas": 203}, {"Año": 2012, "Horas": 100}, {"Año": 2011, "Horas": 23}]}

@app.get("/UsersRecommend/{año}")
async def UsersRecommend( año : int ): 
    return [{"Puesto 1" : "X"}, {"Puesto 2" :" Y"},{"Puesto 3" : "Z"}]

@app.get("/UsersWorstDeveloper/{año}")
async def UsersWorstDeveloper( año : int ):
    return [{"Puesto 1" : "X"}, {"Puesto 2" : "Y"},{"Puesto 3" : "Z"}]

#Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista
#con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados 
#con un análisis de sentimiento como valor.
@app.get("/UsersBestDeveloper/{empresa_desarrolladora}")
async def sentiment_analysis( empresa_desarrolladora : str ):
    return {"valve" : {"Negative" : 182, "Neutral" : 120, "Positive" : 278}}