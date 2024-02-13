from Controllers.Wrapper import PX4Controllers

import numpy as np

import airsim
import socket  # Communicating with Matlab / Simulink
import struct  # Packing / unpacking datalink messages
import threading
import keyboard  # Halting

f = PX4Controllers()
f.Run_Controller()

inp1 = 4.35;
inp2 = 6.32;

float_results = f.Floats([inp1, inp2])
print(float_results)