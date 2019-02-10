from gensim.models import word2vec
mopdelfilePath = 'E:\\data\\model.bin'
model = word2vec.Word2Vec.load(mopdelfilePath)
print(model.wv['中国'])