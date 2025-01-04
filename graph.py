import matplotlib.pyplot as plt
import numpy as np

# define constants for mario + standard kart
vmax1 = 10  # maximum speed (m/s)
a1 = 5      # acceleration (m/s^2)
t1_1 = vmax1 / a1  # time to reach maximum speed (s)
T = 30      # total race duration (s)

# define constants for bowser + steel driver
vmax2 = 14  # maximum speed (m/s)
a2 = 2      # acceleration (m/s^2)
t1_2 = vmax2 / a2  # time to reach maximum speed (s)

# create time arrays for the two combinations
# combination 1: mario + standard kart
time_acceleration1 = np.linspace(0, t1_1, 100)
time_constant1 = np.linspace(t1_1, T, 100)
velocity_acceleration1 = a1 * time_acceleration1
velocity_constant1 = vmax1 * np.ones_like(time_constant1)

time1 = np.concatenate([time_acceleration1, time_constant1])
velocity1 = np.concatenate([velocity_acceleration1, velocity_constant1])

# combination 2: bowser + steel driver
time_acceleration2 = np.linspace(0, t1_2, 100)
time_constant2 = np.linspace(t1_2, T, 100)
velocity_acceleration2 = a2 * time_acceleration2
velocity_constant2 = vmax2 * np.ones_like(time_constant2)

time2 = np.concatenate([time_acceleration2, time_constant2])
velocity2 = np.concatenate([velocity_acceleration2, velocity_constant2])

# calculate displacements
D1_acceleration = 0.5 * a1 * t1_1**2
D1_constant = vmax1 * (T - t1_1)
D1_total = D1_acceleration + D1_constant

D2_acceleration = 0.5 * a2 * t1_2**2
D2_constant = vmax2 * (T - t1_2)
D2_total = D2_acceleration + D2_constant

# plot the velocity-time graph
plt.figure(figsize=(10, 6))
plt.plot(time1, velocity1, label=f"Mario + Standard Kart (Total: {D1_total:.2f} M)", color="darkorange", linewidth=1.5)
plt.plot(time2, velocity2, label=f"Bowser + Steel Driver (Total: {D2_total:.2f} M)", color="green", linewidth=1.5)

# shade the areas under the curves
plt.fill_between(time_acceleration1, velocity_acceleration1, color="red", alpha=0.3, label=f"Mario D1: {D1_acceleration:.2f} M")
plt.fill_between(time_constant1, velocity_constant1, color="blue", alpha=0.3, label=f"Mario D2: {D1_constant:.2f} M")
plt.fill_between(time_acceleration2, velocity_acceleration2, color="lime", alpha=0.3, label=f"Bowser D1: {D2_acceleration:.2f} M")
plt.fill_between(time_constant2, velocity_constant2, color="cyan", alpha=0.3, label=f"Bowser D2: {D2_constant:.2f} M")

# add labels, title, and legend
plt.title("Velocity-Time Graph: Combination Comparison", fontsize=14, pad=12)
plt.xlabel("Time (Seconds)", fontsize=12, labelpad=10)
plt.ylabel("Velocity (M/S)", fontsize=12, labelpad=10)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.7)
plt.axvline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.7)

# adjust grid, legend, and layout
plt.grid(alpha=0.3)
plt.legend(fontsize=10, loc="lower right")
plt.tight_layout()

# show the graph
plt.show()