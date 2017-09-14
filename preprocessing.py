# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:29:10 2017

@author: Josefina
"""

import pandas as pd

#Importar dataset
def leerCsvColumnas(nombre, var_dep, var_ind):
    dataset= pd.read_csv("Data/" + nombre + ".csv", header=0, sep=';', quotechar='"', encoding = "ISO-8859-1")
    dataset = dataset.dropna(axis=0, how='any', thresh=None, subset=['tema', 'texto propio', 'localizacion_info', 'temp'], inplace=False)
    X = dataset.iloc[: , var_dep]
    #X = X.values
    Y = dataset.iloc[: , var_ind]

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
    onehotencoder.fit_transform(data).toarray
    #column_name = list(data)[index]
    #data = data.drop('texto_propio', 1)
    return data

def dummy(data):
    one_hot = pd.get_dummies(data['temp'], drop_first=True)
    data = data.drop('temp', axis=1)
    data = data.join(one_hot)
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

def getPreprocessedDatasets(nombre, var_dep, var_ind):
    df, X, Y = leerCsvColumnas(nombre, var_dep, var_ind)
    #encode data y 
    X_train, X_test, y_train, y_test = splitTrainTest(X, Y, 0.2)
    X_train = featureScaling(X_train)
    X_test = featureScaling(X_test)
    y_test = featureScaling(y_test)
    y_train = featureScaling(y_train)
    
    return X_train, X_test, y_train, y_test


