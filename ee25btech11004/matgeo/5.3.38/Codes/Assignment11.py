import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt

answer = numpy.linalg.solve([[3,1],[-1,2]], [1,-5])

answer[0] = round(answer[0],2)
answer[1] = round(answer[1],2)
print(answer)

fig = plt.figure(figsize =(6,6))
ax = fig.add_subplot(111)

X = np.linspace(-20,20,2)

Y1 = (1-3*X)
Y2 = 0.5*(X-5)

ax.plot(X, Y1, label='Line 1')
ax.plot(X, Y2, label='Line 2')

ax.scatter(answer[0], answer[1], label=f'({answer[0]}, {answer[1]})')

ax.grid(True)
ax.legend()
plt.show()



