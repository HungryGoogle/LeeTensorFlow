import codecs

import gensim
from gensim.models import Word2Vec


def main():
    path_to_model = 'D:\\AI\\words\\baike_26g_news_13g_novel_229g.bin'
    output_file = 'D:\\AI\\words\\baike_26g_news_13g_novel_229g.txt'
    export_to_file(path_to_model, output_file)


def export_to_file(path_to_model, output_file):
    output = codecs.open(output_file, 'w', 'utf-8')
    model = gensim.models.KeyedVectors.load_word2vec_format(path_to_model, binary=True)
    # model = Word2Vec.load_word2vec_format(path_to_model, binary=True)
    print('done loading Word2Vec')
    vocab = model.vocab
    for mid in vocab:
        # print(model[mid])
        # print(mid)
        vector = list()
        for dimension in model[mid]:
            vector.append(str(dimension))
        # line = { "mid": mid, "vector": vector  }
        vector_str = ",".join(vector)
        line = mid + "\t" + vector_str
        # line = json.dumps(line)
        output.write(line + "\n")
    output.close()


if __name__ == "__main__":
    main()

# 之后就可以用java处理了
    # Word2vec的bin文件的java处理
    # https: // blog.csdn.net / zcz_822 / article / details / 52711818