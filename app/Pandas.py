from fastapi import Response
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import os

#Consulta 1 (Top Palabras más usadas)
def get_TopPalabras(TOP):
    movie=pd.read_csv(os.path.join("/app/databasestar/movie.csv"))
    movie_keywords=pd.read_csv(os.path.join("/app/databasestar/movie_keywords.csv"))
    keyword=pd.read_csv(os.path.join("/app/databasestar/keyword.csv"))

    top_keyword=movie.merge(movie_keywords,on='movie_id').merge(keyword,on='keyword_id')
    resultado=top_keyword.groupby('keyword_name', as_index=False).size() #Ocupar el size(cuenta las filas) y devuelve columna llama size
    resultado.rename(columns={'size': 'Cantidad'}, inplace=True)
    resultado.rename(columns={'keyword_name': 'Palabra clave'}, inplace=True)
    resultado = resultado.sort_values('Cantidad', ascending=False).head(TOP)
    return resultado[['Palabra clave', 'Cantidad']]

#Consulta 2 (Top Peores Peliculas)
def get_TopPeoresPeliculas(TOP):
    movie=pd.read_csv(os.path.join("/app/databasestar/movie.csv"))
    
    top_peores = movie.sort_values('popularity', ascending=False).head(TOP)
    top_peores.rename(columns={'title': 'Pelicula'}, inplace=True)
    top_peores.rename(columns={'popularity': 'Popularidad'}, inplace=True)

    return top_peores[['Pelicula', 'Popularidad']]

#Consulta 3 (Top Compañia con más peliculas)
def get_TopCompañiaPeliculas(TOP):
    movie=pd.read_csv(os.path.join("/app/databasestar/movie.csv"))
    movie_company=pd.read_csv(os.path.join("/app/databasestar/movie_company.csv"))
    production_company=pd.read_csv(os.path.join("/app/databasestar/production_company.csv"))

    top_company=movie.merge(movie_company,on='movie_id').merge(production_company,on='company_id')

    resultado=top_company.groupby('company_name', as_index=False).size() #Ocupar el size(cuenta las filas) y devuelve columna llama size
    resultado.rename(columns={'size': 'Cantidad de Peliculas'}, inplace=True)
    resultado.rename(columns={'company_name': 'Nombre de la compañia'}, inplace=True)
    resultado = resultado.sort_values('Cantidad de Peliculas', ascending=False).head(TOP)
    return resultado[['Nombre de la compañia', 'Cantidad de Peliculas']]
