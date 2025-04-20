import matplotlib.pyplot as plt
import numpy as np

# Generate x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)  # Compute sine values

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)

# Add title and labels
plt.title('Sine Wave')
plt.xlabel('x values (radians)')
plt.ylabel('sin(x)')

# Add grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
