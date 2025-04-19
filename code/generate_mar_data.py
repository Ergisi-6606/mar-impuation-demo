# -*- coding: utf-8 -*-
"""

"""


# generate_mar_data.py

import pandas as pd
import numpy as np

def generate_mar_bootstrap(data, n_obs, missing_rate, dependent_col,
                           mar_covariate, iteration, random_seed):
    """
    Generate a bootstrap sample with MAR (Missing At Random) mechanism
    in the dependent variable based on a covariate.
    """
    rss = random_seed + iteration
    boot = data.sample(n=n_obs, random_state=rss, replace=True).reset_index(drop=True)
    boot = boot.sort_values(by=mar_covariate, ascending=True)
    n_missing = int(n_obs * missing_rate)
    missing_indices = list(boot.index)[:n_missing]
    boot["y_comp"] = boot[dependent_col]
    boot.loc[missing_indices, dependent_col] = np.nan
    boot["y_miss"] = boot[dependent_col].isna()
    reordered_cols = list(data.columns) + ["y_miss", "y_comp"]
    boot = boot[reordered_cols].sort_index()
    return boot

#%%opsiyonel olarak deneme yapılabilir.
#if __name__ == "__main__":
#    # 🔹 Veri yolu
#    path_to_data = "../data/diabetes.xlsx"
    
    # 🔹 Veriyi oku
#    df = pd.read_excel(path_to_data)

    # 🔹 Parametreleri buraya sabit yaz
#    mar_sample = generate_mar_bootstrap(
#       data=df,
#        n_obs=400,
#        missing_rate=0.2,
#        dependent_col='Y',
#        mar_covariate='BMI',
#        iteration=1,
#        random_seed=42
#    )

    # 🔹 İlk satırları yazdır
#    print("\n📋 İlk 5 satır:")
#    print(mar_sample.head())
#%%

