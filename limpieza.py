import pandas as pd
import numpy as np
from collections import Counter


#Comenzamos con la carga de los data set para proceseder con la limpieza de los datos
url_amazon = 'https://raw.githubusercontent.com/lucasrdrz/PI-01/main/amazon_prime_titles-score.csv'
amazon = pd.read_csv(url_amazon)
url_disney= 'https://raw.githubusercontent.com/lucasrdrz/PI-01/main/disney_plus_titles-score.csv'
disney = pd.read_csv(url_disney)
url_hulu = 'https://raw.githubusercontent.com/lucasrdrz/PI-01/main/hulu_titles-score%20(2)%20copy.csv'
hulu = pd.read_csv(url_hulu)
url_netflix = 'https://raw.githubusercontent.com/lucasrdrz/PI-01/main/netflix_titles-score.csv'
netflix = pd.read_csv(url_netflix)


#Creamos las columna ID con la letra A de amazon seguido del show_id
amazon['show_id'] = amazon['show_id'].astype('str')
amazon['id'] = 'a' + amazon['show_id']
#Creamos las columna id con la letra d de disney seguido del show_id
disney['show_id'] = disney['show_id'].astype('str')
disney['id'] = 'd' + disney['show_id']
#Creamos las columna id con la letra h de hulu seguido del show_id
hulu['show_id'] = hulu['show_id'].astype('str')
hulu['id'] = 'h' + hulu['show_id']
#Creamos las columna id con la letra n de netflix seguido del show_id\
netflix['show_id'] = netflix['show_id'].astype('str')
netflix['id'] = 'n' + netflix['show_id']

## Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

#cambiamos los valores NaN en la columna Rating por "G" y con el .sum() verificamos que no tengamos nulos en la columna
amazon['rating'].fillna("G", inplace= True)
amazon['rating'].isnull().sum()
#cambiamos los valores NaN en la columna Rating por "G"
disney['rating'].fillna("G", inplace= True)
#cambiamos los valores NaN en la columna Rating por "G"
hulu['rating'].fillna("G", inplace= True)
#cambiamos los valores NaN en la columna Rating por "G"
netflix['rating'].fillna("G", inplace= True)


##  De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

#Procedemos a cambiar el formato de la fecha para que nos quede AAA-mm-dd
amazon['date_added'] = pd.to_datetime(amazon['date_added'], infer_datetime_format=True, errors='coerce')
#Procedemos a cambiar el formato de la fecha para que nos quede AAA-mm-dd
disney['date_added'] = pd.to_datetime(disney['date_added'], infer_datetime_format=True, errors='coerce')
#Procedemos a cambiar el formato de la fecha para que nos quede AAA-mm-dd
hulu['date_added'] = pd.to_datetime(hulu['date_added'], infer_datetime_format=True, errors='coerce')
#Procedemos a cambiar el formato de la fecha para que nos quede AAA-mm-dd
netflix['date_added'] = pd.to_datetime(netflix['date_added'], infer_datetime_format=True, errors='coerce')

## El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer 
## y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

#Lo que procedemos a hacer es separar el duration_type en la parte entera y la parte string para poder utilizarlo 
amazon[['duration_int', 'duration_type']] = amazon['duration'].str.split(' ', n=-1, expand=True, regex=None)
amazon = amazon[amazon.columns[:10].tolist() + ['duration_int', 'duration_type'] + amazon.columns[10:-2].tolist()]
#Lo que procedemos a hacer es separar el duration_type en la parte entera y la parte string para poder utilizarlo 
disney[['duration_int', 'duration_type']] = disney['duration'].str.split(' ', n=-1, expand=True, regex=None)
disney = disney[disney.columns[:10].tolist() + ['duration_int', 'duration_type'] + disney.columns[10:-2].tolist()]
#Lo que procedemos a hacer es separar el duration_type en la parte entera y la parte string para poder utilizarlo 
hulu[['duration_int', 'duration_type']] = hulu['duration'].str.split(' ', n=-1, expand=True, regex=None)
hulu = hulu[hulu.columns[:10].tolist() + ['duration_int', 'duration_type'] + hulu.columns[10:-2].tolist()]
#Lo que procedemos a hacer es separar el duration_type en la parte entera y la parte string para poder utilizarlo 
netflix[['duration_int', 'duration_type']] = netflix['duration'].str.split(' ', n=-1, expand=True, regex=None)
netflix = netflix[netflix.columns[:10].tolist() + ['duration_int', 'duration_type'] + netflix.columns[10:-2].tolist()]
\
#Pasamos los Seasons plural a singular(season)
amazon['duration_type'] = amazon['duration_type'].replace('Seasons' , 'season')
#Pasamos los Seasons plural a singular(season)
disney['duration_type'] = disney['duration_type'].replace('Seasons' , 'season')
#Pasamos los Seasons plural a singular(season)
hulu['duration_type'] = hulu['duration_type'].replace('Seasons' , 'season')
#Pasamos los Seasons plural a singular(season)
netflix['duration_type'] = netflix['duration_type'].replace('Seasons' , 'season')

