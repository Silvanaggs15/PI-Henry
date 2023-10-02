from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello"

    # Cargar los datos del archivo "Consulta_final.csv"
consulta_final = pd.read_csv("Consulta_final.csv")


@app.get("/playtime_genre/{genero}")
async def PlayTimeGenre(genero: str):
    # Filtrar los juegos relevantes por genero
    juegos_relevantes = consulta_final[consulta_final["genres"].str.contains(genero, case=False, na=False)]

    # Agrupar por anio y sumar las horas jugadas
    grouped_data = juegos_relevantes.groupby(juegos_relevantes["release_date"].str[:4])["playtime_forever"].sum().reset_index()

    if grouped_data.empty:
        return {"message": "No se encontraron datos para el genero especificado"}

    # Encontrar el anio con mas horas jugadas
    max_playtime_year = grouped_data.loc[grouped_data["playtime_forever"].idxmax()]["release_date"]

    return {"Anio de lanzamiento con mas horas jugadas para el genero": int(max_playtime_year)}



@app.get("/recomendacion/{usuario_id}")
async def obtener_recomendacion(usuario_id: int):
    recomendaciones = recomendacion_usuario(usuario_id)
    return recomendaciones

from sklearn.metrics.pairwise import cosine_similarity

def recomendacion_usuario(usuario_id):
    # Cargar el archivo "user_juegos.csv"
    df = pd.read_csv("user_juegos.csv")

    # Filtrar el DataFrame para obtener el usuario dado
    usuario = df[df['user_id'] == usuario_id]

    if usuario.empty:
        return {"message": "Usuario no encontrado"}

    # Eliminar la columna de usuario temporalmente para calcular la similitud del coseno
    df_sin_usuario = df[df['user_id'] != usuario_id]

    # Calcular la similitud del coseno entre el usuario dado y todos los demás usuarios
    similitud = cosine_similarity(usuario[['user_id', 'item_id']].values, df_sin_usuario[['user_id', 'item_id']].values)

    # Obtener los índices de los usuarios más similares
    usuarios_similares_indices = similitud[0].argsort()[-5:][::-1]

    # Obtener los juegos preferidos por los usuarios similares
    juegos_recomendados = []
    for indice in usuarios_similares_indices:
        juegos_usuario_similar = df_sin_usuario[df_sin_usuario['user_id'] == df.iloc[indice]['user_id']]['item_name'].values
        juegos_recomendados.extend(juegos_usuario_similar)

    # Filtrar juegos que el usuario ya haya jugado
    juegos_recomendados = [juego for juego in juegos_recomendados if juego not in usuario['item_name'].values]

    # Tomar los primeros 5 juegos recomendados
    juegos_recomendados = juegos_recomendados[:5]

    return {"Recomendaciones para el usuario": usuario_id, "juegos_recomendados": juegos_recomendados}

@app.get("/userxgen/{genero}")
def UserForGenre( genero : str ):
    usuario = df[df['user_id'] == usuario_id]
    return  "usuario que acumula mas horas jugadas" usuario

@app.get("/top3juegos/{usuario_id}")
def UsersRecommend( año : int ):
    return "Top 3 juegos recomendados al usuario:" usuario_id
    