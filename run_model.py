
# -*- coding:utf-8 -*-
from gensim.models import Word2Vec
import pprint
 
# model = Word2Vec.load("jawiki-jasoccker-player.model")
model = Word2Vec.load("./out_models/jawiki-20181022.soccer.model")

pprint.pprint(model.most_similar(positive=["メッシ","レアル"], negative=["バルサ"]))