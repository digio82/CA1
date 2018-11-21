#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 23:56:43 2018

@author: FabioDiGiovine
"""
#test file

#import unittest package
import unittest

#use class from Calculator_CA1a
from Calculator_CA1a import calculator

calc = calculator

#create test calss with built in funcions with assigned values to be used for the test
#each function will test a separate calc function from the Calculator_CA1a class
#the result should give no fails
class CalculatorTest(unittest.TestCase):
    
    def testAddition(self):
        self.assertEqual(4, calc.addition(2,2))
        
    def testSubtraction(self):
        self.assertEqual(4, calc.subtraction(8,4))
        
    def testMultiplication(self):
        self.assertEqual(16, calc.multiplication(4,4))
    
    def testDivision(self):
        self.assertEqual(10, calc.division(100,10))
        self.assertEqual(None , calc.division(7,0))
    
    def testSquareRoot(self):
        self.assertEqual(9,calc.squareRoot(81))
        
    def testSquare(self):
        self.assertEqual(81, calc.square(9))
    
    def testCube(self):
        self.assertEqual(27, calc.cube(3))

    def testSine(self):
        self.assertEqual(0.9129452507276277, calc.sine(20))
        
    def testTangent(self):
        self.assertEqual(1.557407724654902, calc.tangent(1))
        self.assertEqual(0, calc.tangent(0))
    
    def testArcTangent(self):
        self.assertEqual(0.7853981633974483, calc.arcTan(1))

unittest.main()