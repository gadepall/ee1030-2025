import ctypes
import plot

lib = ctypes.CDLL('./code.so')

minu = ctypes.c_double()
sonu = ctypes.c_double()

lib.solve_ages(ctypes.byref(minu), ctypes.byref(sonu))

print(f"Minu's age: {minu.value}")
print(f"Sonu's age: {sonu.value}")

# Pass Python values to plot script
plot.plot_ages(minu.value, sonu.value)

