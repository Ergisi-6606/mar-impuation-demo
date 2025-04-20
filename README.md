# 📊 Iterative Imputation with MAR Missingness (Lasso, Linear, Tree)

Bu proje, BMI değişkenine bağlı olarak MAR (Missing At Random) yapısında eksik veri üretilmesini ve bu eksik verinin Lasso, Doğrusal Regresyon ve Karar Ağacı regresyon modelleri ile **iteratif olarak doldurulmasını** sağlamaktadır.

## 🔧 Kullanılan Dosyalar

| Dosya Adı                        | Açıklama |
|----------------------------------|----------|
| `generate_mar_data.py`           | BMI değişkenine bağlı olarak MAR tipi eksik veri üreten fonksiyonu içerir |
| `converged_fill_function.py`     | Lasso, LinearRegression ve DecisionTree ile convergence kontrollü eksik veri doldurma |
| `iterated_imputed_dataset.py`    | Yukarıdaki modülleri kullanarak 10 farklı bootstrap örneğinde eksik veriyi tamamlayan ana script |

---

## 🧪 Kullanım Talimatı

1. Bu repoyu klonlayın veya ZIP olarak indirin:
```bash
git clone https://github.com/kullaniciadi/mar-imputation-demo.git

## Klasör Yapısı

mar-imputation-demo/
├── code/
│   ├── generate_mar_data.py
│   ├── converged_fill_function.py
│   └── iterated_imputed_dataset.py
├── data/
│   └── diabetes.xlsx
├── output/
│   └── (istenirse imputasyon sonrası kayıt yapılabilir)
└── README.md


## ✍️ Yazar

**Semih Ergişi**  
PhD in Biostatistics  
Ankara University Faculty of Medicine
