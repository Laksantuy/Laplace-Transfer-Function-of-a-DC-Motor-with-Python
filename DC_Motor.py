import sympy as sp

# Definisi variabel simbolik
t, s = sp.symbols('t s')
L, R, V, K, J, b = sp.symbols('L R V K J b')  # Parameter sistem
I, omega = sp.Function('I')(t), sp.Function('omega')(t)  # Variabel waktu

# Persamaan diferensial listrik dan mekanik
eq1 = sp.Eq(L * I.diff(t) + R * I - V + K * omega, 0)  # Listrik
eq2 = sp.Eq(J * omega.diff(t) + b * omega + K * I, 0)  # Mekaniks

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

# Fungsi Alih G(s) = Omega(s) / V(s)
G_s = sp.simplify(Omega_s_sol / V_s)

# Tampilkan hasil
print("=== Model Matematika Motor DC ===")
print("Model Listrik: ", eq1)
print("Model Mekanik: ", eq2)

print("\n=== Transformasi Laplace ===")
print(eq1_Laplace)
print(eq2_Laplace)

print("\n=== Fungsi Alih G(s) ===")
print(G_s)