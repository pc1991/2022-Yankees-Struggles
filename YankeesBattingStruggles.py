# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:28:11 2022

@author: pchri
"""

import numpy
from matplotlib import pyplot
from pandas import read_csv
from pandas import set_option
from pandas.plotting import scatter_matrix

#load dataset
url = r'C:\Users\pchri\Downloads\Yankees Batting Struugles 2022.csv'
dataset = read_csv(url, header=None)

#shape
print(dataset.shape)

#types
print(dataset.dtypes)

#head
set_option('display.width', 100)
print(dataset.head(20)) 

#top row removal
dataset = dataset.drop(labels=0, axis=0)

#convert string to float
dataset = dataset.astype(float)
print(dataset.dtypes)

#histograms
dataset.hist(sharex=False, sharey=False, xlabelsize=1, ylabelsize=1)
pyplot.show()
dataset[2].hist()
pyplot.show()
dataset[13].hist()
pyplot.show()

#bar
dataset[2].plot(kind='bar')
pyplot.show()
dataset[6].plot(kind='bar')
pyplot.show()
dataset[9].plot(kind='bar')
pyplot.show()
dataset[10].plot(kind='bar')
pyplot.show()
dataset[13].plot(kind='bar')
pyplot.show()
dataset[21].plot(kind='bar')
pyplot.show()
dataset[22].plot(kind='bar')
pyplot.show()
dataset[23].plot(kind='bar')
pyplot.show()
dataset[24].plot(kind='bar')
pyplot.show()