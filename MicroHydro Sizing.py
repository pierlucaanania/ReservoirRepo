import numpy as np
import matplotlib.pyplot as plt

def Q(v_jet):        #Q is the flow rate in m^3/s
    pi = np.pi
    d_jet = 0.01   #jet diameter in m
    Cd = 0.98       #discharge coefficient
    return Cd*pi*(d_jet**2)*v_jet/4

def P(v_jet):        #P is the power in W
    rho = 1000       #density of water in kg/m^3
    g = 9.81         #acceleration due to gravity in m/s^2
    return rho*Q(v_jet)*g*v_jet


