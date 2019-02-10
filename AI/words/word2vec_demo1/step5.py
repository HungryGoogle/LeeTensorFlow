from gensim.models import word2vec
mopdelfilePath = 'E:\\data\\model.bin'
model = word2vec.Word2Vec.load(mopdelfilePath)

indexes = model.wv.most_similar_cosmul('中国')
for index in indexes:
    print(index)