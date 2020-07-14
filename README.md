# Fase build2learn Saturdays.AI Mallorca (ods)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/michelangelocasablancas/ods/master)

![wordcloud](img/wordcloud.png?raw=true)

## Contenido de los diretorios

La organización de los ficheros en el repositorio está basada en [2]. Ver también [5]

* `data`: Datos utilizados. Directorio de sólo lectura.
* `img`: Imágenes.
* `ipynb`: _Jupyter Notebooks_ utilizados para experimentar. El nombre incluye como prefijo la fecha en formato AAAAMMDD.

## Plan del proyecto

Este proyecto consiste en identificar si un texto hace referencia a un Objetivo de desarrollo sostenible (ODS en adelante) y tratar de clasificar dicho texto con uno o varios ODS al que hace referencia. 

## Introducción

El proyecto se enmarca en los ODS y en la llamada Agenda 2030, creada por Naciones Unidas en el encuentro de la COP21 
celebrada en 2015 en París. En este encuentro, los países adheridos a Naciones Unidas llegan al Acuerdo de París donde 
se consensuan unos Objetivos de Desarrollo Sostenible que debe abordar cada país con medidas particulares. 

Existen organizaciones, administraciones públicas y también individuos que, muchas veces sin saberlo, están abordando algún o algunos ODS. 
Queremos ver en qué ODS se está contribuyendo más.

La plataforma contará con 2 motores:

* En una primera fase, una **sonda** que rastree todas las noticias que se están difundiendo en internet acerca 
de los objetivos de desarrollo sostenible en Baleares.

* Una vez que dispongamos de la información de todas las noticias, realizaremos una ordenación de los objetivos manualmente, 
para recoger las características lingüísticas que debería entender un segundo motor de clasificación. 
De esta forma el sistema nos permitirá aprender todo lo necesario, para una vez lanzada la plataforma y viendo 
la respuesta de los usuarios en general, seamos capaces de realizar un **motor de clasificación lingüística**, que categorice 
las noticias en base a los 17 Objetivos. 

**Características de la Sonda:**

El sistema aparte de realizar la captura de las noticias también incorporará técnicas de machine learning, para identificar 
y clasificar el sentimiento de la noticia y ver si se trata de una noticia positiva o negativa.

El sistema de captura se realizará en base a un conjunto de hashtags que se definirán y se asociará a cada uno de los 17 objetivos.

**Características del motor de clasificación lingüística:**

El motor de clasificación lingüística se basará en una primera fase en 1 idioma: castellano y en base a un diccionario de palabras, 
se realizará una asociación de términos y objetivos, de manera que, si estamos hablando de un concepto concreto, 
el sistema será capaz clasificarlo en el objetivo correspondiente.

![Imagen 1](img/img1.png?raw=true)

Una vez analizada y clasificada toda la información (en una primera fase, a mano), se mostrarían los resultados en una plataforma web, 
dando visibilidad a los actores que ya están cumpliendo con los ODS. El aspecto de la plataforma sería este: 

![Imagen_2](img/img2.png?raw=true)

Los ODS y la Agenda 2030 proponen metas ambiciosas, desconocidas y urgentes. 
Es por ello por lo que se necesita poner orden y proporcionar un método con el que se pueda abordar la agenda:

*   Poner orden en lo que se está haciendo y/o afecte a Baleares, alrededor de los ODS.
*   Dar visibilidad a los actores que ya están haciendo algo.
*   Fomentar/poner en valor la reputación de los actores que ya están haciendo algo.
*   Ayudar a reducir el impacto de las organizaciones de Baleares.
*   Ayudar a cumplir con la legalidad.
*   Poner en valor los ODS dentro de cada organización

## Datos

Disponemos de los siguientes datos:

* tweets (`#ods`, `#agenda2030`, `#sostenibilidad`) recogidos desde hace aproximadamente un año. ([data/twitter_202006111846.zip](data/twitter_202006111846.zip))
* Palabras clave por cada ODS para etiquetar los tweets. (`data/Diccionario Palabras ODS.xlsx`)

Los tweets están almacenados en una base de datos PostgreSQL. Para empezar a trabajar no necesitamos acceder a la base de datos.
Nos basta un dataset con una foto de los datos actuales.

### Otros datos

## Análisis exploratorio

Estudiar los atributos y características de cada campo.

Utilizar NLP:
* Detección de entidades
* Importancia de palabras: tf-idf
* Comparar con las palabras recopiladas manualmente
* Análisis de sentimientos

Evaluar la posibilidad de etiquetar automáticamente con algún método semi-supervisado.

## Preparar los datos

