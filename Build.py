# Build the shared library
import subprocess

subprocess.check_call(['g++', '-c', '-fPIC', 'foo.cpp', '-o', 'foo.o'])
subprocess.check_call(['g++', '-shared', "-Wl,-soname,libfoo.so", '-o', 'libfoo.so', 'foo.o'])