#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Plot the rectangular coordinates

plt.subplot(121)

x = np.linspace(-np.pi, np.pi, 300)

y1 = np.sin (x)
y2 = (np.sin (x)) ** 2
y3 = np.cos (x)

plt.plot(x, y1, "r", label = "$y_1 = sinx$")
plt.plot(x, y2, "b", label = "$y_2 = sin^2x$") 
plt.plot(x, y3, "g", label = "$y_3 = cosx$")

plt.legend(loc = "lower left")

# Plot the polar coordinates

plt.subplot(122, polar = True)

x = np.linspace(0, 2 * np.pi, 300)

y1 = np.sin (x)
y2 = (np.sin (x)) ** 2
y3 = np.cos (x)

plt.plot(x, y1, "r", label = "$y_1 = sinx$")
plt.plot(x, y2, "b", label = "$y_2 = sin^2x$") 
plt.plot(x, y3, "g", label = "$y_3 = cosx$")

plt.legend(loc = "lower left")

plt.suptitle("Trigonometry Functions")
plt.savefig('trigomometryFunctions.pdf')
plt.show()