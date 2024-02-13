# Advanced Air Mobility Vehicle Simulation

'''
File originally created: 2/4/2024
Authors: Jimmy Bennink

This file should only be ran once to setup the development/running environment 
after the repo is cloned. It creates a virtual environment based on the selected
python interpreter (which should be 3.10.11), and then installs the listed
dependencies to that virtual environment. This file should be updated with each 
new dependency that's used in the source code.
'''

import subprocess
import sys
import os

dependencies = [
                "numpy==1.26.3",
                "scipy==1.12.0",
                "matplotlib==3.8.2",
                "keyboard==0.13.5",
                "msgpack-rpc-python==0.4.1",
                "msgpack-python==0.5.6",
                "pandas==2.2.0",
                "tornado==4.5.3",
                "wheel==0.42.0",
                "airsim==1.8.1",
                "pybind11==2.11.1"
                ]

# Change formatting for linux systems vs Windows systems 
if sys.platform == "linux" or sys.platform == "linux2":
    subprocess.check_call(['sudo', 'apt', 'install', 'python3.10-venv'])
    py_path = os.getcwd() + '/.venv/bin/python'
else:
    py_path = os.getcwd() + '\.venv\Scripts\python.exe'

# Sets up the virtual environment
subprocess.check_call([sys.executable, '-m', 'venv', '.venv'])

# Upgrades pip
subprocess.check_call([py_path, 
                       '-m', 
                       'pip',
                       '--timeout=1000',
                       'install', 
                       '--upgrade', 
                       'pip'])

# Installs packages to virtual environment distribution
for package in dependencies:
    subprocess.check_call([py_path, 
                           '-m', 
                           'pip', 
                           'install', 
                           package])
