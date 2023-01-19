from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from deta import Deta
import pandas as pd
import numpy as np
from limpieza import df_completo
from collections import Counter
import requests



app = FastAPI()
deta = Deta("e09vutye_zkkVKBx8pbV9QAdRCG55PeobRKoAuhQz")  # configure your Deta project 
drive = deta.Drive("images")

@app.post("/")
async def root(file: UploadFile=File(...)):
        return{"file_name": file.filename}


@app.get("/",response_class=HTMLResponse)
async def index():
    return """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PI 01 Lucas Rodriguez - Data Engineering Henry</title>
</head>
<style>
  body {  background-color: #000000;
          font-family: verdana;
          font-size: 75%;}
  h1   {  color: #cdd9e5;
          font-family: verdana;
          font-size: 250%;}
  h3   {  color: #9ACD32;
          font-family: verdana;
          font-size: 150%;}
  p    {  color: #cdd9e5;
          font-family: verdana;
          font-size: 200%;}
  
</style>
<body>
    <h1>Guía para Usuarias/os de la API</h1>
    <h1>IMPORTANTE: Los textos ponerlos entre las barras ej: https://k3ulsw.deta.dev/netflix/love </h1>
    <p> Query 1 : Cantidad de veces que aparece una palabra clave en el título de peliculas/series, por plataforma.</p>
    <h3>Ej: https://k3ulsw.deta.dev/keyword_funcion/netflix/love</h3> 
    <p>Query 2: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año</p>
    <h3>Ej: https://k3ulsw.deta.dev/get_score_count/netflix/85/2010</h3>
    <p>Query 3 : La segunda película con mayor partitura para una plataforma determinada, según el orden alfabético de los títulos..</p>
    <h3>Ej: https://k3ulsw.deta.dev/get_second_score/amazon</h3>
    <p>Query 4 : Pelicula que mas duro segun año , plataforma y tipo de duracion</p>
    <h3>Ej: https://k3ulsw.deta.dev/get_longest/netflix/min/2016</h3>
    <p>Query 5: Cantidad de series y películas por rating</p>
    <h3>Ej: https://k3ulsw.deta.dev/get_rating_count/18+</h3>
    <h1>Si luego de realizar alguna de las consultas desea volver a esta guía utilize https://k3ulsw.deta.dev/ </h1>
</body>
</html>"""

@app.get("/keyword_funcion/{plataforma}/{keyword}") #FUNCIONA
def keyword_funcion(plataforma,keyword):
    cantidad_de_keyword=df_completo.loc[df_completo['title'].str.contains(keyword)]
    tabla_id = cantidad_de_keyword.groupby(['id']).size().reset_index(name='cantidad de id')
    lista=list(plataforma)
    if lista[0] == 'a':
        plataforma = 'amazon'
        cantidad_a = tabla_id['id'].str.startswith('a').sum()
        return f' la plataforma seleccionado fue : {str(plataforma)}, y la cantidad de veces que aparece la palabra sleccionada es :{int(cantidad_a)}'
    else:
        pass
    if lista[0] == 'd':
        plataforma = 'disney'
        cantidad_d = tabla_id['id'].str.startswith('d').sum()
        return f'la plataforma seleccionado fue : {str(plataforma)}, y la cantidad de veces que aparece la palabra sleccionada es : {int(cantidad_d)}'
    else:
        pass
    if lista[0] == 'h':
        plataforma = 'hulu'
        cantidad_h = tabla_id['id'].str.startswith('h').sum()
        return f'la plataforma seleccionado fue :{str(plataforma)}, y la cantidad de veces que aparece la palabra sleccionada es : {int(cantidad_h)}'
    else:
        pass

    if lista[0] == 'n':
        plataforma = 'netflix'
        cantidad_n = tabla_id['id'].str.startswith('n').sum()
        return f'la plataforma seleccionado fue : {str(plataforma)},  y la cantidad de veces que aparece la palabra sleccionada es :{int(cantidad_n)}'
    else:
        return print('por favor ingrese una plaforma como amazon, disney,hulu o netflix muchas gracias')

@app.get("/get_score_count/{plataforma}/{point}/{anio}")#FUNCIONA
def get_score_count(plataforma:str,point:int,anio:int):
    plataformas = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
    df_temp = df_completo[(df_completo["score"]>point)&(df_completo["release_year"]==anio)&(df_completo.id.str[0] == plataformas[plataforma])&(df_completo["type"] == "movie")]
    data = df_temp.groupby(df_temp.id.str[0]).count().iloc[:,0]
    data = data.rename_axis("Cantidad").rename({v: k for k, v in plataformas.items()})
    return data.to_dict()

@app.get("/get_second_score/{plataforma}") #FUNCIONA
def get_second_score(plataforma):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
    df_temp = df_completo[(df_completo['id'].str[0] == dicc[plataforma])&(df_completo['type'] == 'movie')].sort_values(["score","title"],ascending=[False,True]).reset_index(drop=True)
    titulo = df_temp.iloc[1,2]
    score = df_temp.iloc[1,14]
    return f'{titulo}, {score}'

@app.get("/get_longest/{plataforma}/{duration_tipo}/{date}")#FUNCIONA
def get_longest(plataforma:str,duration_tipo:str,date:int):
    plataformas = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
    df_temp = df_completo[(df_completo['id'].str[0] == plataformas[plataforma])&(df_completo['release_year']==date)&(df_completo['duration_type']==duration_tipo)&\
          (df_completo['type']=='movie')].sort_values(['duration_int'], ascending=False).reset_index(drop=True)[["title","duration_int","duration_type"]].iloc[0,:]
    return df_temp.to_dict()

@app.get("/get_rating_count/{rating}") #FUNCIONA
def get_rating_count(rating):
    
    cantidad_rating= df_completo[df_completo['rating']== rating]

    return  f'{rating,(len(cantidad_rating))}'

