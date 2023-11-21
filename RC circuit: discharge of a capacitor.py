'''RC circuit: discharge of a capacitor'''

'''Math Model: C := Capacitor && R := Resistor
(Using a simple readable math notation)

Vc(0) = V0    
Vr = RI

RI + Vc = 0
Vc = -RI

Capacitor: Q=CVc -> dQdt = CdVcdt -> I = CdVcdt

Vc = -RC dVcdt

dVcdt + (1/RC)Vc = 0

Solution: Vc(t) = V0*e^(-t/RC)
'''

###

import numpy as np
import matplotlib.pyplot as plt

###

'''Values'''

C = 0.01
R = 7
tau = R*C
V0 = 1
t_0 = 0
t_end = 1
t = np.linspace(t_0,t_end,100)

###

''' dVcdt + (1/RC)Vc = 0 
    dVcdt = -tau*Vc  || tau = a && Vc = b 
'''

f = lambda a,b : -a/b

V = np.zeros(len(t))
V[0] = V0

'''Euler Method'''

for i in range(1,len(t)):
    V[i] = V[i-1] + f(V[i-1],tau)*(t[i]-t[i-1])

###

plt.figure(1)
plt.title(' RC Circuit: Discharge of a Capacitor')
plt.xlabel('Time [s]')
plt.ylabel('Capacitor Voltage [V]')
plt.plot(t,V)
plt.show()

plt.figure(2)
plt.title(' RC Circuit: Discharge of a Capacitor')
plt.xlabel('Time [s]')
plt.ylabel('Current [A]')
plt.plot(t,V/R)
plt.show()

