import numpy as np
import matplotlib.pyplot as plt

# Parameters
waveL = 500e-9   # 5 nm
slit_sep = 0.2e-3     # 0.1 mm    # d
slit_width = 0.02e-3  # 0.02 mm   # a
L = 1.6               # 1 meter to screen

# Angle array
theta = np.linspace(-0.04, 0.04, 1000)
beta = np.pi * slit_width * np.sin(theta) / waveL
alpha = np.pi * slit_sep * np.sin(theta) / waveL

# Intensity pattern
I = (np.cos(alpha)**2) * (np.sinc(beta/np.pi)**2)
# sinc(πx) = sin(πx)/(πx), thus beta/π for np.sinc
# Plot
plt.plot(theta, I, color='r')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xticks(np.arange(-0.04, 0.05, 0.01))
plt.title("Double-Slit Interference Pattern")
plt.xlabel("Angle (rad)")
plt.ylabel("Intensity")
plt.show()
