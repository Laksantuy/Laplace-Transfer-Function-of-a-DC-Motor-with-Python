# Implementasi Python untuk Menentukan Fungsi Alih Motor DC Menggunakan Transformasi Laplace
## Laksana Aura Ibrahim | 235150300111032

## 📌 Deskripsi Proyek
Proyek ini berfokus pada analisis sistem **Motor DC**, mencakup perumusan **model matematis**, penerapan **Transformasi Laplace**, dan penentuan **Fungsi Alih (Transfer Function)**.

Kode dalam repositori ini ditulis dalam **Python** untuk menyelesaikan persamaan diferensial yang menggambarkan dinamika Motor DC.

---

## ⚙️ 1. Model Matematika
**Persamaan Listrik dan Mekanik:**  
Model Matematis Listrik dan juga Mekanik yang terdapat pada motor DC dapat kita modelkan seperti pada gambar berikut ini:
![model listrik dan mekanik](https://github.com/user-attachments/assets/e1e41306-838c-46a8-84a5-de17d08b51bd) 

Sehingga kita dapat implementasikan persamaan tersebut dalam python menggunakan sympy.

### 📌 Implementasi di Python:
```python
import sympy as sp

# Definisi variabel simbolik
t, s = sp.symbols('t s')
L, R, V, K, J, b = sp.symbols('L R V K J b')  # Parameter sistem
I, omega = sp.Function('I')(t), sp.Function('omega')(t)  # Variabel waktu

# Persamaan diferensial listrik dan mekanik
eq1 = sp.Eq(L * I.diff(t) + R * I - V + K * omega, 0)  # Listrik
eq2 = sp.Eq(J * omega.diff(t) + b * omega + K * I, 0)  # Mekanik
```
- Pertama kita import library sympy
- Kemudian kita definisikan simbol-simbol yang digunakan dalam model matematis Motor DC
- Setelah itu kita tuliskan persamaan untuk model listrik (eq1) dan persamaan untuk model mekanik (eq2)
- Sehingga, setelah kita print (dengan sp.pprint()) kita akan dapatkan output berupa model matematis listrik dan juga mekanik untuk Motor DC seperti berikut:
  
#### Output
```python
>>> == Model Matematika Motor DC ===
>>> Model Listrik: 
>>>                 d                        
>>> K*omega(t) + L*--(I(t)) + R*I(t) - V = 0
>>>                dt    
>>> Model Mekanik:
>>>    d                                     
>>> J*--(omega(t)) - K*I(t) + b*omega(t) = 0
>>>   dt  
```
---

## 🔄 2. Transformasi Laplace
Menggunakan **Transformasi Laplace**, persamaan diferensial dapat diubah menjadi domain **s**
Sehingga kita dapatkan persamaan untuk model listrik dan mekanik seperti berikut:

![model listrik dan mekanik laplace](https://github.com/user-attachments/assets/155f6be5-6fec-4c50-9e92-12368e074308)

Adapun untuk implementasinya dalam python dapat kita lakukan dengan kode seperti berikut:

### 📌 Implementasi di Python:
```python
# Transformasi Laplace (dengan kondisi awal nol)
I_s, Omega_s, V_s = sp.symbols('I_s Omega_s V_s')
eq1_Laplace = eq1.subs({I.diff(t): s * I_s, I: I_s, omega: Omega_s, V: V_s})
eq2_Laplace = eq2.subs({omega.diff(t): s * Omega_s, omega: Omega_s, I: I_s})
```
- Pertama kita definisikan simbol matematis dengan domain s
- kemudian kita substitusikan untuk setiap diferensial di dalam persamaan, baik persamaan listrik ataupun mekanik
- Sehingga kita dapatkan output persamaan transformasi laplace seperti berikut ini:

#### Output
```python
>>> === Transformasi Laplace ===
>>> Model Listrik:
>>> I_s*L*s + I_s*R + K*Omega_s - V_s = 0
>>> Model Mekanik:
>>> -I_s*K + J*Omega_s*s + Omega_s*b = 0
```
---

## 📊 3. Transfer Function
Untuk menemukan Transfer Function, secara matematis dapat kita lakukan dalam empat langkah.
Adapun tiga langkah pertama adalah:
- Pecahkan untuk Is dari persamaan Laplace Mekanik
- Substitusi Is tersebut ke dalam persamaan Laplace Listrik
- Pecahkan untuk Omega_s dari persamaan yang didapatkan setelah substitusi

Langkah-langkahnya secara detil dapat dituliskan seperti berikut:
![transfer function 1](https://github.com/user-attachments/assets/d84e33fe-4ec6-43c6-8d00-e2af1dcd2ffa)
![transfer function 2](https://github.com/user-attachments/assets/25058697-6464-4b25-b712-bee8c85201a6)

Kemudian langkah terakhir adalah dengan menemukan transfer function G(s) dengan:
G(s) = Omega(s) / V(s)
Yang dapat kita tuliskan seperti berikut:
![transfer function 3](https://github.com/user-attachments/assets/6655fcd4-6e58-4f69-99bc-a72456fda924)

Adapun implementasinya dalam python dapat kita tulis kodenya seperti berikut:

### 📌 Implementasi di Python:
```python
# Pecahkan I_s dari eq2_Laplace
I_s_sol = sp.solve(eq2_Laplace, I_s)[0]

# Substitusi I_s ke dalam eq1_Laplace
eq1_substituted = eq1_Laplace.subs(I_s, I_s_sol)

# Pecahkan Omega_s dalam bentuk V_s
Omega_s_sol = sp.solve(eq1_substituted, Omega_s)[0]

# Fungsi Alih G(s) = Omega(s) / V(s)
G_s = sp.simplify(Omega_s_sol / V_s)
```
- Pertama kita pecahkan I_s dari eq2_laplace
- Kemudian kita substitusikan I_s tersebut kedalam eq1_laplace
- kemudian kita pecahkan omega_s dari persamaan eq1_substituted
- Kemudian terakhir kita tentukan transfer function dengan G(s) = Omega(s) / V(s)

Sehingga kita dapatkan output seperti berikut:
#### Output
```python
>>> === Fungsi Alih G(s) ===
>>>                 K                
>>> ---------------------------------
>>>      2            2              
>>> J*L*s  + J*R*s + K  + L*b*s + R*b
```

## 📝 4. Print dengan Pretty Print
Dengan menggunakan bantuan syntax pretty print (sp.pprint()) yang terdapat dalam library sympy, kita dapat menampilkan semua persamaan yang kita dapatkan dari program dengan rapi dan enak dilihat.

Adapun implementasinya dapat dituliskan seperti berikut:
```python
print("=== Model Matematika Motor DC ===")
print("Model Listrik: ")
sp.pprint(eq1) # Model Listrik
print("Model Mekanik: ")
sp.pprint(eq2) # Model Mekanik
sp.pprint("\n=== Transformasi Laplace ===")
print("Model Listrik: ") 
sp.pprint(eq1_Laplace) # Model Listrik
print("Model Mekanik: ")
sp.pprint(eq2_Laplace) # Model Mekanik

sp.pprint("\n=== Fungsi Alih G(s) ===")
sp.pprint(G_s)
```
#### Output
```python
>>> === Model Matematika Motor DC ===
>>> Model Listrik: 
>>>                d                        
>>> K*omega(t) + L*--(I(t)) + R*I(t) - V = 0
>>>                dt                       
>>> Model Mekanik: 
>>>   d                                     
>>> J*--(omega(t)) - K*I(t) + b*omega(t) = 0
>>>   dt                                    
>>>                             
>>> === Transformasi Laplace ===
>>> Model Listrik: 
>>> I_s*L*s + I_s*R + K*Omega_s - V_s = 0
>>> Model Mekanik: 
>>> -I_s*K + J*Omega_s*s + Omega_s*b = 0
>>>                         
>>> === Fungsi Alih G(s) ===
>>>                 K                
>>> ---------------------------------
>>>      2            2              
>>> J*L*s  + J*R*s + K  + L*b*s + R*b
```

## 📃 Kesimpulan
Dalam proyek Python ini, kita telah:
- Menentukan model matematis motor DC dan mengimplementasikannya dalam python
- Menentukan transformasi laplace dari model matematis tersebut dan mengimplementasikannya dalam python
- Menemukan transfer function dengan perhitungan matematis dan implementasi program pada python
- Memastikan bahwa hasil yang didapatkan dengan perhitungan matematis sama dengan output yang diberikan oleh program python

Alhamdulillah.
