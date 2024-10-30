import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up constants and time variable
frequency_components = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]  # Fourier components (odd harmonics for square wave)
amplitudes = [4/(np.pi*n) for n in frequency_components]  # Amplitude of each component (Fourier series)
time = np.linspace(0, 2 * np.pi, 1000)  # Time variable

# Initialize figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
ax1.set_xlim(0, 6 * np.pi)
ax1.set_ylim(-4, 4)
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")
ax2.set_xlim(0, 6 * np.pi)
ax2.set_ylim(-4, 4)
ax2.set_xlabel("Time")
ax2.set_ylabel("Amplitude")

# Initialize lines for sine, cosine, summed signal in first plot
sine_lines = [ax1.plot([], [], lw=1, color=f"C{i}", label=f"Sine component {i+1}")[0] for i in range(len(frequency_components))]
cosine_lines = [ax1.plot([], [], lw=1, linestyle='--', color=f"C{i}", label=f"Cosine component {i+1}")[0] for i in range(len(frequency_components))]
sum_line, = ax1.plot([], [], lw=2, color="black", label="Summed Signal")

# Initialize line for the summed signal in the second plot
resultant_line, = ax2.plot([], [], lw=2, color="black", label="Summed Signal")

# Initialize signal arrays for summing components
y_sum = np.zeros_like(time)

def init():
    # Initialize all lines to empty
    for line in sine_lines + cosine_lines:
        line.set_data([], [])
    sum_line.set_data([], [])
    resultant_line.set_data([], [])
    return sine_lines + cosine_lines + [sum_line, resultant_line]

# Update function for animation
def update(frame):
    y_sum[:frame] = 0
    for i, (freq, amp) in enumerate(zip(frequency_components, amplitudes)):
        y_sine = amp * np.sin(freq * time[:frame])  # Sine component
        y_cosine = amp * np.cos(freq * time[:frame])  # Cosine component
        y_sum[:frame] += y_sine + y_cosine  # Summing both sine and cosine components
        sine_lines[i].set_data(time[:frame], y_sine)  # Update sine component line
        cosine_lines[i].set_data(time[:frame], y_cosine)  # Update cosine component line

    # Update sum line in both plots
    sum_line.set_data(time[:frame], y_sum[:frame])
    resultant_line.set_data(time[:frame], y_sum[:frame])
    return sine_lines + cosine_lines + [sum_line, resultant_line]

# Create animation
ani = FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, interval=20)

# Display the animation
ax1.legend(loc="upper right")
ax1.set_title("Fourier Series Approximation with Sine and Cosine Components")
ax2.set_title("Resultant Summed Signal")
plt.tight_layout()
plt.show()
