import ctypes as ct

lib = ct.CDLL("./problem.so")
lib.give_data.argtypes = [ct.POINTER(ct.c_double)]
lib.give_findata.argtypes = [ct.POINTER(ct.c_double)]

points = ct.c_double*8
data = points()
lib.give_data(data)
finpoints = ct.c_double*8
findata = finpoints()
lib.give_findata(findata)

def send_data():
    return data, findata 




