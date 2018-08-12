# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:20:48 2018

@author: TheLastTitan
"""

def remBalance (balance,monthlyPayment):
    '''
    Just pass the balance to get the remaining balance after 1 year
    '''
    month = 0
    while month < 12:
        unpaid = balance - monthlyPayment
        interest = unpaid * (monthlyInterestRate)
        balance = unpaid + interest
        month += 1
    return balance

balance = 999999; annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12; finalBalance = 1
low = balance/12
high = (balance*((1+monthlyInterestRate)**12))/12

while finalBalance > 0 or finalBalance < -1:
    monthlyPayment = (low + high)/2
    finalBalance = remBalance(balance, monthlyPayment)
    high += finalBalance/6
        
print ('Lowest Payment:', round(monthlyPayment,2))
