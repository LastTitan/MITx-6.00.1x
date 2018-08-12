# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:43:38 2018

@author: TheLastTitan
"""
def newBalance (balance,monthlyPaymentRate,annualInterestRate):
    '''
    Just pass the balance to get new balance which is the sum of 
    (balance - minimum monthly payment) and the monthly interest 
    on the unpaid payment.
    '''
    unpaid = balance - (balance * monthlyPaymentRate)
    interest = unpaid * (annualInterestRate/12)
    return unpaid + interest

month = 0

while month < 12:
    balance = newBalance(balance)
    month += 1
        
print ('Remaining balance:', round(balance,2))