import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
y = []
for i in range(1, 19):
    img = cv.imread(f"C:/Users/bbkx2/Downloads/ColourSample/{i}.jpg", 1)
    while True:
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        lower = np.array([10, 40, 60])
        upper = np.array([255, 255, 250])
        mask = cv.inRange(hsv, lower, upper)
        result = cv.bitwise_and(img, img, mask=mask)
        B, G, R = img[170,35]
        if B > 10 and G > 200 and R > 180: y.append("Not Polluted")
        else: y.append("Polluted")
        break
x = [str(i) for i in range(1, 19)]
plt.figure(1), plt.subplot(2, 1, 1), plt.scatter(x, y, color='red')
plt.title("Water Condition"), plt.xlabel("Sample"), plt.ylabel("Condition")
plt.grid(), plt.show()
