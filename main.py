#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:50:55 2017

@author: josefinaperez
"""

def main():
    #preprocessing
    #ann (tiene que quedar en true/false)
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)