from gensim.models import word2vec
mopdelfilePath = 'E:\\data\\model.bin'
model = word2vec.Word2Vec.load(mopdelfilePath)
index = 200
print (model.wv.index2word[200])