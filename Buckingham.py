#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:22:38 2021

@author: RussianMilitaryBlimp
"""

import numpy as np
import sympy as sym
import sys, os
from random import shuffle


Var =	{#       M   L   T  ...
    # "a_p   ":  [ 0,  2,  0],
    "L     ":  [ 0,  1,  0],
    "u     ":  [ 0,  1, -1],
    # "rho   ":  [ 1, -3,  0],
    # "mu    ":  [ 1, -1, -1],
    "Lambda":  [ 0, -1,  0],
    "nu    ":  [ 0,  2, -1],
    "I     ":  [ 1,  0, -3],
    "eps   ":  [ 0, -3, -1],
    "C_i   ":  [ 1, -3,  0],
    "C_p   ":  [ 1, -3,  0],
    # "mdot  ":  [ 1,  0, -1],
}

def PI(Var, ask=True):

    dims = Var.values()

    dims = np.matrix([i for i in iter(dims)])

    (n, p) = dims.shape

    print("-"*25)
    print("%d Dimensionless groups"%(n-p))

    A = np.zeros((p, n))

    for i in range(n):
        A[:,i] = dims[i]
        pass

    M = sym.nsimplify(sym.Matrix(A), rational=True).nullspace()
    
    pi = []
    for p, i in zip(M, range(n-p)):
        print("\nPI Group %d"%(i+1))
        pi.append({})
        for expon in zip(p, Var.keys()):
            if expon[0] == 0:
                pass
            else:
                pi[-1][expon[1].strip()] = expon[0]
                print(expon[1], ": \t", expon[0])
     
    print("-"*25) 

    yes = input("\nShuffle inputs? (Y/N)") if ask else "N"
    
    if yes.lower() in ["y", "yes", "yeah", "ye"]:
        items = list(Var.items())
        shuffle(items)
        PI(dict(items))
    else:
        return pi

if __name__ == '__main__':
    try:
        PI(Var)
    except KeyboardInterrupt:
        print()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
