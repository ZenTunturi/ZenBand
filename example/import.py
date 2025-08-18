# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 14:07:02 2025

@author: andri
"""

import numpy as np

##############################################
# initialize parameters
er1 = 1
er2 = 12
r = 0.45
N_Points = 100

x = np.linspace(-0.5, 0.5, 1024)
y = np.linspace(-0.5, 0.5, 1024)
X,Y = np.meshgrid(x, y)
###############################################

ER = np.zeros((len(x), len(y)))

# define the shape
ER = ER + (X**2 + Y**2 > r**2)
ER  = er1 + (er2 - er1) * ER
# plt.pcolor(ER)
################## Bands #####################

# define beta vectors
beta = np.zeros((2, N_Points))
beta[0, 0:29] = np.linspace(0, np.pi, 29); beta[0, 29:59] = np.pi;                     beta[0, 59:100] = np.linspace(np.pi, 0, 41)
beta[1, 0:29] = 0;                         beta[1, 29:59] = np.linspace(0, np.pi, 30); beta[1, 59:100] = np.linspace(np.pi, 0, 41)

# define names of key points of symmetry
KP = ['$\Gamma$', '$X$', '$M$', '$\Gamma$']

# define key points of symmetry
KT = [0, 29, 58, 99]

# define direct lattice vectors
t1    = np.array([[1],[0]])
t2    = np.array([[0],[1]])

# define reciprocal lattice vectors
T1    = 2*np.pi * np.array([[1],[0]])
T2    = 2*np.pi * np.array([[0],[1]])

data = {'er':ER, 'beta':beta, 't1':t1, 't2':t2, 'T1':T1, 'T2':T2, 'KP':KP, 'KT':KT}
np.save('import_sample_bands.npy', data)
################## Contours ##################

# define beta vectors
bx    = np.linspace(-np.pi,  np.pi, N_Points)
by    = np.linspace( np.pi, -np.pi, N_Points)
beta  = np.zeros((2, N_Points**2))

idx = 0

for nx in range(0, N_Points):
    for ny in range(0, N_Points):
        beta[:,idx] = np.array(([bx[nx], by[ny]]))
        idx = idx + 1
        
# define direct lattice vectors
t1    = np.array([[1],[0]])
t2    = np.array([[0],[1]])

# define reciprocal lattice vectors
T1    = 2*np.pi * np.array([[1],[0]])
T2    = 2*np.pi * np.array([[0],[1]])

data = {'er':ER, 'beta':beta, 't1':t1, 't2':t2, 'T1':T1, 'T2':T2}
np.save('import_sample_contours.npy', data)
