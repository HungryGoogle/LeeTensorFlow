import pkuseg

lexicon = ['北京大学', '北京天安门']				  #希望分词时用户词典中的词固定不分开
segDefault = pkuseg.pkuseg()					#默认分词类型
seg = pkuseg.pkuseg()			#加载模型，给定用户词典
textDefault = segDefault.cut('我爱北京天安门')	    #进行分词
text = seg.cut('我爱北京天安门')					#进行分词
print(textDefault)
print(text)

for w in text:
    print(w.word, "/", w.flag, ", ", end=' ')

print("\n" + "="*40)