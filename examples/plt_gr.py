#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:48:51 2017

@author: justinwu
"""

import numpy as np
t=np.arange(0.,5.,0.2)
print(t)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()