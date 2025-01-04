import matplotlib.pyplot as plt
import numpy as np

# Define constants
Vmax = 10  # Maximum speed (m/s)
a = 5      # Acceleration (m/s^2)
t1 = Vmax / a  # Time to reach maximum speed (s)
T = 30     # Total race duration (s)

# Create time arrays for the two phases
time_acceleration = np.linspace(0, t1, 100)  # Time for acceleration phase
time_constant = np.linspace(t1, T, 100)      # Time for constant speed phase

# Velocity functions
velocity_acceleration = a * time_acceleration  # v(t) = a * t for acceleration phase
velocity_constant = Vmax * np.ones_like(time_constant)  # v(t) = Vmax for constant speed phase

# Plot the velocity-time graph
plt.figure(figsize=(8, 5))
plt.plot(time_acceleration, velocity_acceleration, label="Acceleration Phase", color="darkorange", linewidth=1.5)
plt.plot(time_constant, velocity_constant, label="Constant Speed Phase", color="royalblue", linewidth=1.5)

# Shade the areas under the curves
plt.fill_between(time_acceleration, velocity_acceleration, color="red", alpha=0.3, label="Displacement (D1)")
plt.fill_between(time_constant, velocity_constant, color="blue", alpha=0.3, label="Displacement (D2)")

# Annotate important points
plt.scatter([0, t1, T], [0, Vmax, Vmax], color="black", s=20, zorder=5)  # Key points (0,0), (t1, Vmax), (T, Vmax)
plt.text(t1 / 2, Vmax / 4, "D1 (10 m)", color="red", fontsize=9, ha="center")
plt.text(t1 + (T - t1) / 2, Vmax / 1.5, "D2 (280 m)", color="blue", fontsize=9, ha="center")

# Add labels, title, and legend
plt.title("Velocity-Time Graph for Mario + Standard Kart", fontsize=12, pad=10)
plt.xlabel("Time (seconds)", fontsize=10, labelpad=8)
plt.ylabel("Velocity (m/s)", fontsize=10, labelpad=8)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.7)
plt.axvline(0, color="black", linewidth=0.8, linestyle="--", alpha=0.7)

# Adjust grid, legend, and layout
plt.grid(alpha=0.3)
plt.legend(fontsize=9, loc="lower right")
plt.tight_layout()

# Show the graph
plt.show()