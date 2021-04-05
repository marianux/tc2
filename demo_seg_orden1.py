#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:30:31 2020

@author: mariano
"""


from splane import pzmap, grpDelay, bodePlot
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt


w0 = 10**3
qq = 1


my_tf = TransferFunction( [w0**2], [1, w0/qq, w0**2] )

bodePlot(my_tf)

pzmap(my_tf) #S plane pole/zero plot

grpDelay(my_tf)
