import pandas as pd
import jieba

# 词向量 - 实际动手使用word2vec
# https://blog.csdn.net/sfw_123817/article/details/81304658

filePath = 'E:\\data\\testdata.txt'
fileSegWordDonePath = 'E:\\data\\testdata_seg_done.txt'
fileTrainRead = pd.read_csv(filePath)
fileTrain = pd.Series(fileTrainRead.iloc[:,0])
f = lambda x: x[9:-11]
fileTrain = fileTrain.apply(f)

fileTrain.dropna(how='any')

fileTrainSeg = []
for line in fileTrain:
    data = jieba.cut(line, cut_all=False)
    # print(list(data))
    fileTrainSeg.append(" ".join(list(data)))

output_list = pd.Series(fileTrainSeg)
output_list.to_csv(fileSegWordDonePath, encoding='utf-8')