## 💡 Açıklamalar

### `generate_mar_data.py`:
- Verilen veri setinde BMI değişkenine bağlı olarak bağımlı değişken `Y` için MAR yapısında eksiklik oluşturur.
- `y_comp`: Eksiklik öncesi gerçek değerler
- `y_miss`: Eksik olan gözlemler (True/False olarak)

### `model_func_limited.py`:
- İteratif olarak çalışan 3 farklı regresyon modeli içerir:
  - Linear Regression
  - Lasso Regression
  - Decision Tree Regression
- Convergence (yakınsama) kontrolü `mapc()` fonksiyonu ile yapılır.

### `khko_simulation_runner_global.py`:
- 1000 bootstrap örneğiyle MAR veriler üretir.
- Yukarıdaki modellerle imputasyon yapar.
- RMSE ve KHKO değerlerini hesaplar.
- Sonuçları `output/sonucden25_1.csv` dosyasına kaydeder.

## 🧪 Kullanım

Öncelikle aşağıdaki kütüphanelerin kurulu olması gerekir:

```bash
pip install pandas numpy scikit-learn


## ✍️ Yazar

**Semih Ergişi**  
PhD in Biostatistics  
Ankara University Faculty of Medicine
