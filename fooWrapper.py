import ctypes

lib = ctypes.CDLL("libfoo.so", winmode=0)

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)