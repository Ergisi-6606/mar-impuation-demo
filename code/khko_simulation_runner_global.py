import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import sys
import os

# Çalışma dizinini otomatik olarak ayarla (GitHub için dinamik yol)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "code"))

from model_func_limited import lin_reg, dec_reg, las_reg
from generate_mar_data import generate_mar_bootstrap

# Veri dosyasını oku ve ölçekle
data_path = os.path.join(BASE_DIR, "data", "diabetes.xlsx")
veri = pd.read_excel(data_path)
scaler = StandardScaler()
veri[['AGE','BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5','S6']] = scaler.fit_transform(
    veri[['AGE','BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5','S6']]
)

# Parametreler
n1 = 50
m_o = 0.25
rss = 50000
mn = 1
mx = 1001

deneme = []

for i in range(mn, mx):
    daa = generate_mar_bootstrap(veri, n_obs=n1, missing_rate=m_o,
                                 dependent_col="Y", mar_covariate="BMI",
                                 iteration=i, random_seed=rss)
    ortal = daa["y_comp"].mean()
    las = las_reg(daa).values.tolist()[0]
    dec = dec_reg(daa).values.tolist()[0]
    lin = lin_reg(daa).values.tolist()[0]
    deneme.append([lin, las, dec, ortal])
    print(i, "nolu döngü bitti")

# Sonuçları DataFrame'e çevir ve KHKO hesapla
df_25 = pd.DataFrame(np.concatenate(deneme), columns=["mse", "model", "ortal"])
df_25["oran"] = "%25"
df_25["rmse"] = np.sqrt(df_25["mse"])
df_25["rmse"] = df_25["rmse"].astype("float").round(1)
df_25["khko_deg"] = (df_25["rmse"] / df_25["ortal"].astype("float")).round(1)
df_25.drop(["mse", "ortal"], axis=1, inplace=True)

# CSV olarak kaydet
output_path = os.path.join(BASE_DIR, "output", "sonucden25_1.csv")
df_25.to_csv(output_path, index=False)
