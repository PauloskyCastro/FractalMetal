import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_metal():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    metal = f.generate()
    # Add noise to the fractal shape to make it look more like metal
    noise = np.random.normal(0, 0.05, metal.shape)
    metal = metal + noise
    metal = np.clip(metal, 0, 1)
    # Apply a metal-like color map to the fractal shape
    metal = plt.cm.cool(metal)
    # Return the fractal metal
    return metal

# Generate 10 fractal metal images
for i in range(10):
    metal = generate_fractal_metal()
    plt.imsave("fractal_metal_{}.png".format(i), metal)
