import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import resample
fs=8000
d=0.5
f=200
t=np.linspace(0,d,int(fs*d))
old_signal=np.sin(2*np.pi*f*t)
fs_new=1000
new_sample=int(fs_new*d)
new_signal=resample(old_signal,new_sample)
t1=np.linspace(0,0.5,new_sample)
'''plt.plot(t,old_signal)
plt.plot(t1,new_siganl)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('sine wave')
plt.show()'''
amplitude=1
quantization_levels=8
maximum_val=2**(8-1)-1
minimum_val=2**(8-1)
quantised_signal=np.round(new_signal*maximum_val/amplitude)*amplitude/(minimum_val)
plt.plot(t1,quantised_signal)
plt.show()
