import numpy as np
a=np.arange(12)
a.shape=[3,4]
print(a)
b=np.ravel(a)
print(b)
np.savetxt(a,fmt='%d',delimiter=',')
np.ar