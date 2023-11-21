import numpy as np
import matplotlib.pyplot as plt

# Parametri del pannello fotovoltaico
tensione_nominale = 36.0  # Volt
corrente_di_cortocircuito = 9.0  # Ampere
tensione_di_circuito_aperto = 44.0  # Volt

# Genera un array di valori di tensione nel range da 0 a tensione_di_circuito_aperto con incrementi di 1 Volt
tensione_array = np.arange(0, tensione_di_circuito_aperto + 1, 1)

# Calcola la corrente per ogni valore di tensione utilizzando l'equazione della caratteristica I-V di un pannello fotovoltaico
corrente_array = corrente_di_cortocircuito - (corrente_di_cortocircuito / tensione_di_circuito_aperto) * tensione_array

# Calcola la potenza per ogni coppia di valori di tensione e corrente
potenza_array = tensione_array * corrente_array

# Crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(tensione_array, potenza_array, label='Curva Potenza-Corrente')
plt.xlabel('Tensione (V)')
plt.ylabel('Potenza (W)')
plt.title('Curva Potenza-Corrente di un Pannello Fotovoltaico')
plt.legend()
plt.grid(True)
plt.show()