* A partir de los tweets recogidos durante más de un año en una base de datos y exportados en JSON, hacer lectura el archivo que los contiene.
* Filtrar los tweets que están en español
* Eliminar entradas con texto nulo.
* Reindexar sin eliminar el índice original para después poder enlazar los textos con el resto de información del tweet. El reindexado es necesario para guardar el dataframe en formato feather.
* Limpiar los _tweets_: Eliminar emojis, caracteres inválidos, separar los hashtags con camel-case en diferentes palabras

## Clasificar los _tweets_

Para clasificar los _tweets_ nos planteamos tres opciones.

### LDA

Utilizar LDA[3] para agrupar los _tweets_ por temas de manera no supervisada.

Hicimos algunas pruebas pero no llegamos a profundizar en esta opción.

[20200613_tweets.ipynb](ipynb/20200613_tweets.ipynb)

### Similitud entre documentos

Unir la lista de palabras clave por ODS y considerarla un documento.
Obtener la similitud de cada _tweet_ con estos documentos.

El comparación de los textos con la librería `spacy` fue la que nos dio mejores resultados.

[20200617_similarity.ipynb](ipynb/20200617_similarity.ipynb), [20200627_similarity.ipynb](ipynb/202006127_similarity.ipynb)
 
### Búsqueda de documentos

Construir una matriz `tf-idf` con todos los _tweets_ y usarla para buscar _tweets_.

1. Calcular `tf-idf` para una palabra clave.
1. Buscar los documentos (_tweets_) más similares. Para ello utilizar la similitud coseno[4].

Con este método no obtuvimos nada en claro.

[20200703_tfidf.ipynb](ipynb/20200703_tfidf.ipynb)

## Resultados

### Lista de ODS y su frecuencia

![ODS Bar](img/ods_bars.svg?raw=true)

### Número de ODS por tweet

![ODS Hist](img/ods_histogram.svg?raw=true)

Hay aproximadamente un **40%** de _tweets_ que no están asociados a ningún ODS. 

### Clasificación de otros textos

La operaciones que realizamos a los _tweets_ se pueden aplicar a cualquier otro texto.
En [table.md](doc/table.md) se incluye el resultado de clasificar varios textos.

[20200714_ods.ipynb](ipynb/20200714_ods.ipynb)

## Refinamiento del modelo

## Conclusiones

* En base al diccionario de palabras, se puede categorizar el grado de similitud de los tweets con los diferentes 17 Objetivosa de Desarollo Sostenible. Hay palabras que se asocian directamente a varios ODS, debido a que tocan el mismo área.

* El grado de similitud entre las palabras y los ODS lo hemos establecido en un 70%. Quizás podríamos ser más restrictivos y subir dicho grado a un 90%, para que el resultado fuese más preciso.

* El 40.87% de los tweets no están relacionados con ningún ODS debido a la baja calidad del tweet, porque a penas contenían información o texto válido. Una gran parte del proyecto lo hemos destinado a la limpieza de los datos, para partir de una calidad óptima de información.

* La cantidad de ODS por tweet es muy similar entre los 2 y 10 ODS.


## Próximos Pasos

* Los tweets llevan asociadas las posiciones geográficas desde donde se emite el tweet, esto nos permitiría ver en qué poblaciones de España (o del mundo), se está dando visibilidad a los ODS. 

* Los tweets se generan desde cuentas específicas y se podrían ver cuántas cuentas hacen referencias a empresas. De esta manera podríamos analizar la información asociando las empresas a su sector de actividad empresarial y determinar que tipología de empresas están más comprometidas. 

* Otro tema que se puede realizar es añadir más diccionarios en otros idiomas, ya que, solo nos hemos basado en aquellos tweets escritos en castellano, pero se podría realizar algo similar en otros idiomas.

* Hasta la fecha solo hemos evaluado textos de un máximo de 140 caracteres, pero se puede ampliar a textos más largos, de hecho se han realizado pruebas con resultados satisfactorios.

* También podemos utilizar una librería de análisis de sentimiento para saber si el impacto del ODS en el texto analizado está siendo positivo o negativo.

* Y hemos hablado de crear un bot que esté en un servicio online y que esté siempre en funcionamiento, categorizando los textos recibidos. 


## Referencias

1. https://www.un.org/sustainabledevelopment/es/objetivos-de-desarrollo-sostenible/
2. Cook, Joshua. "Interactive Software Development".
_Docker for Data Science: Building Scalable and Extensible Data Infrastructure Around the Jupyter Notebook Server_. Apress, 2017, pp. 213-251.
3. https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation
4. https://en.wikipedia.org/wiki/Cosine_similarity
5. https://www.thinkingondata.com/how-to-organize-data-science-projects/
