from fastapi import Response
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import os

#Consulta 1 (Top peliculas con mayor números de fondos reacudados)
def get_TopPeliculas(TOP):  
    movie=pd.read_csv(os.path.join("/app/databasestar/movie.csv"))

    top_movies=movie.sort_values(by='revenue',ascending=False).head(TOP)  #Consulta
    plt.figure(figsize=(max(10,len(top_movies)*0.8),6)) #La figura a crear con ancho dinamico(dependiedo de top) controlando su tamaño
    grafica=sns.barplot(x='title', y='revenue', data=top_movies, palette='deep') #Genera el grafico

    plt.title(f"TOP {TOP} peliculas con mayor recaudación")
    plt.ylabel("RECAUDACIONES (EN MILLONES USD)")
    plt.xlabel("PELICULAS")
    grafica.set_xticklabels(grafica.get_xticklabels(), rotation=10, ha='right') #Rotacion de etiqueta
    plt.tight_layout() #Funcion que ajusta automaticamnete espacio entre  los nombre y titulos evitando que se corten

    buffer=BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return Response(content=buffer.read(), media_type="image/png")

#Consulta 2 (Top generos de peliculas)
def get_TopGeneros(TOP):
    if TOP > 20:
        return "El número dado excede el número de generos disponibles"

    movie=pd.read_csv(os.path.join("/app/databasestar/movie.csv"))
    movie_genre=pd.read_csv(os.path.join("/app/databasestar/movie_genres.csv"))
    genre=pd.read_csv(os.path.join("/app/databasestar/genre.csv"))
    consulta=movie.merge(movie_genre,left_on='movie_id',right_on='movie_id').merge(genre,left_on='genre_id',right_on='genre_id')
    resultado=consulta['genre_name'].value_counts()
    top_generos=resultado.sort_values(ascending=False).head(TOP) #Consulta

    plt.figure(figsize=(19,13)) #La figura a crear con ancho predeterminado
    grafica=plt.pie(top_generos.values, autopct=lambda p: f'{p:.1f}%', startangle=150, colors=plt.cm.Paired.colors) # Puedes dejar los porcentajes si lo deseas
    plt.legend([f"{genre} ({count})" for genre, count in top_generos.items()], loc="best")
    plt.axis('equal') #Necesario para relacion tabla con gráfica
    plt.title(f"TOP {TOP} generos de peliculas")
    plt.tight_layout() #Funcion que ajusta automaticamnete espacio entre  los nombre y titulos evitando que se corten
    
    buffer=BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return Response(content=buffer.read(), media_type="image/png")

#Consulta 3 (Top Popularidad Peliculas con generos por pelicula)
def get_TopPopularidad(TOP):
    movie=pd.read_csv(os.path.join("/app/databasestar/movie.csv"))
    movie_cast=pd.read_csv(os.path.join("/app/databasestar/movie_cast.csv"))
    gender=pd.read_csv(os.path.join("/app/databasestar/gender.csv"))

    consulta=movie.merge(movie_cast, on='movie_id').merge(gender,on='gender_id')
    resultado=consulta.groupby('title', as_index=False).agg(Popularidad=('popularity','max'),Masculino=('gender_id',lambda x:(x==2).sum()),
    Femenino=('gender_id',lambda x:(x==1).sum()),Indefinido=('gender_id',lambda x:(x==0).sum()))
    top_generos=resultado.sort_values(by='Popularidad', ascending=False).head(TOP) #Consulta
    top_Popularidad=top_generos.melt(id_vars='title', value_vars=['Masculino', 'Femenino', 'Indefinido'], var_name='Género', value_name='Cantidad') #Convertir datos a entrada de grafica

    fig, ax = plt.subplots(figsize=(19, 13)) #La figura a crear con ancho predeterminado
    ax.set_xlabel("Película")
    ax.set_ylabel("Cantidad")
    # Create a custom cubehelix palette
    # Create a diverging palette with a darker center
    dark_center_div = sns.diverging_palette(150, 275, s=80, l=55, n=9, center="dark")
    sns.barplot(data=top_Popularidad, x='title', y='Cantidad', hue='Género',palette=dark_center_div)
    plt.xticks(rotation=15, ha='right')
    plt.title(f"TOP {TOP} Popularidad de Peliculas con cantidad de participacion del genero de las personas")
    plt.tight_layout() #Funcion que ajusta automaticamnete espacio entre  los nombre y titulos evitando que se corten
    
    buffer=BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return Response(content=buffer.read(), media_type="image/png")