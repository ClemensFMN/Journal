#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:53:11 2026

@author: cnovak
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameter für die Kurven
t = np.linspace(-np.pi, np.pi, 500)


# Kurven in der z-Ebene
z1 = 0.5*(np.cos(t) + 1j*np.sin(t))
z2 = 1.0*(np.cos(t) + 1j*np.sin(t))
z3 = 1.5*(np.cos(t) + 1j*np.sin(t))

# Mapping w = e^z
w1 = np.exp(z1)
w2 = np.exp(z2)
w3 = np.exp(z3)

# Plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# z-Ebene (links)
ax1.plot(np.real(z1), np.imag(z1))
ax1.plot(np.real(z2), np.imag(z2))
ax1.plot(np.real(z3), np.imag(z3))
ax1.set_xlabel('Re(z)')
ax1.set_ylabel('Im(z)')
ax1.grid(True)
ax1.legend()
ax1.axis('equal')

# w-Ebene (rechts)
ax2.plot(np.real(w1), np.imag(w1))
ax2.plot(np.real(w2), np.imag(w2))
ax2.plot(np.real(w3), np.imag(w3))
ax2.set_xlabel('Re(w)')
ax2.set_ylabel('Im(w)')
ax2.grid(True)
ax2.legend()
ax2.axis('equal')

plt.tight_layout()
plt.show()
