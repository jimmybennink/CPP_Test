import ctypes

lib = ctypes.CDLL("Controllers/PX4_Controllers.so", winmode=0)

# Used for type checking the returned pointer

# Actual wrapper class
class PX4Controllers(object):

    lib.Run_Floats.argtypes = [ctypes.c_void_p, ctypes.c_float]
    #lib.Run_Floats.restype = ctypes.py_object

    def __init__(self):
        self.obj = lib.Controller_init()

    def Run_Controller(self):
        lib.Run_Controller(self.obj)

    def Floats(self, input):
        return lib.Run_Floats(self.obj, input)
