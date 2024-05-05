# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:59:39 2024

@author: hatice
"""

import numpy as np
import pandas as pd

veriler = pd.read_csv("satislar.csv", encoding="utf-8")

aylar = veriler[["Aylar"]]
print(aylar)

satislar = veriler[["Satislar"]]
print(satislar)

satislar2 = veriler.iloc[:,:1].values
print(satislar2)

# verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(veriler[["aylar", "satislar"]])

# verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)   

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

# model insaası(linear regression)
# basit dogrusal regresyon icin gerekli kutuphane
from sklearn.linear_model import LinearRegression
lr=LinearRegression()    #obje
lr.fit(X_train, Y_train) # verileri model olarak gostermesi icin fit gerekli

tahmin = lr.predict(X_test)

















