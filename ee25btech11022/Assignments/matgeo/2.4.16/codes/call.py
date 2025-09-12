# call.py
import ctypes

lib = ctypes.CDLL('./libcode.so')
result = lib.check_perpendicular()
print("The lines are perpendicular." if result else "The lines are NOT perpendicular.")

arr = (ctypes.c_double * 12)()
lib.get_points(arr)
for i, name in enumerate(['A', 'B', 'C', 'D']):
    print(f"Point {name}: ({arr[i*3]}, {arr[i*3+1]}, {arr[i*3+2]})")

