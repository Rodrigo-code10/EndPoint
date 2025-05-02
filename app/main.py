from fastapi import FastAPI 
#Importe de funciones
from SQL import *
from Pandas import *
from SeabornGrafica import *
from Formato import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

#Consultas SLQ (6)    SQL.py
@app.get("/idioma") 
def ConIdioma():
    return get_IdiomaAsignado()

@app.get("/aparicionespordepartamento") 
def AparicionPorDepartementoMovieCrew():
    return get_AparicioneCreWDepartament()

@app.get("/Keywords/{item_key}") 
def BusKey(item_key: str):
    try:
        return get_RelacionPeliculasKey(item_key)
    except:
        return {'Error': 'nodata'}

@app.get("/Director/{item_dir}") 
def RelacionPeliculasDirector(item_dir: str):
    try:
        return get_RelacionPeliculasDirector(item_dir)
    except :
        return {'Error': 'nodata'}

@app.get("/Personaje/{item_per}") 
def RelacionPersonajePrincipal(item_per: str):
    try:
        return get_RelacionPeliculasPersonajePrincipal(item_per)
    except:
        return {'Error': 'nodata'}
    
@app.get("/Persona/{item_orden}") 
def PersonasGeneroOrden(item_orden: str):
    try:
        if item_orden not in ['ASC', 'DESC']:  # Validar que el orden sea ASC o DESC
            return {"Error": "Orden debe ser 'ASC' o 'DESC'"}
        return get_GeneroPersonas(item_orden)
    except:
        return {'Error': 'nodata'}



#Consultas Pandas (JSON) (3)  Pandas.py

@app.get("/TopPalabras/{item_TOP}") 
def PalabrasMasUsadas(item_TOP: int):
    try:
        tabla= get_TopPalabras(item_TOP)
        titulo=f"Top {item_TOP} Palabras Más Usadas"
        return TablaFormato(tabla, titulo)
    except:
        return {'Error': 'nodata'}

@app.get("/TopPeores/{item_TOP}") 
def PeroresPeliculasPopularidad(item_TOP: int):
    try:
        tabla= get_TopPeoresPeliculas(item_TOP)
        titulo=f"Top {item_TOP} Peores peliculas por Popularidad"
        return TablaFormato(tabla, titulo)
    except:
        return {'Error': 'nodata'}

@app.get("/TopCompañias/{item_TOP}") 
def CompañiasConMasPeliculas(item_TOP: int):
    try:
        tabla = get_TopCompañiaPeliculas(item_TOP)
        titulo=f"Top {item_TOP} Compañias de Peliculas"
        return TablaFormato(tabla, titulo)
    except:
        return {'Error': 'nodata'}


#Consultas Pandas (Seaborn/graficas) (3)  SeabornGrafica.py
@app.get("/TOPPelicula/{item_TOP}") 
async def TOPPeliculasMayorRecaudacion(item_TOP: int):
    try:
        return get_TopPeliculas(item_TOP)
    except:
        return {"Error": "nodata"}
     
@app.get("/TOPCategoria/{item_TOP}") 
async def TOPGenerosDePeliculas(item_TOP: int):
    try:
        return get_TopGeneros(item_TOP)
    except:
        return {"Error": "nodata"}

@app.get("/TOPGenero/{item_TOP}") 
async def get_TopPoularidad_Gender(item_TOP: int):
    try:
        return get_TopPopularidad(item_TOP)
    except:
        return {"Error": "nodata"}
    