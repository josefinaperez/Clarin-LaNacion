#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:20:43 2017

@author: josefinaperez
"""

import keras
from keras.models import Sequential
from keras.layers import Dense

def buildANN(cant_var_indep, cant_var_dep, cant_clases):
    print("Building ANN...")
    classifier = Sequential()
    cant_nodos_hidden = round((cant_var_indep + cant_var_dep) / 2)
    classifier.add(Dense(output_dim = cant_nodos_hidden, init = 'uniform', activation = 'relu', input_dim = cant_var_indep))
    classifier.add(Dense(output_dim = cant_nodos_hidden, init = 'uniform', activation = 'relu'))
    classifier.add(Dense(output_dim = cant_clases, init = 'uniform', activation = 'softmax'))
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    return classifier

def fitANN(classifier, X_train, y_train):
    print("Fitting classifier...")
    classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)

#def predict(classifier, X):
    #print("Making predictions...")
    #y = classifier.predict(X)
    #return y

def a(X_train, y_train, cant_clases):
    print("HOLA")
    classifier = buildANN(1, 4, cant_clases)
    print("LICEN")
    fitANN(classifier, X_train, y_train)
    