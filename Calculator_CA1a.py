#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 23:05:55 2018

@author: FabioDiGiovine
"""

#import math package
import math

#create Class Calculator  
class calculator():
    
    # create menu function (use of new line|n )
    def menu():
        print('')
        print ('********************** MENU ********************')
        print('')
        print(' 1 Addition\n 2 Subtraction\n 3 Multiplication\n 4 Division\n 5 Square Root\n 6 Square\n 7 Cube\n 8 Sine\n 9 Tangent\n 10 Arc Tangent\n 11 TO QUIT\n')
    
    #function choice thet will ask the use to input an INTEGER value (with exception handling)
    def choice():
        while 1==1: 
            try:
                choice = int(input('************************************************\nMake your choice (between 1 and 10 to do a calculation or any other number)\n************************************************\n: '))
                break
            except:
                print('You must enter a integer value')
        return choice

    #askValue function to prompt the user tu input an integer value
    def askVal():
        while 1==1:
            try:
                val = int(input('Input an integer value: '))
                break
            except:
                print('You must enter a integer value')
        return val
      
####series of 10 math functions to be used for calculations
        
    def addition(a,b):
        return (a+b)
    
    def subtraction(a,b):
        return (a-b)
    
    def multiplication(a,b):
        return (a*b)
    
    #division by zero rule
    def division(a,b):
        if b == 0:
            print('It is not possible to divide a number by zero')
        else:
            return (a/b)
      
    def squareRoot(a):
        return math.sqrt(a)
    
    def square(a):
        return (a*a)
    
    def cube(a):
        return(a*a*a)
    
    def sine(a):
        return(math.sin(a))
    
    
    def tangent(a):
        return (math.tan(a))
    
    def arcTan(a):
        return (math.atan(a))