from DB import get_connection
import mysql.connector 

#Consulta 1
def get_IdiomaAsignado(): #Catálogo completo de títulos, tengan o no idioma asignado.
    try:
        conn = get_connection() #Establecer la conexión con la base de datos
        cursor = conn.cursor(dictionary=True) #Crear un cursos para ejecutar consulta

        cursor.execute(
            "SELECT M.movie_id, M.title, L.language_name, LR.language_role "  
            "FROM movie M " 
            "LEFT JOIN movie_languages ML on M.movie_id = ML.movie_id "
            "LEFT JOIN language L on ML.language_id = L.language_id " 
            "LEFT JOIN language_role  LR on ML.language_role_id = LR.role_id;"
        ) #Ejecutar la consulta SQL para resultados
        
        resultados = cursor.fetchall()  #Obtener todos los resultados de la consulta
        cursor.close()  #Cerrar el cursor y la conexión a la base de datos
        conn.close()

        return {"Titulos con su idiomas asignados": resultados} #Retorna resultados

    except mysql.connector.Error as err:
        return {"Error": str(err), "Details": str(err.__dict__)}  # Agregar más detalles del error

#Consulta 2
def get_AparicioneCreWDepartament(): #Personas con mayor numero de apariciones en crew por departamento.
    try:
        conn = get_connection() #Establecer la conexión con la base de datos
        cursor = conn.cursor(dictionary=True) #Crear un cursos para ejecutar consulta

        cursor.execute(
            "SELECT D.department_name Nombre_Apartamento, P.person_name Nombre_Persona, A.apariciones "

            "FROM (SELECT  department_id,  person_id, COUNT(*) apariciones "
  	               "FROM movie_crew "
                   "GROUP BY department_id, person_id) A "
      
            "JOIN (SELECT department_id, MAX(apariciones) AS max_apariciones "
                  "FROM (SELECT department_id, person_id, COUNT(*) AS apariciones "
      		            "FROM movie_crew "
      		            "GROUP BY department_id, person_id) CAPP "
                  "GROUP BY department_id) AS Mx ON A.department_id = Mx.department_id AND A.apariciones= Mx.max_apariciones "
      
            "JOIN department D ON A.department_id = D.department_id "
            "JOIN person P ON A.person_id = P.person_id "
            "GROUP BY D.department_name, P.person_name,A.apariciones "
            "ORDER BY D.department_name"
        ) #Ejecutar la consulta SQL para resultados
        
        resultado= cursor.fetchall()  #Obtener todos los resultados de la consulta
        cursor.close()  #Cerrar el cursor y la conexión a la base de datos
        conn.close()

        return {"Personas con mayor numero de apariciones en crew por departamento": resultado} #Retorna resultados

    except mysql.connector.Error as err:
        return {"Error": str(err), "Details": str(err.__dict__)}  # Agregar más detalles del error
    
#Consulta 3
def get_RelacionPeliculasKey(key): #Catálogo  de títulos, relacionado con la palabra "key"
    try:
        conn = get_connection() #Establecer la conexión con la base de datos
        cursor = conn.cursor(dictionary=True) #Crear un cursos para ejecutar consulta

        cursor.execute(
            "SELECT M.title,K.keyword_name "
            "FROM movie M "
            "RIGHT JOIN movie_keywords MK on M.movie_id=MK.movie_id "
            "RIGHT JOIN keyword K on MK.keyword_id= K.keyword_id "
            "WHERE K.keyword_name = %s; ",(key,)   
        ) #Ejecutar la consulta SQL para resultados
        
        resultados = cursor.fetchall()  #Obtener todos los resultados de la consulta
        cursor.close()  #Cerrar el cursor y la conexión a la base de datos
        conn.close()

        return {"Titulos relacionados con la palabra " + key : resultados} #Retorna resultados

    except mysql.connector.Error as err:
        return {"Error": str(err), "Details": str(err.__dict__)}  # Agregar más detalles del error

#Consulta 4
def get_RelacionPeliculasDirector(Director): #Catálogo  de títulos, relacionado con la palabra "director"
    try:
        conn = get_connection() #Establecer la conexión con la base de datos
        cursor = conn.cursor(dictionary=True) #Crear un cursos para ejecutar consulta

        cursor.execute(
            "SELECT M.title, P.person_name "
            "FROM movie M "
            "INNER JOIN movie_crew MC ON M.movie_id = MC.movie_id "
            "INNER JOIN person P ON P.person_id=MC.person_id " 
            "WHERE MC.job = 'Director' AND  P.person_name = %s; " ,(Director,)
        ) #Ejecutar la consulta SQL para resultados
        
        resultados = cursor.fetchall()  #Obtener todos los resultados de la consulta
        cursor.close()  #Cerrar el cursor y la conexión a la base de datos
        conn.close()

        return {"Las peliculas de " + Director + " son " : resultados} #Retorna resultados

    except mysql.connector.Error as err:
        return {"Error": str(err), "Details": str(err.__dict__)}  # Agregar más detalles del error


#Consulta 5
def get_RelacionPeliculasPersonajePrincipal(Pelicula): #Personaje Principal dependiendo de "Pelicula"
    try:
        conn = get_connection() #Establecer la conexión con la base de datos
        cursor = conn.cursor(dictionary=True) #Crear un cursos para ejecutar consulta

        cursor.execute(
            "SELECT M.movie_id, M.title, P.person_name, MC.character_name "
            "FROM movie M "
            "INNER JOIN movie_cast MC ON M.movie_id = MC.movie_id "
            "INNER JOIN person P ON P.person_id = MC.person_id "
            "WHERE MC.cast_order = 0 AND M.title = %s; " ,(Pelicula, )
        ) #Ejecutar la consulta SQL para resultados
        
        resultados = cursor.fetchall()  #Obtener todos los resultados de la consulta
        cursor.close()  #Cerrar el cursor y la conexión a la base de datos
        conn.close()

        return {"El personaje principal  de " + Pelicula + " es" : resultados} #Retorna resultados

    except mysql.connector.Error as err:
        return {"Error": str(err), "Details": str(err.__dict__)}  # Agregar más detalles del error

#Consulta 6
def get_GeneroPersonas(Orden): #Personas con su genero dependiendo de se "Genero"
    try:
        conn = get_connection() #Establecer la conexión con la base de datos
        cursor = conn.cursor(dictionary=True) #Crear un cursos para ejecutar consulta

        cursor.execute(
            "SELECT M.movie_id, M.title, P.person_name,MC.character_name, G.gender "
            "FROM movie M "
            "LEFT JOIN movie_cast MC ON MC.movie_id = M.movie_id "
            "LEFT JOIN gender G ON G.gender_id = MC.gender_id "
            "JOIN person P ON P.person_id = MC.person_id "
            f"ORDER BY M.movie_id {Orden} "
            "LIMIT 10;" 
        ) #Ejecutar la consulta SQL para resultados
        
        resultados = cursor.fetchall()  #Obtener todos los resultados de la consulta
        cursor.close()  #Cerrar el cursor y la conexión a la base de datos
        conn.close()

        return {"El genero de forma" + Orden  + " es " : resultados} #Retorna resultados

    except mysql.connector.Error as err:
        return {"Error": str(err), "Details": str(err.__dict__)}  # Agregar más detalles del error
    