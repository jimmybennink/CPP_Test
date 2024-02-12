import ctypes

lib = ctypes.CDLL("Controllers/PX4_Controllers.so", winmode=0)

class PX4Controllers(object):
    def __init__(self):
        self.obj = lib.Controller_init()

    def Run_Controller(self):
        lib.Run_Controller(self.obj)