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
    return dataset, X, Y

def leerCsv(nombre):
    dataset = pd.read_csv("Data/" + nombre + ".csv", header=0, sep=';', quotechar='"', encoding = "ISO-8859-1")
    return dataset

def encodeData(data, index):
    from sklearn.preprocessing import LabelEncoder
    labelencoder = LabelEncoder()
    data[:, index] = labelencoder.fit_transform(data[:, index])
    return data

def getDummyVariables(data, index):
    from sklearn.preprocessing import OneHotEncoder
    onehotencoder = OneHotEncoder(categorical_features = [index])
    data = onehotencoder.fit_transform(data).toarray
    column_name = list(data)[index]
    data = data.drop(column_name, 1)
    return data

def splitTrainTest(X, y, porc_test):
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = porc_test, random_state = 0)
    return X_train, X_test, y_train, y_test

def featureScaling(X):
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    return X


df, X, Y = leerCsvColumnas("clarin_titulos_final", [23, 24, 26, 27], 25)
X = encodeData(X,0)
X = getDummyVariables(X,0)
X_train, X_test, y_train, y_test = splitTrainTest(X, Y, 0.2)
X_train = featureScaling(X_train)