#Cambiamos todos los textos de las columnas a lower(minuscula)
amazon['type'] = amazon['type'].str.lower()
amazon['title'] = amazon['title'].str.lower()
amazon['director'] = amazon['director'].str.lower()
amazon['cast'] = amazon['cast'].str.lower()
amazon['country'] = amazon['country'].str.lower()
amazon['rating'] = amazon['rating'].str.lower()
amazon['listed_in'] = amazon['listed_in'].str.lower()
amazon['description'] = amazon['description'].str.lower()
amazon['duration_type'] = amazon ['duration_type'].str.lower()
#Cambiamos todos los textos de las columnas a lower(minuscula)
disney['type'] = disney['type'].str.lower()
disney['title'] = disney['title'].str.lower()
disney['director'] = disney['director'].str.lower()
disney['cast'] = disney['cast'].str.lower()
disney['country'] = disney['country'].str.lower()
disney['rating'] = disney['rating'].str.lower()
disney['listed_in'] = disney['listed_in'].str.lower()
disney['description'] = disney['description'].str.lower()
disney['duration_type'] = disney['duration_type'].str.lower()
#Cambiamos todos los textos de las columnas a lower(minuscula)
hulu['type'] = hulu['type'].str.lower()
hulu['title'] = hulu['title'].str.lower()
hulu['director'] = hulu['director'].str.lower()
hulu['country'] = hulu['country'].str.lower()
hulu['rating'] = hulu['rating'].str.lower()
hulu['listed_in'] = hulu['listed_in'].str.lower()
hulu['description'] = hulu['description'].str.lower()
#hulu['cast'] = hulu['cast'].str.lower() da error por los NaN
hulu['duration_type'] = hulu['duration_type'].str.lower()
#Cambiamos todos los textos de las columnas a lower(minuscula)
netflix['type'] = netflix['type'].str.lower()
netflix['title'] = netflix['title'].str.lower()
netflix['director'] = netflix['director'].str.lower()
netflix['cast'] = netflix['cast'].str.lower()
netflix['country'] = netflix['country'].str.lower()
netflix['rating'] = netflix['rating'].str.lower()
netflix['listed_in'] = netflix['listed_in'].str.lower()
netflix['description'] = netflix['description'].str.lower()
netflix['duration_type'] = netflix['duration_type'].str.lower()

#unificamos los dataframes en uno solo para mayor comidad para manejar la informacion
df_completo= pd.concat([amazon,netflix,hulu,disney])
df_completo.duration_int=df_completo.duration_int.fillna(0)
df_completo.duration_int=df_completo['duration_int'].astype(int)
df_completo

#FIN DE ETL
#INICIO DE QUERYS



# Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma


#Comenzamos con las querys 
def keyword_funcion(plataforma,keyword):
    cantidad_de_keyword=df_completo.loc[df_completo['title'].str.contains(keyword)]
    tabla_id = cantidad_de_keyword.groupby(['id']).size().reset_index(name='cantidad de id')
    lista=list(plataforma)
    if lista[0] == 'a':
        plataforma = 'amazon'
        cantidad_a = tabla_id['id'].str.startswith('a').sum()
        return plataforma, cantidad_a
    else:
        pass
    if lista[0] == 'd':
        plataforma = 'disney'
        cantidad_d = tabla_id['id'].str.startswith('d').sum()
        return plataforma, cantidad_d
    else:
        pass
    if lista[0] == 'h':
        plataforma = 'hulu'
        cantidad_h = tabla_id['id'].str.startswith('h').sum()
        return plataforma, cantidad_h
    else:
        pass

    if lista[0] == 'n':
        plataforma = 'netflix'
        cantidad_n = tabla_id['id'].str.startswith('n').sum()
        return plataforma, cantidad_n
    else:
        return print('por favor ingrese una plaforma como amazon, disney,hulu o netflix muchas gracias')


# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

#Segunda query 
def get_score_count(plataforma,point,anio):
    filtro_anio_y_score = df_completo[(df_completo['release_year'] == anio) & (df_completo['score']> point)&(df_completo['type']=="movie")]
    lista=list(plataforma)
    if lista[0] == 'a':
        plataforma = 'amazon'
        cantidad_a = filtro_anio_y_score['id'].str.startswith('a').sum()
        return plataforma, cantidad_a
    else:
        pass
    if lista[0] == 'd':
        plataforma = 'disney'
        cantidad_d = filtro_anio_y_score['id'].str.startswith('d').sum()
        return plataforma, cantidad_d
    else:
        pass
    if lista[0] == 'h':
        plataforma = 'hulu'
        cantidad_h = filtro_anio_y_score['id'].str.startswith('h').sum()
        return plataforma, cantidad_h
    else:
        pass

    if lista[0] == 'n':
        plataforma = 'netflix'
        cantidad_n = filtro_anio_y_score['id'].str.startswith('n').sum()
        return plataforma, cantidad_n
    else:
        return print('Hay un error con la plataforma seleccionada o el anio seleccionado, por favor intentelo nuevamente')
    

# La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

#Query 3
def get_second_score(plataforma):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}
    df_temp = df_completo[(df_completo['id'].str[0] == dicc[plataforma])&(df_completo['type'] == 'movie')].sort_values(["score","title"],ascending=[False,True]).reset_index(drop=True)
    titulo = df_temp.iloc[1,2]
    score = df_temp.iloc[1,14]
    return titulo, score

# Película que más duró según año, plataforma y tipo de duración

def get_longest(plataforma,duration_tipo,date):
     dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}
     df_temp = df_completo[(df_completo['id'].str[0] == dicc[plataforma])&(df_completo['release_year']==date)&(df_completo['duration_type']==duration_tipo)&\
     (df_completo['type']=='movie')].sort_values(['duration_int'], ascending = False).reset_index(drop = True)
     return df_temp


# Cantidad de series y películas por rating

def get_rating_count(rating):
    
    cantidad_rating= df_completo[df_completo['rating']== rating]

    return rating, len(cantidad_rating)