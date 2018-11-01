# -*- coding:utf-8 -*-
import logging
from gensim.models import word2vec

# COURPUS="ja.text8" 
# MODEL_NAME="jawiki-jasoccker-player.model"

COURPUS="./out_corpus/jawiki-20181022.soccer.courpus"
MODEL_NAME="./out_models/jawiki-20181022.soccer.model"


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.Text8Corpus(COURPUS)
model = word2vec.Word2Vec(sentences, size=200)
model.save(MODEL_NAME)