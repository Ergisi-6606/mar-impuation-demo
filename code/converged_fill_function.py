# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 14:14:38 2025

@author: user
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor

def mapc(a, b):
    return np.mean(abs(b - a) / a)

def linear_fill_converged(verr, max_iter=1000, stop_rounds=200):
    df = verr.copy()
    idx = df[df["y_miss"] == True].index
    df["Y"] = df["Y"].fillna(df["Y"].mean())
    kıyas = -1
    aynı = 0
    say = 0

    while True:
        prev = df.loc[idx, "Y"].values
        model = LinearRegression().fit(df.drop(columns=["Y", "y_miss", "y_comp"]), df["Y"])
        df.loc[idx, "Y"] = model.predict(df.loc[idx, model.feature_names_in_])
        mapc_val = np.round(mapc(prev, df.loc[idx, "Y"].values), 5)
        if kıyas == mapc_val:
            aynı += 1
        else:
            kıyas = mapc_val
            aynı = 0
        if aynı == stop_rounds or say == max_iter:
            break
        say += 1

    return df, say, kıyas

def lasso_fill_converged(verr, max_iter=1000, stop_rounds=200):
    df = verr.copy()
    idx = df[df["y_miss"] == True].index
    df["Y"] = df["Y"].fillna(df["Y"].mean())
    kıyas = -1
    aynı = 0
    say = 0

    while True:
        prev = df.loc[idx, "Y"].values
        model = Lasso(random_state=42).fit(df.drop(columns=["Y", "y_miss", "y_comp"]), df["Y"])
        df.loc[idx, "Y"] = model.predict(df.loc[idx, model.feature_names_in_])
        mapc_val = np.round(mapc(prev, df.loc[idx, "Y"].values), 5)
        if kıyas == mapc_val:
            aynı += 1
        else:
            kıyas = mapc_val
            aynı = 0
        if aynı == stop_rounds or say == max_iter:
            break
        say += 1

    return df, say, kıyas

def decision_fill_converged(verr, max_iter=1000, stop_rounds=200, **tree_params):
    df = verr.copy()
    idx = df[df["y_miss"] == True].index
    df["Y"] = df["Y"].fillna(df["Y"].mean())
    kıyas = -1
    aynı = 0
    say = 0

    while True:
        prev = df.loc[idx, "Y"].values
        model = DecisionTreeRegressor(random_state=42, **tree_params).fit(
            df.drop(columns=["Y", "y_miss", "y_comp"]), df["Y"]
        )
        df.loc[idx, "Y"] = model.predict(df.loc[idx, model.feature_names_in_])
        mapc_val = np.round(mapc(prev, df.loc[idx, "Y"].values), 5)
        if kıyas == mapc_val:
            aynı += 1
        else:
            kıyas = mapc_val
            aynı = 0
        if aynı == stop_rounds or say == max_iter:
            break
        say += 1

    return df, say, kıyas
