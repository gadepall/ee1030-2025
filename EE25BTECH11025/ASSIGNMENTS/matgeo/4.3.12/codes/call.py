import ctypes as ct

lib = ct.CDLL("./problem.so")

lib.give_data.argtypes = [ct.POINTER(ct.c_double)]

points = ct.c_double*12

data = points()

lib.give_data(data)

def send_data():
    return data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]

