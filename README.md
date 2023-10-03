PROYECTO INDIVIDUAL N° 1:
Este es mi proyecto personal de Machine Learning Operations (MLOPS).

Descripcion del proyecto
En este proyecto, asumí el rol de un Data Scientist en Steam, una plataforma de videojuegos.
El objetivo principal fue crear un sistema de recomendación como mi primer modelo de Machine Learning para solucionar un problema de negocio.Steam me encargó crear un sistema de recomendación de videojuegos para usuarios. Al revisar los datos disponibles, encontré que la calidad de los mismos era muy baja y no estaban listos para su procesamiento. Esto implicó realizar un trabajo de Data Engineering para transformar los datos y obtener un Minimum Viable Product (MVP) para el cierre del proyecto.

El proyecto abordó el ciclo de vida completo de un proyecto de Machine Learning, desde el tratamiento de datos hasta el entrenamiento y mantenimiento del modelo de ML. Además, se desarrolló una API utilizando el framework FastAPI para disponibilizar los datos de la plataforma y se implementaron diferentes consultas para interactuar. También realicé un análisis exploratorio de datos (EDA) para investigar las relaciones entre las variables del dataset, identificar outliers o anomalías, y descubrir patrones interesantes que podrían ser útiles en análisis posteriores. A su vez, desarrollé un sistema de recomendación basado en videos juegos similares utilizando técnicas de cálculo de similitud.

Procedimiento:
Durante el desarrollo del proyecto, se llevaron a cabo las siguientes tareas: Transformaciones de datos (ETL):
1) Descomprimi los archivos gz.
2) Realice la transformacion de los datos eliminando los que no necesitaba ya que eran archivos muy pesados.
3) Comence por el archivo "steam_games":
- Lo converti en dataframe para que sea mas facil trabajar sobre el archivo
- Elimine las columnas que no necesitaba
- Elimine los nulos
- Guarde los cambios en un archivo csv: "steam_games.csv"
4) Abri el archivo users.items.json:
- Lo descomprimi en un json "australian_users_items.json":
- Lo converti en dataframe para para que sea mas facil trabajar sobre el archivo
- Elimine las columnas que no necesitaba
- Desanide la columna items para obtener las columnas internas, separadas y poder trabajar con ellas
- Elimine los nulos
- Guarde los cambios en un archivo csv: "australian_user_items.csv.csv"
5) Abri el archivo user_reviews.json.gz:
- Lo descomprimi en un json "australian_user_reviews.json"
- Lo converti en dataframe para para que sea mas facil trabajar sobre el archivo
- Elimine las columnas que no necesitaba
- Elimine los nulos
- Guarde los cambios en un archivo csv: "australian_user_reviews.csv"

6) Analisis de Sentimiento:
Realice el analisis de sentimiento con el archivo "australian_user_reviews".aplicando los valores 0 para reseñas malas, 1 para reseñas neutrales y 2 para reseñas positivas. A su vez, se definio colocar valor 1 para reseñas ausentes.
Luego se aplicó la función a la columna 'user_reviews.review' y crear la nueva columna 'sentiment_analysis'.
Se eliminó la columna original 'user_reviews.review' ya que no se necesitaba mas.
Se guardó el DataFrame actualizado en un nuevo archivo CSV llamado "australian_user_reviews_with_sentiment.csv".

7) Desarrollo API:
Se desarrolló una API utilizando el framework FastAPI para disponibilizar los datos de la plataforma. Se implementaron las siguientes consultas:
Se tomaron los archivos "steam_games.csv" y "australian_user_items.csv". 
De estos elegi las columnas que necesitaba para generar la funcion solicitaada.
columnas_steam_games = ["id", "genres", "release_date"]
columnas_australian_user_items = ["item_id", "playtime_forever"]
Luego guarde esa consulta en un nuevo archivo csv llamado "Consulta_final.csv"
Luego elimine valores nulos y tome una muestra del archivo de 20000 datos para cargar en la API.
Arme la funcion y la probe con un ejemplo.
Genere el endpoint en FastAPI y cargue alli el archivo.

8) Deployment: 
El proyecto se deployó utilizando el servicio Render para que la API sea consumible desde la web. Puedes acceder a la API y consultar la documentación en el siguiente enlace:https://silvana-deploy.onrender.com

9) EDA: 
Se realizó un análisis exploratorio de datos (EDA) con el archivo "user_juegos.csv", para investigar las relaciones entre las variables del dataset y descubrir patrones. Se utilizaron técnicas de visualización y se generaron gráficas. 

10) Modelo de Aprendizaje automatico:
Se desarrolló un sistema de recomendación "user-item" basado en juegos similares. Se calculó la similitud del coseno entre un usuario dado y todos los demas usuarios. Luego se obtuvo los índices de los usuarios similares, para que a partir de esa informacion se pudiera obtener los juegos preferidos por los usuarios similares. Se aplicó un filtro de juegos que el usuario ya hubiera jugado para poder así devolver 5 juegos recomendados para dicho usuario. Esta función , llamada "def recomendacion_usuario( id de usuario ):", fue implementada en la API.
Procedimiento del MLA:
Tome una muestra de 10000 datos del archivo "australian_user_items.csv" y use un filtro con los datos que fueran int tanto en la columna "user_id" como "item_id" y str para la columna "item_id".
Luego guarde ese Dataframe en un archivo csv llamado "user_juegos.csv" para armar la funcion y el endpoint.
Cree la funcion "def recomendacion_usuario(usuario_id):" 
Cree un ejemplo para revisar que devuelva informacion.
Genere el Genere el endpoint en FastAPI y cargue alli el archivo.

11) Repositorio y archivos relevantes:
En el repositorio de GitHub "https://github.com/Silvanaggs15/PI-Henry", puedes encontrar los siguientes archivos relevantes:

*Proyecto Individual: En este ipynb se encuentran:
- ETL: El archivo ETL contiene el código y los detalles de las transformaciones de datos realizadas en el proyecto.
- Los códigos correspondientes a las funciones implementadas para los endpoints de la API. Cada función se asocia a una consulta específica mencionada previamente.

*EDA: El archivo EDA contiene el código y las visualizaciones generadas durante el análisis exploratorio de datos. Aquí se exploraron las relaciones entre las variables del dataset, se identificaron outliers o anomalías y se buscaron patrones interesantes.

*Además de estos archivos, el repositorio también puede contener otros recursos relevantes como datos adicionales, documentación adicional o notebooks utilizados en el proceso de desarrollo.

12) Conclusiones:
En este proyecto personal de Machine Learning, asumí el rol de un Data Scientist y trabajé en la creación de un sistema de recomendación de juegos para una plataforma de juegos. Realicé tareas de Data Engineering, desarrollé una API utilizando FastAPI, realicé análisis exploratorio de datos (EDA) y creé un sistema de recomendación basado en usuarios similares.

A lo largo del proyecto, adquirí experiencia en el manejo y transformación de datos, implementé consultas en una API, realicé análisis exploratorio de datos y utilicé técnicas de cálculo de similitud para recomendar juegos. El despliegue de la API permitió que los departamentos de Analytics y Machine Learning pudieran consumir los datos y utilizar el sistema de recomendación en sus procesos.

El repositorio de GitHub "https://github.com/Silvanaggs15/PI-Henry" contiene todos los archivos relevantes y el código desarrollado durante el proyecto. También puedes acceder a la API y consultar la documentación en el siguiente enlace: https://silvana-deploy.onrender.com

¡Gracias por revisar mi proyecto!


