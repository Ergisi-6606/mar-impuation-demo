
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error as MSE

def mapc(a, b):
    return np.mean(abs(b - a) / a)

def lin_reg(verr):
    atama_sonuc = pd.DataFrame(columns=['mse', "model"])
    tekrar_say = 200
    df = verr.copy()
    idx = df[df.y_miss == True].index
    df["Y"] = df["Y"].fillna(df["Y"].mean())
    say = 0
    kıyas = -1
    aynı = 0
    while True:
        X = df[['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']]
        y = df["Y"]
        prev_iter = df.loc[idx, "Y"].values
        model = LinearRegression().fit(X, y)
        dfp = df.loc[idx, X.columns]
        pred = model.predict(dfp)
        df.loc[idx, "Y"] = pred
        if kıyas == np.round(mapc(prev_iter, pred), 5):
            aynı += 1
        else:
            kıyas = np.round(mapc(prev_iter, pred), 5)
            aynı = 0
        if aynı == tekrar_say or say == 1000:
            atama_sonuc.loc[0, "mse"] = MSE(verr.loc[idx, "y_comp"].values, pred)
            atama_sonuc.loc[0, "model"] = "lin"
            break
        say += 1
    return atama_sonuc

def dec_reg(verr):
    atama_sonuc = pd.DataFrame(columns=['mse', "model"])
    tekrar_say = 200
    df = verr.copy()
    idx = df[df.y_miss == True].index
    df["Y"] = df["Y"].fillna(df["Y"].mean())
    say = 0
    kıyas = -1
    aynı = 0
    while True:
        X = df[['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']]
        y = df["Y"]
        prev_iter = df.loc[idx, "Y"].values
        model = DecisionTreeRegressor().fit(X, y)
        dfp = df.loc[idx, X.columns]
        pred = model.predict(dfp)
        df.loc[idx, "Y"] = pred
        if kıyas == np.round(mapc(prev_iter, pred), 5):
            aynı += 1
        else:
            kıyas = np.round(mapc(prev_iter, pred), 5)
            aynı = 0
        if aynı == tekrar_say or say == 1000:
            atama_sonuc.loc[0, "mse"] = MSE(verr.loc[idx, "y_comp"].values, pred)
            atama_sonuc.loc[0, "model"] = "dec"
            break
        say += 1
    return atama_sonuc

def las_reg(verr):
    atama_sonuc = pd.DataFrame(columns=['mse', "model"])
    tekrar_say = 200
    df = verr.copy()
    idx = df[df.y_miss == True].index
    df["Y"] = df["Y"].fillna(df["Y"].mean())
    say = 0
    kıyas = -1
    aynı = 0
    while True:
        X = df[['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']]
        y = df["Y"]
        prev_iter = df.loc[idx, "Y"].values
        model = Lasso().fit(X, y)
        dfp = df.loc[idx, X.columns]
        pred = model.predict(dfp)
        df.loc[idx, "Y"] = pred
        if kıyas == np.round(mapc(prev_iter, pred), 5):
            aynı += 1
        else:
            kıyas = np.round(mapc(prev_iter, pred), 5)
            aynı = 0
        if aynı == tekrar_say or say == 1000:
            atama_sonuc.loc[0, "mse"] = MSE(verr.loc[idx, "y_comp"].values, pred)
            atama_sonuc.loc[0, "model"] = "lasso"
            break
        say += 1
    return atama_sonuc
