#! /usr/bin/env python
# -*- coding=utf-8 -*-
import os
import jieba.analyse
import jieba
import jieba.posseg as pseg
import sys
import json
import string
import time
from sklearn import feature_extraction
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
reload(sys)
sys.setdefaultencoding('utf8')

# 获取文件列表（该目录下放着100份文档）
def getFilelist(argv):
    print argv
    path = argv[0]
    print path
    filelist = []
    for f in os.listdir(path):
        if (f[0] == '.'):
            pass
        else:
            filelist.append(f)
    return filelist, path


#对文档进行分词处理
def fenci(argv, path):
    # 保存分词结果的目录
    sFilePath = 'D:\\test_data\\fenci\\'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)
    # 读取文档
    filename = argv
    f = open(path + filename, 'r+')
    file_list = f.read()
    f.close()
    # 对文档进行分词处理，采用默认模式
    seg_list = jieba.cut(file_list, cut_all=True)
    # 对空格，换行符进行处理
    result = []
    for seg in seg_list:
        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n"):
            result.append(seg)

    # 将分词后的结果用空格隔开，保存至本地。比如"我来到北京清华大学"，分词结果写入为："我 来到 北京 清华大学"
    f = open(sFilePath + "/" + filename + "-seg.txt", "w+")
    f.write(' '.join(result))
    f.close()


# 读取100份已分词好的文档，进行TF-IDF计算
def GetKeyword(argv, path):
    sFilePath = 'D:\\test_data\\fenci\\'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)
    filename = argv
    f = open(path + filename, 'r+')
    file_list = f.read()
    f.close()
    global s
    topK = 30
    withWeight = False
    tags = jieba.analyse.extract_tags(file_list, topK=topK, withWeight=withWeight)  # 直接调用
    result = []
    for seg in tags:
        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n"):
            result.append(seg)

    # 将分词后的结果用空格隔开，保存至本地。比如"我来到北京清华大学"，分词结果写入为："我 来到 北京 清华大学"
    f = open(sFilePath + "/" + filename + "-seg.txt", "w+")
    f.write(' '.join(result))
    f.close()

def Tfidf():
    path = 'D:\\test_data\\fenci\\'
    corpus = []  # 存取100份文档的分词结果
    for ff in os.listdir(path):
        fname = path + ff
        print fname
        f = open(fname, 'r+')
        content = f.read()
        f.close()
        corpus.append(content)
    f = open("llll.txt",'a')
    f.write(json.dumps(corpus))
    f.close()
    print corpus
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))# 类似在所有分词中的比例

    word = vectorizer.get_feature_names()  # 所有文本的关键字
    weight = tfidf.toarray()  # 对应的tfidf矩阵,同时打印出所有的矩阵
    KMS(weight)

    # for each in weight:
    #     print each
    dict = 1-cosine_similarity(weight)
    for each in dict:
        print each
    sFilePath = 'D:\\test_data\\answer\\'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)

    # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
    for i in range(len(weight)):
        print u"--------Writing all the tf-idf in the", i, u" file into ", sFilePath + '/' + string.zfill(i, 5) + '.txt', "--------"
        f = open(sFilePath + '/' + string.zfill(i, 5) + '.txt', 'w+')
        for j in range(len(word)):
            f.write(word[j] + "    " + str(weight[i][j]) + "\n")
        f.close()
def KMS(tfidf_matrix): #利用聚类
    num_clusters = 6    #假定聚类的数目
    km = KMeans(n_clusters=num_clusters)
    km.fit(tfidf_matrix)
    clusters = km.labels_.tolist()
    # km = joblib.load('doc_cluster.pkl')
    # clusters = km.labels_.tolist()
    print "****************"
    for each in clusters:
        print each,
    print "****************"

if __name__ == "__main__":
    argv = ['D:\\test_data\\novel_data\\']
    print argv[0]
    allfile = getFilelist(argv)
    print allfile
    for ff in allfile[0]:
        print ff
        print "Using jieba on " + ff
        GetKeyword(ff, argv[0])
    Tfidf()
    #对整个文档进行排序
    path= 'D:\\test_data\\answer\\'
    os.system("sort -nrk 2 " + path + "/*.txt >" + path + "/sorted.txt")