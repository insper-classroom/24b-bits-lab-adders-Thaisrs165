#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b 

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]

    haList[0] = halfAdder(a, b, s[0], s[1]) 
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()


@block
def adder2bits(x, y, soma, carry):
    carry1 = Signal(bool(0))

    full_adder1 = fullAdder(x[0], y[0], 0, soma[0], carry1)
    full_adder2 = fullAdder(x[1], y[1], carry1, soma[1], carry) 

    return instances() 


@block
def adder(x, y, soma, carry):
    n = len(x)
    carry_in = Signal(bool(0))
    carrys = [Signal(bool(0)) for _ in range(n + 1)]

    faList = [fullAdder(x[i], y[i], carrys[i], soma[i], carrys[i + 1]) for i in range(n)] 

    @always_comb
    def comb():
        carry.next = carrys[n]

    return instances() 