import ctypes

lib = ctypes.CDLL("Controllers/PX4_Controllers.so", winmode=0)

# Used for type checking the returned pointer

# Actual wrapper class
class PX4Controllers(object):

    lib.Run_Floats.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
    lib.Run_Floats.restype = ctypes.c_void_p

    def __init__(self):
        self.obj = lib.Controller_init()

    def Run_Controller(self):
        lib.Run_Controller(self.obj)

    def Floats(self, inp_list):

        ret1 = ctypes.c_float(inp_list[0])
        ret2 = ctypes.c_float(inp_list[1])
        lib.Run_Floats(self.obj, ctypes.byref(ret1), ctypes.byref(ret2))

        return  (ret1.value, ret2.value)
