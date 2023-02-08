#This module takes Binary value and converts the value to Decimal and returns Decimal value
def BinarytoDecimal(binNum):
    DecimalNumber = 0
    power = 0
    while binNum>0:
        DecimalNumber += 2 **power* (binNum%10)
        binNum //=10
        power += 1
    return DecimalNumber
"""
@ Kaushal Gurung
Londonmet ID-19031057
"""
