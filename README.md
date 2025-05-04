# Proyecto EndPoint
El proyecto consiste básicamente en subir nuestra base de datos MySQL y gestionarla mediante una interfaz gráfica usando phpMyAdmin, además de conectarla con nuestra API desarrollada con FastAPI.<br>
Los pueros locales usados fueron los puertos:
  - http://localhost:8081/     Usado para phpmyAdmin
  - http://localhost:8083/     Usado nuestra API (donde se realizan las consultas)

<br>Se elaboraron 12 consultas divididas en:<br>
  - 6 Consultas con SQL, visualizadas en formato JSON desde el localhost de la API
  - 3 Consultas con Pandas, visualizadas en formato de tabla en el localhost de la API
  - 3 Consultas con Pandas y Searborn, visualizadas en formato de gráfica en el localhost de la API

## Consultas con SQL
Las consultas propuestas fueron:
  1. http://localhost:8083/idioma	
  2. http://localhost:8083/aparicionespordepartamento
  3. `http://localhost:8083/Keywords/{item_key}`
      - Donde `{item_key}` debe ser reemplazado con una palabra clave válida de la base de datos `MOVIES`
      - Por ejemplo: http://localhost:8083/Keywords/holiday
  4. `http://localhost:8083/Director/{item_dir}`
       - Donde `{item_dir}` debe ser reemplazado con un Director válida en la base de datos `MOVIES`
       - Por ejemplo: http://localhost:8083/Director/Sam%20Raimi (ojo el %20 es un espacio)
  5. `http://localhost:8083/Personaje/{item_per}`
       - Donde `{item_per}` debe ser reemplazado con un Personaje válido en la base de datos `MOVIES`
       - Por ejemplo: http://localhost:8083/Personaje/Spider-Man
  6. `http://localhost:8083/Persona/{item_orden}`
        - Donde `{item_orden}` debe ser reemplazado con orden ASC o  DESC
       - Por ejemplo: http://localhost:8083/Persona/ASC

## Consultas con Pandas
Las consultas propuestas fueron:
  1. `http://localhost:8083/TopPalabras/{item_TOP}`
      - Donde `{item_TOP}` debe ser reemplazado con un número que representa el tamaño del TOP
      - Por ejemplo: http://localhost:8083/TopPalabras/5
  3. `http://localhost:8083/TopPeores/{item_TOP}`
      - Donde `{item_TOP}` debe ser reemplazado con un número que representa el tamaño del TOP
      - Por ejemplo: http://localhost:8083/TopPeores/7
  5. `http://localhost:8083/TopCompañias/{item_TOP}`
      - Donde `{item_TOP}` debe ser reemplazado con un número que representa el tamaño del TOP
      - Por ejemplo: http://localhost:8083/TopCompañias/10

## Consultas con Pandas y Searborn
Las consultas propuestas fueron:
  1. `http://localhost:8083/TOPPelicula/{item_TOP}`
      - Donde `{item_TOP}` debe ser reemplazado con un número que representa el tamaño del TOP
      - Por ejemplo: http://localhost:8083/TOPPelicula/4
  2. `http://localhost:8083/TOPCategoria/{item_TOP}`
      - Donde `{item_TOP}` debe ser reemplazado con un número que representa el tamaño del TOP
      - Por ejemplo: http://localhost:8083/TOPCategoria/8
  3. `http://localhost:8083/TOPGenero/{item_TOP}`
      - Donde `{item_TOP}` debe ser reemplazado con un número que representa el tamaño del TOP
      - Por ejemplo: http://localhost:8083/TOPGenero/10
    
## Adicionales
Las estruturas del los directorios del Proyecto son:<br>


```plaintext
EndPoint/
├── app/                                      
│   ├── databasestar/                     # Archivos de datos en formato .csv utilizados para análisis y visualización con Pandas y Seaborn
│   ├── Dockerfile                        # Define cómo construir la imagen Docker del backend (FastAPI, dependencias, etc.)
│   ├── requirements.txt                  # Lista de dependencias Python necesarias para ejecutar la aplicación
│   ├── DB.py                             # Configura y proporciona la conexión a la base de datos MySQL usando variables de entorno
│   ├── Formato.py                        # Funcion de Formato para estilo de las tablas
│   ├── SQL.py                            # Funciones de consultasr con SQL
│   ├── Pandas.py                         # Funciones de consultas con DataFrame para generar tablas
│   ├── SeabornGrafica.py                 # Funciones de consultas con DataFrame para generar graficas
│   └── main.py                           # Archivo principal de FastAPI
├── databasestar/                         # Archivos de datos o recursos en terminacion .sql (Por si alguien quiere usarlos de forma independiente)
├── Ejemplo_Consultas(Imágenes)/          # Imágnes de ejemplos de las consutas
├── msyql/                                # Archivos de base de datos, para subida automatica
├── mysql_data/                           # Archivos de la base de datos
└── docker-compose.yml                    # Configura los contenedores (API + Base de datos)
