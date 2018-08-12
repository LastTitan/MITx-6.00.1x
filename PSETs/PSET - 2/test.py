# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:03:55 2018

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
        print ('Month:', month, 'unpaid:',unpaid, 'interest:', interest, 'balance:', balance)
    return balance


balance = 1000; annualInterestRate = 0.012; monthlyPayment = 83.8361
monthlyInterestRate = annualInterestRate/12; finalBalance = 1

finalBalance = remBalance(balance, monthlyPayment)
        
print ('Final Balance:', finalBalance)
