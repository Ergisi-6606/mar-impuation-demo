# MAR Imputation Example

Bu proje, BMI değişkenine bağlı olarak MAR (Missing At Random) eksiklik yapısı oluşturulmuş bir veri seti üretmek ve bu yapıyı bootstrap örneklemesiyle analiz etmek amacıyla hazırlanmıştır.

## 📁 Klasör Yapısı

```
mar-imputation-demo/
├── data/
│   └── diabetes.xlsx
├── code/
│   └── generate_mar_data.py
└── README.md
```

## 💡 Açıklama

`generate_mar_data.py` dosyası:

- Orijinal veri setini okur (`data/diabetes.xlsx`)
- BMI değişkenine bağlı olarak bağımlı değişken `Y`'de %20 oranında MAR tipi eksiklik oluşturur
- Eksiklik öncesi gerçek Y değerlerini `y_comp` kolonunda saklar
- Eksik değerlerin olduğu satırları `y_miss` kolonunda True/False olarak işaretler

## 🧪 Kullanım

Kodun çalışması için Python 3 ve `pandas`, `numpy` kütüphaneleri yüklü olmalıdır.

```bash
python code/generate_mar_data.py
```

Çalıştırıldığında ilk 5 satır ekrana yazdırılır.

## ✍️ Yazar

**Semih Ergişi**  
PhD Student in Biostatistics  
Ankara University Faculty of Medicine
