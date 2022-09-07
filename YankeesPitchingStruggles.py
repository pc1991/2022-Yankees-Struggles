# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:28:31 2022

@author: pchri
"""

import numpy
from matplotlib import pyplot
from pandas import read_csv
from pandas import set_option
from pandas.plotting import scatter_matrix

#load dataset
url = r'C:\Users\pchri\Downloads\Yankees Pitching Struugles 2022.csv'
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

#bar
dataset[2].plot(kind='bar')
pyplot.show()
dataset[4].plot(kind='bar')
pyplot.show()
dataset[5].plot(kind='bar')
pyplot.show()
dataset[6].plot(kind='bar')
pyplot.show()
dataset[7].plot(kind='bar')
pyplot.show()
dataset[8].plot(kind='bar')
pyplot.show()
dataset[9].plot(kind='bar')
pyplot.show()
dataset[10].plot(kind='bar')
pyplot.show()
dataset[12].plot(kind='bar')
pyplot.show()
dataset[14].plot(kind='bar')
pyplot.show()
dataset[15].plot(kind='bar')
pyplot.show()