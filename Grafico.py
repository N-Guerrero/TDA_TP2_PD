
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

# Leer archivo y extraer datos
results = {}
with open('tiempos_totales.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        chars = int(parts[0].split(':')[1])
        time = float(parts[1].split(':')[1])
        results[chars] = time

# Preparar datos ordenados
x = np.array(sorted(results.keys()))
y = np.array([results[n] for n in x])

# Ajuste por cuadrados mínimos con función cuadrática
f_teorica = lambda x, c1, c2: c1 * x**2 + c2
c, _ = scipy.optimize.curve_fit(f_teorica, x, y)
y_fit = f_teorica(x, *c)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo', label='Tiempos reales')
plt.plot(x, y_fit, 'r-', label=f'Ajuste teórico: {c[0]:.2e}·n² + {c[1]:.2e}')
plt.xlabel("Cantidad de caracteres")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación entre tiempos reales y tiempo teórico O(n²)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Error cuadrático total
error_total = np.sum((y - y_fit) ** 2)
print(f"Error cuadrático total: {error_total:.6e}")