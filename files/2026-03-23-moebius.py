# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:10:45 2026

@author: x372924
"""

import numpy as np
import matplotlib.pyplot as plt


def mpg(z):
    # return ((10 + 6*1j)*z - 12*1j)/(3*1j*z - 6*1j + 5)
    return((5*1j-23)*z - 25+11*1j)/((7*1j-5)*z - 3+1j)


# LINE STUFF
# parameter for the curves
t = np.linspace(-10, 10, 500)
# Kurven in der z-Ebene
# zs = [0.5*t+1j*t, 0.3*t+1-0.5*1j*t]



# CIRCLE STUFF
# parameter for the curves
# t = np.linspace(-np.pi, np.pi, 500)
# zs = [0.5*np.cos(t) + 0.5*1j*np.sin(t), np.cos(t) + 1j*np.sin(t), 2*np.cos(t) + 2*1j*np.sin(t), 1 + 0.5*np.cos(t) + 1j + 0.5*1j*np.sin(t)]
zs = [np.cos(t) + 1j*np.sin(t)]



ws = [mpg(z) for z in zs]



# Plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# z-plane (left)
for i in range(len(zs)):
    ax1.plot(np.real(zs[i]), np.imag(zs[i]))
    ax1.set_xlabel('Re(z)')
    ax1.set_ylabel('Im(z)')
    ax1.grid(True)
    ax1.legend()
    ax1.axis('equal')

# w-plane (right)
for i in range(len(ws)):
    ax2.plot(np.real(ws[i]), np.imag(ws[i]))
    ax2.set_xlabel('Re(w)')
    ax2.set_ylabel('Im(w)')
    ax2.grid(True)
    ax2.legend()
    ax2.axis('equal')

plt.tight_layout()
plt.show()