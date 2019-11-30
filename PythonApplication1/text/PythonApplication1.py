# 基于TF-IDF算法的关键词抽取
 
import jieba
import jieba.analyse
 
f= open('example.txt', mode = 'r' ,encoding='utf-8')
sentence=f.read()
f.close()
 
keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n','nr','ns'))
 
# print(type(keywords))
# <class 'list'>
 
f = open("look.txt", 'a')
f.seek(0)
f.truncate()
for item in keywords: f.write(item[0]+'\n')
f.close()