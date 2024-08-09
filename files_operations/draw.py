import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create a new figure
fig, ax = plt.subplots(figsize=(6, 6), facecolor='white')

# Set limits and aspect ratio
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal', 'box')

# Create the gradient background
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
ax.imshow(gradient, extent=[-1.2, 1.2, -1.2, 1.2], origin='lower', cmap='coolwarm', alpha=0.6)

# Create the clock circle
circle = patches.Circle((0, 0), 1, edgecolor='none', facecolor='white', zorder=2)
ax.add_patch(circle)

# Draw the hour, minute, and second hands
hour_hand = patches.FancyArrow(0, 0, 0.5 * np.cos(np.pi/3), 0.5 * np.sin(np.pi/3), width=0.05, color='gray', zorder=3)
minute_hand = patches.FancyArrow(0, 0, 0.7 * np.cos(np.pi/6), 0.7 * np.sin(np.pi/6), width=0.03, color='gray', zorder=3)
second_hand = patches.FancyArrow(0, 0, 0.9 * np.cos(np.pi/2), 0.9 * np.sin(np.pi/2), width=0.01, color='red', zorder=4)

ax.add_patch(hour_hand)
ax.add_patch(minute_hand)
ax.add_patch(second_hand)

# Remove axes
ax.axis('off')

# Display the plot
plt.show()