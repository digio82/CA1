#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 23:06:56 2018

@author: FabioDiGiovine
"""

#Run File
#Import class from  Calculator_CA1a
from Calculator_CA1a import calculator

calc = calculator

#set choice to 0, promt the menu to the user till right selection is done as per menu choices
choice = 0

while choice !=11: 

    calc.menu()
    choice = calc.choice()
    print ('Choice: ', choice)

    #if choice selection is between 1 and 10 perform selected calculation    
    if 1<=choice<=10: 
    
        #ask user to input the 1st value
        val1 = calc.askVal()
        
        #for the 1st 4 calculation ask the user to input the second value, for the rest proceed with 1 value only
        if choice <5:
            val2 = calc.askVal()
              
        if choice == 1:
            result = calc.addition(val1,val2)
            
        elif choice == 2:
            result = calc.subtraction(val1,val2)
        
        elif choice == 3:
            result = calc.multiplication(val1,val2)
        
        elif choice == 4:
            result = calc.division(val1,val2)
        
        elif choice == 5:
            result = calc.squareRoot(val1)
        
        elif choice == 6:
            result = calc.square(val1)
            
        elif choice == 7:
            result = calc.cube(val1)
            
        elif choice == 8:
            result = calc.sine(val1)
            
        elif choice == 9:
            result = calc.tangent(val1)
        
        elif choice == 10:
            result = calc.arcTan(val1)
        
        #print the result
        print ('')
        print ('*********************************************')
        print ('The result of your calculation is = ', result)
        print ('*********************************************')
        print ('')
        print ('')
    
    #or quit the console
    else:
        exit