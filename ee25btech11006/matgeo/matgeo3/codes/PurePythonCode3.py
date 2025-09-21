import numpy as np
import math

# Given magnitudes
a_mag = 1/2
b_mag = 4/np.sqrt(3)
cross_mag = 1/np.sqrt(3)

# sinθ = |a×b|/(|a||b|)
sin_theta = cross_mag/(a_mag*b_mag)
theta1 = math.degrees(math.asin(sin_theta))
theta2 = 180 - theta1

print("Possible angles:", theta1, "or", theta2)

# a·b = |a||b|cosθ
dot1 = a_mag*b_mag*math.cos(math.radians(theta1))
dot2 = a_mag*b_mag*math.cos(math.radians(theta2))

print("Possible values of a·b:", dot1, "or", dot2)