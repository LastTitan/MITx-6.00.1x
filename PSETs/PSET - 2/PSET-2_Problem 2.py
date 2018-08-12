# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:50:23 2018

@author: TheLastTitan
"""

def remBalance (balance,monthlyPayment,annualInterestRate):
    '''
    Just pass the balance to get the remaining balance after 1 year
    '''
    month = 0
    while month < 12:
        unpaid = balance - monthlyPayment
        interest = unpaid * (annualInterestRate/12)
        balance = unpaid + interest
        month += 1
    return round(balance,0)

balance = 4773
monthlyPayment = 0
annualInterestRate = 0.2
finalBalance = 1

while finalBalance > 0:
    monthlyPayment += 10
    finalBalance = remBalance(balance, monthlyPayment, annualInterestRate)
    
print ('Lowest Payment:', monthlyPayment)
    
    