import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load compiled .so file  
lib = ctypes.CDLL('./libregression.so')

get_data = lib.get_data
get_data.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_int)
]
get_data.restype = None

years = np.zeros(6, dtype=np.double)
prod = np.zeros(6, dtype=np.double)
n = ctypes.c_int()
get_data(
    years.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    prod.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    ctypes.byref(n)
)

x = np.arange(1, n.value + 1)
y = prod

# Get statistics using .so file
get_stats = lib.get_stats
stats = np.zeros(3, dtype=np.double)
get_stats(
    years.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    prod.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    n,
    stats.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)
alpha, beta, alpha_plus_beta = stats

# Plot scatter and regression (bar for production, points for prediction)
plt.figure(figsize=(8,5))
plt.bar(years, prod, color='lightblue', label='Production')
plt.scatter(years, prod, color='black', zorder=2, label='Data Points')
reg_line = alpha + beta * (x-1)
plt.plot(years, reg_line, color='red', linewidth=2, label='Regression')
plt.xlabel('Year')
plt.ylabel('Production (lakh tonnes)')
plt.title(f'Regression Bar Graph & Line: $\\alpha+\\beta$={alpha_plus_beta:.2f}')
plt.legend()
plt.tight_layout()
plt.show()

