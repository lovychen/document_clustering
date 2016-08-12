#! /usr/bin/env python
# -*- coding=utf-8 -*-
# from __future__ import print_function, unicode_literals
import sys
import os
import json
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append("../")
import jieba
import sys
sys.path.append('../')
import jieba.analyse
from optparse import OptionParser  # 引入关键词的包
from docopt import docopt
from optparse import OptionParser
path = "D:\\code\\github\\document\\document_clustering\\novel_data\\"
# jieba.load_userdict("userdict.txt")#导入用户自定义词典
import jieba.posseg as pseg
class Fenci:
    def __init__(self,u):
        self.u = u
    def Get_fenci(self):

        # jieba.add_word('石墨烯')#动态添加自定义单词
        jieba.add_word('凱特琳')
        jieba.del_word('自定义词')
        jieba.add_word("易风化")
        filtered_tokens = []
        test_sent = ""
        for i in range(1,2):
            Data_path = path + "he"+".txt"
            test_sent ="".join(open(Data_path, 'rb').read())
        print (test_sent)
        words = jieba.cut(test_sent)
        filtered_tokens.append([each for each in jieba.cut(test_sent)])
        print ('-'*40)
        print (json.dumps(filtered_tokens))
        print("="*40)
    def GetKeyword(self,text):
        global s
        topK = 20
        withWeight = False
        tags = jieba.analyse.extract_tags(text, topK=topK, withWeight=withWeight)  # 直接调用
        for tag in tags:
            s.add(tag)
        # if withWeight is True:
        #     for tag in tags:
        #         print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
        #     print tag
        # else:
        #     print(",".join(tags))

if __name__ == "__main__":
    s = set()
    for fn in os.listdir(path):
        print fn
        Data_path = path + fn
        test_sent=""
        test_sent = "".join(open(Data_path, 'rb').read())
        Fenci('www').GetKeyword(test_sent)
    count  =  0
    f = open("tttt.txt",'a')
    for x in s:
        count = count + 1
        f.write(x+" ")
    f.close()
    print count