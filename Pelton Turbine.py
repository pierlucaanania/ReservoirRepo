import math

class PeltonTurbine:
    def __init__(self, nozzle_diameter, runner_diameter, efficiency):
        self.nozzle_diameter = nozzle_diameter  # Diametro ugello
        self.runner_diameter = runner_diameter  # Diametro girante
        self.efficiency = efficiency  # Efficienza della turbina (0-1)

    def calculate_power(self, water_flow_rate, water_head):
        # Calcola la velocità dell'acqua uscente dall'ugello (m/s)
        water_velocity = math.sqrt(2 * 9.81 * water_head)

        # Calcola la velocità tangenziale della girante (m/s)
        runner_velocity = water_velocity * math.sin(math.radians(160))  # 160 gradi tipici

        # Calcola la potenza meccanica generata (Watt)
        mechanical_power = 0.5 * water_flow_rate * runner_velocity**2

        # Calcola la potenza elettrica generata (Watt)
        electrical_power = mechanical_power * self.efficiency

        return electrical_power

# Parametri della turbina
nozzle_diameter = 0.05  # metri
runner_diameter = 0.2   # metri
efficiency = 0.85       # Efficienza

# Flusso d'acqua e altezza
water_flow_rate = 0.01  # metri cubi al secondo
water_head = 100         # metri

# Creazione dell'oggetto turbina
turbine = PeltonTurbine(nozzle_diameter, runner_diameter, efficiency)

# Calcolo della potenza generata
power_generated = turbine.calculate_power(water_flow_rate, water_head)
print(f"Potenza generata: {power_generated:.2f} Watt")
