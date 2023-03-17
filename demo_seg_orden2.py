#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:55:28 2020

@author: mariano
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot


w0 = 1

plt.close('all')

qq_param = [ 0.5, np.sqrt(2)/2, 10]

for qq in range(len(qq_param)):
    
    my_tf = TransferFunction( [w0**2], [1, w0/qq_param[qq], w0**2] )
    
    bodePlot(my_tf, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq_param[qq]) )
    
    pzmap(my_tf, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq_param[qq])) #S plane pole/zero plot
    
    GroupDelay(my_tf, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq_param[qq]))
    
    