#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:50:55 2017

@author: josefinaperez
"""
CANT_CLASES = 9
NOMBRE_ARCHIVO = "clarin_titulos_final"
VAR_DEP = [23, 24, 26, 27]
VAR_IND = 25

def main():
    from preprocessing import getPreprocessedDatasets
    X_train, X_test, y_train, y_test = getPreprocessedDatasets(NOMBRE_ARCHIVO, VAR_DEP, VAR_IND)
    
    from ann import a
    a(X_train, y_train, CANT_CLASES)
    
    #ann (tiene que quedar en true/false)
    #from sklearn.metrics import confusion_matrix
    #cm = confusion_matrix(y_test, y_pred)
    

main()

