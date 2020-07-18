FROM jupyter/scipy-notebook:ea01ec4d9f57

RUN pip install pyarrow==0.16.0
RUN pip install spacy==2.3.0
RUN pip install Flask==1.1.2
RUN pip install textblob==0.15.3
RUN pip install langid==1.1.6
RUN pip install langdetect==1.0.8
RUN pip install gensim==3.8.0
RUN pip install geopandas==0.8.0
RUN pip install geopy==2.0.0
RUN pip install wordcloud==1.7.0

RUN pip install https://github.com/explosion/spacy-models/releases/download/es_core_news_lg-2.3.0/es_core_news_lg-2.3.0.tar.gz

USER root

RUN apt update -y
RUN apt-get install -y libproj-dev proj-data proj-bin
RUN apt-get install -y libgeos-dev

USER jovyan

RUN pip install cartopy