from pathlib import Path

# Kod içeriğini tekrar oluştur

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "code"))

from model_func_limited import lin_reg, dec_reg, las_reg
from converged_fill_function import lasso_fill_converged, linear_fill_converged, decision_fill_converged
from generate_mar_data import generate_mar_bootstrap

data_path = os.path.join(BASE_DIR, "data", "diabetes.xlsx")
veri = pd.read_excel(data_path)
scaler = StandardScaler()
veri[['AGE','BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5','S6']] = scaler.fit_transform(
    veri[['AGE','BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5','S6']]
)

n1 = 420
m_o = 0.10
rss = 70000
mn = 1
mx = 11

# Lasso imputasyonu
lasso_sonuc = {}
for i in range(mn, mx):
    daa = generate_mar_bootstrap(veri, n1, m_o, "Y", "BMI", i, rss)
    converged_df, toplam_iterasyon, son_mapc = lasso_fill_converged(daa)
    lasso_sonuc[i] = [converged_df, toplam_iterasyon, son_mapc]

# Linear imputasyonu
linear_sonuc = {}
for i in range(mn, mx):
    daa = generate_mar_bootstrap(veri, n1, m_o, "Y", "BMI", i, rss)
    converged_df, toplam_iterasyon, son_mapc = linear_fill_converged(daa)
    linear_sonuc[i] = [converged_df, toplam_iterasyon, son_mapc]

# Decision Tree imputasyonu
decision_sonuc = {}
for i in range(mn, mx):
    daa = generate_mar_bootstrap(veri, n1, m_o, "Y", "BMI", i, rss)
    df_dec, iter_dec, mapc_dec = decision_fill_converged(
        daa,
        max_depth=9,
        max_features='sqrt',
        max_leaf_nodes=90,
        min_samples_leaf=10,
        min_weight_fraction_leaf=0.1,
        splitter='best'
    )
    decision_sonuc[i] = [df_dec, iter_dec, mapc_dec]

# Örnek çıktı
# Aşağıdaki kod yardımıyla impute edilmiş veri setleri ekrana yazdırılabilir. 
# Below cen be used to impute dataset and written in the console.  
# To get iteration number and convergence values, [0] can be changed to [1] and [2]
for i in range(1, 11):
    print("Lasso:")
    print(lasso_sonuc[i][0].iloc[:, :-2])
    print("Linear:")
    print(linear_sonuc[i][0].iloc[:, :-2])
    print("Decision Tree:")
    print(decision_sonuc[i][0].iloc[:, :-2])








