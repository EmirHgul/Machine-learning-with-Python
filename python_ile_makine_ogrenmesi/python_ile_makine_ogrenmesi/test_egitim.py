# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:37:32 2024

@author: hatice
"""

# veri setini test ve eğitim olarak ikiye ayırma

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

veriler = pd.read_csv('eksikveriler.csv')

ulke = veriler.iloc[:, 0:1].values

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

cinsiyet = veriler.iloc[:,-1].values


sonuc3 = pd.DataFrame(data= cinsiyet, index = range(22), columns = ["cinsiyet"])
print(sonuc3)

s=pd.concat([sonuc,sonuc2], axis=1)
s2=pd.concat([s,sonuc3], axis=1)
#buraya kadar olan kodlar kategorikVeri_donusumu dosyasından alıntı.

  
# x bağımsız değişken bağımsız değişkenimiz ise hedef değişken olan cinsiyet
# 67% > for train, 33% > for test
# random_state > rastsal sayı üretici
x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0 ) 



# OZNITELIK OLCEKLENDIRME
# 5 farklı turde sutun içeren bu tablomuzu aynı türden ölçeklendirip normal dağılıma uygun hale getirmek istiyoruz.
# Bunun için örneğin hepsinin ortalamasını alsak yine tablolar arası sonuçlar farklı çıkar bu yüzden
# öznitelik ölçeklendirmesi yapıyoruz.

from sklearn.preprocessing import StandardScaler

sc= StandardScaler()

X_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)















