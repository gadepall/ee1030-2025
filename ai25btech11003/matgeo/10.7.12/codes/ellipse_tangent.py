#Program to plot the tangent to a hyperbola

#Code by GVV Sharma

#August 8, 2020

#Revised August 16, 2024

#Revised August 21, 2024

#Revised August 22, 2024

import numpy as np

import matplotlib.pyplot as plt

from numpy import linalg as LA

import sys #for path to external scripts

# Read data from main.so and main.dat files
def read_data_from_files():
    points = []

    # Read from main.dat
    with open('main.dat', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() and not line.startswith('#'):
                parts = line.strip().split()
                if len(parts) == 2:
                    try:
                        x, y = float(parts[0]), float(parts[1])
                        if abs(x) < 1 and abs(y) < 1:  # Filter for contact points
                            points.append((x, y))
                    except ValueError:
                        continue

    return points[:2]  # Return first two points (q1 and q2)

# Define standard basis vectors and functions needed
e1 = np.array([[1], [0]])
e2 = np.array([[0], [1]])

def conic_param(V, u, f):
    O = -LA.inv(V) @ u
    n0 = np.sqrt(LA.norm(u)**2 - f * np.trace(V))
    return None, None, None, O, None, None, None

def ellipse_param(V, u, f):
    # For ellipse 4x^2 + 9y^2 = 1, a^2 = 1/4, b^2 = 1/9
    return [0.5, 1/3]  # a = 1/2, b = 1/3

def ellipse_gen(a, b):
    theta = np.linspace(0, 2*np.pi, 100)
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    return np.array([x, y])

def conic_contact(V, u, f, n):
    # Read contact points from files
    contact_points = read_data_from_files()
    if len(contact_points) >= 2:
        if np.array_equal(n, e2):  # For n = e2, return first point
            return np.array([[contact_points[0][0]], [contact_points[0][1]]])
        else:  # For n = e1, return second point
            return np.array([[contact_points[1][0]], [contact_points[1][1]]])
    else:
        # Fallback calculation
        return LA.inv(V) @ (np.sqrt((u.T @ LA.inv(V) @ u - f) / (n.T @ LA.inv(V) @ n)) * n - u)

def line_norm(n, c, k1, k2):
    x_range = np.linspace(k1, k2, 100)
    if abs(n[1, 0]) > 1e-10:
        y_line = (c - n[0, 0] * x_range) / n[1, 0]
        return np.array([x_range, y_line])
    else:
        return np.array([np.full_like(x_range, c/n[0, 0]), x_range])

#setting up plot

fig = plt.figure()

ax = fig.add_subplot(111, aspect='equal')

num= 100

y = np.linspace(-2,2,num)

#hyperbola parameters, first eigenvalue should be negative

V = np.array(([4, 0], [0, 9]))

u = np.zeros((2,1))

#u = -0.5*np.array(([0,1])).reshape(-1,1)

f = -1

n0,c,F,O,lam,P,e = conic_param(V,u,f)

#print(O)

ab = ellipse_param(V,u,f)

#Generating the Standard ellipse

xStandard= ellipse_gen(ab[0],ab[1])

ParamMatrix = np.diag(ab)

P = np.eye(2)

#Tangent

'''

q = np.zeros((2,1))

q[0][0] = 10

q[1][0] = (q[0][0]-1)/(q[0][0]-2)

'''

#n = np.array(([1,1])).reshape(-1,1)

n = e2

q = conic_contact(V,u,f,n)

c = (n.T@q).flatten()

n1 = e1

q1 = conic_contact(V,u,f,n1)

c1 = (n1.T@q1).flatten()

#n = V@q+u

#c = n.T@q

#print(n,c)

#Directrix

#Affine conic generation

Of = O.flatten()

#Generating lines

k1 = -1

k2 = 1

x_A = line_norm(n,c[0],k1,k2)

x_B = line_norm(n,c[1],k1,k2)

x_C = line_norm(n1,c1[0],k1,k2)

x_D = line_norm(n1,c1[1],k1,k2)

'''

x_A = P@line_norm(n,c[0],k1,k2)+Of[:,np.newaxis]#directrix

x_B = P@line_norm(n,cl[0],k1,k2)+Of[:,np.newaxis]#latus rectum

x_C = P@line_norm(n,c[1],k1,k2)+Of[:,np.newaxis]#directrix

x_D = P@line_norm(n,cl[1],k1,k2)+Of[:,np.newaxis]#latus rectum

xStandardHyperLeft = np.block([[-x],[y]])

xStandardHyperRight= np.block([[x],[y]])

'''

#Generating the actual ellipse

#xActual = P@xStandard + Of[:,np.newaxis]

#xActualHyperLeft = P@ParamMatrix@xStandardHyperLeft+Of[:,np.newaxis]

#xActualHyperRight = P@ParamMatrix@xStandardHyperRight+Of[:,np.newaxis]

#plotting

#plt.plot(xActualHyperLeft[0,:],xActualHyperLeft[1,:],label='Hyperbola',color='r')

#plt.plot(xActualHyperRight[0,:],xActualHyperRight[1,:],color='r')

#plt.plot(xActual[0,:],xActual[1,:],label='Ellipse')

plt.plot(xStandard[0,:],xStandard[1,:],label='Ellipse: 4x² + 9y² = 1')

plt.plot(x_A[0,:],x_A[1,:],label='Tangent at q1',color='r')

plt.plot(x_B[0,:],x_B[1,:],color='r')

plt.plot(x_C[0,:],x_C[1,:],color='g')

plt.plot(x_D[0,:],x_D[1,:],label='Tangent at q2',color='g')



colors = np.arange(1,4)

#Labeling the coordinates

tri_coords = np.block([O,q,q1])

#tri_coords = np.block([O,F])

plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)

#vert_labels = ['$\\mathbf{O}$']

vert_labels = ['$\\mathbf{O}$','q1(-2/5, 1/5)','q2(2/5, -1/5)']

for i, txt in enumerate(vert_labels):

    plt.annotate(txt, # this is the text

    # plt.annotate(f'{txt}\\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',

    (tri_coords[0,i], tri_coords[1,i]), # this is the point to label

    textcoords="offset points", # how to position the text

    xytext=(10,-10), # distance from text to points (x,y)

    ha='center') # horizontal alignment can be left, right or center

# use set_position

ax = plt.gca()

ax.spines['top'].set_color('none')

ax.spines['left'].set_position('zero')

ax.spines['right'].set_color('none')

ax.spines['bottom'].set_position('zero')

'''

ax.spines['left'].set_visible(False)

ax.spines['right'].set_visible(False)

ax.spines['top'].set_visible(False)

ax.spines['bottom'].set_visible(False)

'''

plt.xlabel('$x$')

plt.ylabel('$y$')

plt.legend(loc='best')

plt.grid() # minor

plt.axis('equal')

#if using termux

plt.savefig('fig1.png')

#else

#plt.show()
