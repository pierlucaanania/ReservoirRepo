import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Parametri del profilo NACA0012
m = 0.0  # Linea media
p = 0.0  # Posizione del massimo spessore
t = 0.12  # Spessore percentuale

# Punti sulla superficie superiore e inferiore del profilo
num_points = 100
theta = np.linspace(0, np.pi, num_points)
x_upper = 0.5 * (1 - np.cos(theta))
x_lower = 0.5 * (1 - np.cos(theta))
y_upper = t / 0.2 * (0.2969 * np.sqrt(
    x_upper) - 0.1260 * x_upper - 0.3516 * x_upper ** 2 + 0.2843 * x_upper ** 3 - 0.1015 * x_upper ** 4)
y_lower = -t / 0.2 * (0.2969 * np.sqrt(
    x_lower) - 0.1260 * x_lower - 0.3516 * x_lower ** 2 + 0.2843 * x_lower ** 3 - 0.1015 * x_lower ** 4)

# Punti sulla superficie completa del profilo
x = np.concatenate((x_upper, x_lower[::-1]))
y = np.concatenate((y_upper, y_lower[::-1]))


# Metodo dei pannelli
def build_panels(x, y):
    panels = []
    for i in range(len(x) - 1):
        x0, y0 = x[i], y[i]
        x1, y1 = x[i + 1], y[i + 1]
        panels.append([x0, y0, x1, y1])
    return panels


# Calcolo delle normali
def calculate_normals(panels):
    normals = []
    for panel in panels:
        x0, y0, x1, y1 = panel
        dx = x1 - x0
        dy = y1 - y0
        length = np.sqrt(dx ** 2 + dy ** 2)
        nx = dy / length
        ny = -dx / length
        normals.append([nx, ny])
    return normals


# Soluzione del sistema lineare per il potenziale vorticoso
def solve_system(panels):
    num_panels = len(panels)
    A = np.zeros((num_panels, num_panels))
    b = np.zeros(num_panels)

    for i in range(num_panels):
        xi, yi = panels[i][:2]
        for j in range(num_panels):
            xj, yj = panels[j][:2]
            A[i, j] = np.log(np.sqrt((xi - xj) ** 2 + (yi - yj) ** 2))
        b[i] = -2 * np.pi

    strengths = np.linalg.solve(A, b)
    return strengths


# Calcolo dei coefficienti di pressione
def calculate_pressure_coefficients(panels, strengths, normals):
    num_panels = len(panels)
    cp = np.zeros(num_panels)
    for i in range(num_panels):
        cp[i] = 1 - (strengths[i] / 2.0)
    return cp


# Costruzione dei pannelli
panels = build_panels(x, y)

# Calcolo delle normali
normals = calculate_normals(panels)

# Soluzione del sistema lineare
strengths = solve_system(panels)

# Calcolo dei coefficienti di pressione
cp = calculate_pressure_coefficients(panels, strengths, normals)

# Calcolo delle coordinate dei punti di flusso
num_points = 100
flow_points = np.linspace(0, 1, num_points)
x_flow = np.zeros(num_points)
y_flow = np.zeros(num_points)
for i in range(num_points):
    x_flow[i] = flow_points[i]
    y_flow[i] = 0.0

# Calcolo del campo di velocità
u_freestream = 1.0
u = np.zeros(num_points)
v = np.zeros(num_points)
for i in range(num_points):
    for j in range(len(panels)):
        xi, yi = panels[j][:2]
        xj, yj = x_flow[i], y_flow[i]
        dx = xj - xi
        dy = yj - yi
        r_squared = dx ** 2 + dy ** 2
        u[i] += (strengths[j] / (2 * np.pi)) * (dy / r_squared)
        v[i] += -(strengths[j] / (2 * np.pi)) * (dx / r_squared)
    u[i] += u_freestream

# Plot del profilo alare
plt.figure(figsize=(8, 4))
plt.plot(x, y, color='black')
plt.scatter([panel[0] for panel in panels], [panel[1] for panel in panels], color='red', s=10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Profilo alare NACA0012')
plt.gca().set_aspect('equal')
plt.xlim(0, 1)
plt.ylim(-0.5, 0.5)
plt.gca().invert_yaxis()
plt.show()

# Plot dei coefficienti di pressione
plt.figure(figsize=(8, 4))
plt.plot(x_flow, cp, color='black')
plt.xlabel('x')
plt.ylabel('$C_p$')
plt.title('Coefficiente di Pressione sul Profilo alare NACA0012')
plt.gca().invert_yaxis()
plt.show()

# Plot del campo di velocità
plt.figure(figsize=(8, 4))
plt.plot(x_flow, u, label='U', color='black')
plt.plot(x_flow, v, label='V', linestyle='dashed', color='black')
plt.xlabel('x')
plt.ylabel('Velocità')
plt.title('Campo di Velocità intorno al Profilo alare NACA0012')
plt.legend()
plt.show()
