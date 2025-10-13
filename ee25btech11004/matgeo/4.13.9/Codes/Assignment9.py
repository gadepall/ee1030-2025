import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (6,6))
ax = fig.add_subplot(111)


vector = str(input("Input the vectors, and input X when you are done"))

counter = 0;
sum = np.zeros(2)

while(vector != "X"):
    vector.strip()
    vector0, vector1 = vector.split(" ")
    vector0 = int(vector0)
    vector1= int(vector1)
    vectorA = np.array([vector0,vector1])
    sum += vectorA
    counter = counter + 1

    ax.scatter(vector0, vector1, label = f'({vector0}, {vector1})')

    vector = str(input("Input the next vector"))
    
commonpoint = sum/counter

print(f"The line passes through ( {commonpoint[0]}, {commonpoint[1]} )")



ax.set_aspect('equal', adjustable='box')
ax.set_title("Three Points")

plt.legend()
ax.grid(True)
plt.show()








