import numpy as np
import matplotlib.pyplot as plt

# Initialize random_walk
random_walk = [0]
print(random_walk)
print(type(random_walk))

for x in range(100):
    step = random_walk[-1]
    print(step)
    dice = np.random.randint(1, 7)
    print('pierwszyrzut ',dice)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step += 1
    else:
        step += np.random.randint(1, 7)
        print('else',step)

    random_walk.append(step)

# Plot random_walk
print(random_walk)
plt.plot(random_walk)
plt.show()