"""
@Time    : 2018/8/29 14:46
@Author  : Lishihang
@File    : sample_processing.py
@Software: PyCharm
@desc:
"""
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import Normalizer
import numpy as np

dir = "d:/ZSL_ImageGame/DatasetA_train_20180813/"


def words_embed():
    """
    处理label_list和class_wordembeddings,文本特征
    :return: data/word_embeddings.csv
    """
    train_labels = pd.read_csv(dir + "label_list.txt", sep='\t', header=None)
    print(train_labels.head())

    train_words = pd.read_csv(dir +"class_wordembeddings.txt", sep=' ', header=None)
    print(train_words.head())

    res = pd.merge(train_labels, train_words, left_on=1, right_on=0)

    res = res.drop([1, '1_x', '0_y'], axis=1)
    print(res.head())
    res.to_csv('output/word_embeddings.csv', index=None, header=None, sep='\t')

def traindata():
    """
    连接数据
    :return:
    """
    train = pd.read_csv(dir + 'train.txt', header=None, sep='\t')
    train_attr = pd.read_csv(dir + "attributes_per_class.txt", sep='\t', header=None)
    train_words=pd.read_csv('output/word_embeddings.csv',sep='\t',header=None)

    print(train.head())
    print(train_attr.head())
    print(train_words.head())
    # res.to_csv('output/traindata.csv',index=None,header=None,sep='\t')

def normalline(data):

    for i,cs in enumerate(np.sum(data,axis=1).values):
        if cs!=0:
            data.iloc[i,:]=data.iloc[i,:]*1.0/cs
    return data


def wordsnormal():

    words=pd.read_csv(r"D:\TianChi\201809ZSL\DatasetA_train_20180813\attributes_per_class.txt", header=None, sep='\t')
    target = pd.read_csv(r"D:\TianChi\201809ZSL\DatasetA_train_20180813\train.txt", header=None, sep='\t')

    # print(set(words.iloc[:, 0].values.tolist()) - set(target.iloc[:, 1].values.tolist()))


    labels=np.array(words.iloc[:,0]).reshape(-1,1)

    dentype=words.iloc[:,1:7]
    dentype=normalline(dentype)

    dencolor = words.iloc[:, 7:15]
    dencolor=normalline(dencolor)

    denhas = words.iloc[:, 15:19]
    denhas = normalline(denhas)

    denfor=words.iloc[:, 19:25]
    denfor = normalline(denfor)

    words=pd.DataFrame(np.concatenate((labels,dentype,dencolor,denhas,denfor),axis=1))

    # print(words.head())
    # print(words.iloc[:,1:].describe())
    testwords = words[words.iloc[:, 0].isin(set(words.iloc[:, 0].values.tolist()) - set(target.iloc[:, 1].values.tolist()))]
    words.to_csv("../data/attributes_per_class_norm.csv",header=None,sep='\t',index=None)

if __name__ == '__main__':
    # words_embed()
    # traindata()

    wordsnormal()