import ctypes as ct

lib = ct.CDLL("./problem.so")

lib.give_data.argtypes = [ct.POINTER(ct.c_double)]

points = ct.c_double*3
data = points()
lib.give_data(data)

def send_data():
    return data[0], data[1], data[2]