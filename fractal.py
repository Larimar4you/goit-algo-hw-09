import numpy as np
import matplotlib.pyplot as plt

WIDTH, HEIGHT = 400, 400
MAX_ITER = 50

result = np.zeros((HEIGHT, WIDTH))

for y in range(HEIGHT):
    for x in range(WIDTH):
        re = -2 + (x / WIDTH) * 3
        im = -1.5 + (y / HEIGHT) * 3
        c = complex(re, im)
        z = 0

        for i in range(MAX_ITER):
            z = z * z + c
            if abs(z) > 2:
                result[y, x] = i
                break

plt.imshow(result, cmap="inferno")
plt.axis("off")
plt.show()

# запусти мене
