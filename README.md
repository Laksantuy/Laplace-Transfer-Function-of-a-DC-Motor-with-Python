# Analisis Motor DC: Model Matematika, Transformasi Laplace, dan Transfer Function

## 📌 Deskripsi Proyek
Proyek ini berfokus pada analisis sistem **Motor DC**, mencakup perumusan **model matematis**, penerapan **Transformasi Laplace**, dan penentuan **Fungsi Alih (Transfer Function)**.  

Kode dalam repositori ini ditulis dalam **Python/MATLAB** untuk menyelesaikan persamaan diferensial yang menggambarkan dinamika Motor DC.

---

## ⚙️ 1. Model Matematika
Motor DC dapat dimodelkan menggunakan persamaan listrik dan mekanik sebagai berikut:  

**Persamaan Listrik:**  
\[
V(t) = L \frac{di(t)}{dt} + Ri(t) + e(t)
\]
dengan:  
- \(V(t)\) = Tegangan input (Volt)  
- \(i(t)\) = Arus motor (Ampere)  
- \(L\) = Induktansi (Henry)  
- \(R\) = Resistansi (Ohm)  
- \(e(t)\) = Gaya Gerak Listrik (EMF) balik  

**Persamaan Mekanik:**  
\[
J \frac{d\omega(t)}{dt} + B\omega(t) = T(t)
\]
dengan:  
- \(J\) = Momen inersia rotor (kg·m²)  
- \(B\) = Koefisien redaman viskositas (N·m·s)  
- \(\omega(t)\) = Kecepatan sudut (rad/s)  
- \(T(t)\) = Torsi motor (N·m)  

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
#### Output
```python
>>> == Model Matematika Motor DC ===
>>> Model Listrik:  Eq(K*omega(t) + L*Derivative(I(t), t) + R*I(t) - V, 0)
>>> Model Mekanik:  Eq(J*Derivative(omega(t), t) + K*I(t) + b*omega(t), 0)
```
---

## 🔄 2. Transformasi Laplace
Menggunakan **Transformasi Laplace**, persamaan diferensial dapat diubah menjadi domain **s**:  

**Persamaan Listrik (Laplace):**  
\[
V(s) = (Ls + R)I(s) + E(s)
\]

**Persamaan Mekanik (Laplace):**  
\[
(Js + B) \Omega(s) = T(s)
\]

### 📌 Implementasi di Python:
```python
# Transformasi Laplace (dengan kondisi awal nol)
I_s, Omega_s, V_s = sp.symbols('I_s Omega_s V_s')
eq1_Laplace = eq1.subs({I.diff(t): s * I_s, I: I_s, omega: Omega_s, V: V_s})
eq2_Laplace = eq2.subs({omega.diff(t): s * Omega_s, omega: Omega_s, I: I_s})

# Pecahkan I_s dari eq2_Laplace
I_s_sol = sp.solve(eq2_Laplace, I_s)[0]

# Substitusi I_s ke dalam eq1_Laplace
eq1_substituted = eq1_Laplace.subs(I_s, I_s_sol)

# Pecahkan Omega_s dalam bentuk V_s
Omega_s_sol = sp.solve(eq1_substituted, Omega_s)[0]
```
#### Output
```python
>>> === Transformasi Laplace ===
>>> Model Listrik:  Eq(I_s*L*s + I_s*R + K*Omega_s - V_s, 0)
>>> Model Mekanik:  Eq(I_s*K + J*Omega_s*s + Omega_s*b, 0)
```
---

## 📊 3. Transfer Function
Fungsi alih sistem Motor DC diperoleh dari hubungan antara kecepatan sudut **\(\Omega(s)\)** dan tegangan input **\(V(s)\)**:  

\[
G(s) = \frac{\Omega(s)}{V(s)}
\]

Bentuk umum dari transfer function:  
\[
G(s) = \frac{K}{(Js + B)(Ls + R) + K^2}
\]
di mana **\(K\)** adalah konstanta penguatan motor.

### 📌 Implementasi di Python:
```python
# Fungsi Alih G(s) = Omega(s) / V(s)
G_s = sp.simplify(Omega_s_sol / V_s)
```
#### Output
```python
>>> === Fungsi Alih G(s) ===
>>> -K/(J*L*s**2 + J*R*s - K**2 + L*b*s + R*b)
```
