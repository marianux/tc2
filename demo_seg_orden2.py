#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:55:28 2020

@author: mariano
"""

from splane import pzmap, grpDelay, bodePlot, convert2SOS
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt


w0 = 1
qq = 1

plt.close('all')

qq_param = [ 0.5, 1, 10]

for qq in range(len(qq_param)):
    
    my_tf = TransferFunction( [w0**2], [1, w0/qq_param[qq], w0**2] )
    
    bodePlot(my_tf, 1)
    
    pzmap(my_tf, 2) #S plane pole/zero plot
    
    grpDelay(my_tf, 3)
    