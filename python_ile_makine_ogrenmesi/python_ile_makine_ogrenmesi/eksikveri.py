# kullanabilecek kaynak web sitesi: bilkav.com
# eksikveriler isimli csv dosyamızın yaş sutununda bulunan eksik verileri ortalama ile tahmin edip doldurduk

import pandas as pd
import numpy as np

veriler = pd.read_csv('eksikveriler.csv')

#sci - kit learn

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

Yas = veriler.iloc[:,1:4].values


imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)









