import ctypes as ct

def give_data():
    lib = ct.CDLL("./problem.so")
    entry = ct.c_double*4
    lib.make_data.argtypes = [ct.POINTER(ct.c_double)]
    data = entry()
    lib.make_data(data)

    return data[1], data[3], data[0], data[0], data[1], data[2]