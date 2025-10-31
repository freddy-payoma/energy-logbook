# archivo: grafica_rapida.py
import matplotlib.pyplot as plt

# Datos simples
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear la gráfica
plt.plot(x, y, marker='o', linestyle='-', label='Datos')

# Personalizar
plt.title("Gráfica sencilla")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

# Mostrar
plt.show()
