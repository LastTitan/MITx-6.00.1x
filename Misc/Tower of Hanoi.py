# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:06:08 2018

@author: TheLastTitan
"""

def printMove (fr,to):
    print ('Move from', fr, 'to', to )

def move (n,fr,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
        move(n-1,fr,spare,to)
        move(1,fr,to,spare)
        move(n-1,spare,to,fr)
        
move (2, 'p1', 'p2','p3' )