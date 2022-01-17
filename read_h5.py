import numpy as np
import h5py

# read an h5 file #
f = h5py.File('C3H8_DFT_NMS.h5', 'r')
for name in f:
    layer1 = f[name]
lst = list(layer1.keys())
print('Found',len(lst),'Molecules')
Size = [0]*len(lst)
for i in range(0,len(lst)):
    group = layer1[lst[i]]
    spec = np.array(group['species'])
    ener = np.array(group['energies'])
    atyp = spec.astype(str)
    coor = np.array(group['coordinates'])
    Size[i] = len(ener)
    print(atyp, 'Size:', Size[i])
    print('coordinates shape:',coor.shape,';dtype:',coor.dtype,';size:',coor.size)
    print('energies shape:',ener.shape,';dtype:',ener.dtype,';size:',ener.size)
    print('species shape:',spec.shape,';dtype:',spec.dtype,';size:',spec.size)
    
print('Total data:', sum(Size)) 


