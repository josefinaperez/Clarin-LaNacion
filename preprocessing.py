# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:29:10 2017

@author: Josefina
"""

import pandas as pd

#Importar dataset
def leerCsvColumnas(nombre, var_dep, var_ind):
    dataset= pd.read_csv("Data/" + nombre + ".csv", header=0, sep=';', quotechar='"', encoding = "ISO-8859-1")
    X = dataset.iloc[: , var_dep].values
    Y = dataset.iloc[: , var_ind].values
    return X, Y

def leerCsv(nombre):
    dataset = pd.read_csv("Data/" + nombre + ".csv", header=0, sep=';', quotechar='"', encoding = "ISO-8859-1")
    return dataset

def encodeData(data, index):
    from sklearn.preprocessing import LabelEncoder
    labelencoder = LabelEncoder()
    data[:, index] = labelencoder.fit_transform(data[:, index])
    return data

def dummyVariables(data, index):
    from sklearn.preprocessing import OneHotEncoder
    onehotencoder = OneHotEncoder(categorical_features = [index])
    data = onehotencoder.fit_transform(data).toarray
    column_name = list(data)[index]
    data = data.drop(column_name, 1)
    return data

df = leerCsv("clarin_titulos_final")
X, Y = leerCsvColumnas("clarin_titulos_final", [23, 24, 26, 27], 25)
X = encodeData(X,0)
X = dummyVariables(X,0)
print(X[:, 0])
index = 0
data = X