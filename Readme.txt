Proyecto Individual N° 1

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
Se tomaron los archivos "steam_games.csv" y "australian_user_items.csv". 
De estos elegi las columnas que necesitaba para generar la funcion solicitaada.
columnas_steam_games = ["id", "genres", "release_date"]
columnas_australian_user_items = ["item_id", "playtime_forever"]
Luego guarde esa consulta en un nuevo archivo csv llamado "Consulta_final.csv"
Luego elimine valores nulos y tome una muestra del archivo de 20000 datos para cargar en la API.
Arme la funcion y la probe con un ejemplo.
Genere el endpoint en FastAPI y cargue alli el archivo.

8) EDA: Realice el analisis de los datos con el archivo "user_juegosEDA.csv"

9) Modelo de Aprendizaje automatico:
Tome una muestra de 10000 datos del archivo "australian_user_items.csv" y use un filtro con los datos que fueran int tanto en la columna "user_id" como "item_id" y str para la columna "item_id".
Luego guarde ese Dataframe en un archivo csv llamado "user_juegos.csv" para armar la funcion y el endpoint.
Cree la funcion "def recomendacion_usuario(usuario_id):" 
Cree un ejemplo para revisar que devuelva informacion.
Genere el Genere el endpoint en FastAPI y cargue alli el archivo.

10) Arme el render y deploy.

11) Clone el repositorio generado en la carpeta "PI MLOps - STEAM" y lo subi a mi cuenta de GitHub.




