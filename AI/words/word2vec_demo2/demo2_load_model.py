import gensim
from gensim.models import word2vec
mopdelfilePath = 'D:\\AI\\words\\news_12g_baidubaike_20g_novel_90g_embedding_64.model'
# mopdelfilePath = 'D:\\AI\\words\\baike_26g_news_13g_novel_229g.bin'
# model = gensim.models.KeyedVectors.load_word2vec_format(mopdelfilePath, binary=True)

model = gensim.models.Word2Vec.load(mopdelfilePath)
# model = word2vec.Word2Vec.load(mopdelfilePath)
print(model.wv['中国'])