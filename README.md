# Fase build2learn Saturdays.AI Mallorca (ods)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/michelangelocasablancas/ods/master)

## Contenido de los diretorios

La organización de los ficheros en el repositorio está basada en [2].

* `data`: Datos utilizados. Directorio de sólo lectura.
* `img`: Imágenes.
* `ipynb`: _Jupyter Notebooks_ utilizados para experimentar. El nombre incluye como prefijo la fecha en formato AAAAMMDD.

## Plan del proyecto

Este proyecto consiste en identificar si un texto hace referencia a un ODS[1] (Objetivo de desarrollo sostenible)
y tratar de clasificar a cual. Incluye divulgación sobre los ODS.

## Introducción

El proyecto se enmarca en los ODS y en la llamada Agenda 2030, creada por Naciones Unidas en el encuentro de la COP21 
celebrada en 2015 en París. En este encuentro, los países adheridos a Naciones Unidas llegan al Acuerdo de París donde 
se consensuan unos Objetivos de Desarrollo Sostenible (ODS en adelante) que debe abordar cada país con medidas particulares. 
La primera meta que deben cumplir dichos países, es presentar un plan de Acción antes de 2020. España lo ha presentado recientemente. 

Esta Agenda multinivel y multiactor, que hay que cumplir cara a 2030, y cuyos ODS hay que abordar. 
En este proyecto nos centraremos en la Empresa Privada, dejando al margen a la Empresa Pública y el individuo en general. 

Existen organizaciones que, muchas veces sin saberlo, están abordando algún o algunos ODS. 
Con la ejecución de este proyecto se quiere dar visibilidad a esas organizaciones, proporcionándoles una mención especial. 

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

Los ODS y la Agenda 2030 proponen metas ambiciosas, desconocidas y urgentes. Es por ello por lo que se necesita poner orden y proporcionar un método con el que se pueda abordar la agenda:
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

* Limpiar los _tweets_.

## Clasificar los _tweets_

### LDA

Utilizar LDA[3] para agrupar los _tweets_ por temas de manera no supervisada.

### Similitud entre documentos

Unir la lista de palabras clave por ODS y considerarla un documento.
Obtener la similitud de cada _tweet_ con estos documentos.

### Búsqueda de documentos

Construir una matriz `tf-idf` con todos los _tweets_ y usarla para buscar _tweets_.

1. Calcular `tf-idf` para una palabra clave.
1. Buscar los documentos (_tweets_) más similares. Para ello utilizar la similitud coseno[4].

## Obtener información de los _tweets_

Recuperar usuario, empresa, etc. de los _tweets_.

## Refinamiento del modelo

## Resultados

## Conclusiones

## Referencias

1. https://www.un.org/sustainabledevelopment/es/objetivos-de-desarrollo-sostenible/
1. Cook, Joshua. "Interactive Software Development".
_Docker for Data Science: Building Scalable and Extensible Data Infrastructure Around the Jupyter Notebook Server_. Apress, 2017, pp. 213-251.
1. https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation
1. https://en.wikipedia.org/wiki/Cosine_similarity
