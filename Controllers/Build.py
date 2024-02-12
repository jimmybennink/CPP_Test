# Build the shared library
import subprocess

subprocess.check_call(['g++', 
                       '-c', 
                       '-fPIC', 
                       'Controllers/PX4_Controllers.cpp', 
                       '-o', 
                       'Controllers/PX4_Controllers.o'])
subprocess.check_call(['g++', 
                       '-shared', 
                       "-Wl,-soname,Controllers/PX4_Controllers.so", 
                       '-o', 
                       'Controllers/PX4_Controllers.so', 
                       'Controllers/PX4_Controllers.o'])