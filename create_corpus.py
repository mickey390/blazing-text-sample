# -*- coding:utf-8 -*-
import linecache
import random
import MeCab

random.seed(42)
filename = './data/soccer.txt'
save_file = './out_corpus/jawiki-20181022.soccer.courpus'
t = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

if __name__ == '__main__':
    num_lines = sum(1 for line in open(filename))
    indices = list(range(num_lines))
    print (indices)

    with open(save_file, 'w') as f:
        for i in indices:
            text = linecache.getline(filename, i)
            text = text.strip()
            text = t.parse(text).strip()
            print (text)
            f.write(text)