import json
import string
import re

import pandas as pd

import spacy

from flask import Flask, request, jsonify

app = Flask(__name__)


def camel_case(example):
    if any(x in example for x in string.punctuation):
        return False
    else:
        if any(list(map(str.isupper, example[1:-1]))) and not all(list(map(str.isupper, example[1:-1]))):
            return True
        else:
            return False


def camel_case_split(word):
    idx = list(map(str.isupper, word))
    case_change = [0]
    for (i, (x, y)) in enumerate(zip(idx, idx[1:])):
        if x and not y:
            case_change.append(i)
        elif not x and y:
            case_change.append(i + 1)
    case_change.append(len(word))
    return [word[x:y] for x, y in zip(case_change, case_change[1:]) if x < y]


nlp = spacy.load("es_core_news_lg")


def clean_tweets(tweet):
    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub('http\S*', '', tweet)
    tweet = re.sub(r'@[a-zA-Z0-9]+', '', tweet)

    camel_case_words = [word[1:] for word in re.findall(r'#[a-zA-Z]+', tweet) if camel_case(word[1:])]
    splited_words = [' '.join(camel_case_split(word[1:])) for word in re.findall(r'#[a-zA-Z]+', tweet) if
                     camel_case(word[1:])]
    for camel, splited in zip(camel_case_words, splited_words):
        tweet = tweet.replace(camel, splited)

    tweet = re.sub(r'#', '', tweet)
    tweet = re.sub(r"\b[a-zA-Z]\b", "", tweet)
    tweet = re.sub(r"\s+", " ", tweet)

    tweet_tokens = nlp(tweet)
    tweets_clean = [word.lemma_ for word in tweet_tokens if not word.is_stop and word.pos_ != 'PUNCT']

    return ' '.join(tweets_clean).lower().strip()


def classify(text):
    palabras = pd.read_feather('../data/diccionario_palabras_ods')

    words_list = palabras[['ODS.1', 'PALABRAS']].dropna().groupby('ODS.1')['PALABRAS'].apply(list)
    words_list_nlp = [nlp(' '.join(words).lower()) for words in words_list]

    clean_text = clean_tweets(text)
    return [nlp(clean_text).similarity(words) for words in words_list_nlp]


@app.route('/')
def hello_world():
    return 'ODS: Texts classification'


@app.route('/', methods=['POST'])
def classify_text():
    record = json.loads(request.data)
    return jsonify(classify(record['text']))
