
## Introducción:

Me presento soy Lucas Rodriguez, estudiante de la carrera de Data Science en SoyHenry actualmente em encuentro en la etapa de labs

En el primer lab, vamos a realizar un proyecto de Data Engineer, donde se nos hizo entrega de 4 datasets de platamormas de video o streamings que son amazon, disney, plus, hulu y netflix.
Debemos realizar el analisis explotarorio de dichos datasets para poder corregir los valores faltantes, verificar la integridad de los datos y armar nuevas columnas con mayor informacion como asi fue requirido.

## Explicacion del Proyecto :

Se realizo un trabajo de ETL sobre los conjuntos de datos recibidos.

Se desarrolle una API con FastApi para disponibilizar los datos y se realizo el  deployment de la API se realizo en Deta.

Las funciones a realizar son:

Cantidad de veces que aparece una palabra clave en el título de peliculas/series, por plataforma

Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

La segunda película con mayor partitura para una plataforma determinada, según el orden alfabético de los títulos.

Película que más apareció según año, plataforma y tipo de duración

Cantidad de series y películas por rating


## Explicación de los contenidos del Repositorio:

En la carpeta appse encuentran los datasets analizados, el archivo main.py que es el archivo en el cual se configura FastAPI y se instancian los decoradores de la API y además, el archivo limpieza.py en el cual se encuentra todo el proceso de etl comentado.

## Herramientas usadas:

fastapi
deta
python
pandas
limpieza
requests

## Adicional:

· Video de muestra :

https://youtu.be/kZMHEi3RGpo

- Incio de pagina y guia para usuarias/os

https://k3ulsw.deta.dev/


· Enlaces para consulta :

https://k3ulsw.deta.dev/keyword_funcion/netflix/love

https://k3ulsw.deta.dev/get_second_score/amazon

https://k3ulsw.deta.dev/get_score_count/netflix/85/2010

https://k3ulsw.deta.dev/get_longest/netflix/min/2016

https://k3ulsw.deta.dev/get_rating_count/18+
