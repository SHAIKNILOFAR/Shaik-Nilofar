import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
with open("nrml_binary.txt","wb") as k:
	k.write(x)
