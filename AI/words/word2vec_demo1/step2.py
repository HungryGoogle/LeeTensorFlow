from gensim.models import word2vec
import pandas as pd

filePath = 'E:\\data\\testdata.txt'
fileSegWordDonePath = 'E:\\data\\testdata_seg_done.txt'

mopdelfilePath = 'E:\\data\\model.bin'

fileTrainRead = pd.read_csv(fileSegWordDonePath)
train_sentences = pd.Series(fileTrainRead.iloc[:, 1])
f = lambda x: str(x).split(" ")
train_sentences = train_sentences.apply(f)

model = word2vec.Word2Vec(train_sentences, size=300)
model.save(mopdelfilePath)