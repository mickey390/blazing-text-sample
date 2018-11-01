# -*- coding:utf-8 -*-
import json
import gzip

# SAVE_FILE = './data/japanese_footballer.txt'
# SELECT_CATEGORY = '日本のサッカー選手'

SAVE_FILE = './data/soccer.txt'
SELECT_CATEGORY = 'サッカー'

def save(text):
    with open(SAVE_FILE, 'a') as f:
        f.write(text + '\n')

with gzip.open("./wikipediba_data/jawiki-20181022-cirrussearch-content.json.gz") as f:
    for line in f:
        json_line = json.loads(line.decode('utf-8'))
        if "index" not in json_line:
            category = json_line["category"]
            text = json_line["text"]
            l_in = [s for s in category if SELECT_CATEGORY in s]
            if len(l_in) > 0:
                print (l_in)
                print (text)
                save(text)



