# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:28:50 2024

@author: hatice
"""

# KATEGORİK VERİLERİ BİLGİSAYAR DİLİNE ÇEVİRME


import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer

veriler = pd.read_csv('eksikveriler.csv')

ulke = veriler.iloc[:, 0:1].values
print(ulke)

# label encoding gösterimi  

le = preprocessing.LabelEncoder()  
ulke[:, 0] = le.fit_transform(veriler.iloc[:, 0])
print(ulke)

# one hot encoding gösterimi
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)
 

# one hot encoding gösterimindeki kolonların isimlerini ülkelerin isimleri ile değiştirdik.
print(list(range(22)))
sonuc = pd.DataFrame(data=ulke, index = range(22), columns= ["fr","tr","us"])
print(sonuc)

# bu aşamadan sonra yapılan bütün değişiklikleri tek bir dataframe'de topladık.

Yas = veriler.iloc[:, 1:4].values

sonuc2 = pd.DataFrame(data=Yas, index = range(22), columns = ["boy","kilo","Yas"])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data= cinsiyet, index = range(22), columns = ["cinsiyet"])
print(sonuc3)

s=pd.concat([sonuc,sonuc2], axis=1)
s2=pd.concat([s,sonuc3], axis=1)
print(s2)
























