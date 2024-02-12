from Controllers.Wrapper import PX4Controllers

f = PX4Controllers()
f.Run_Controller()

float_results = f.Floats(3.3)
print(float_results)