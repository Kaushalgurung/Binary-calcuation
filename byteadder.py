#This module is for creating Logic-Gates and calculating the addition of two binary numbers.

#AND-GATE
def AND_gate(a,b):
	if a==b==1:
		return 1
	else:
		return 0
#OR-GATE
def OR_gate(a,b):
	if a==b==0:
		return 0
	else:
		return 1	
#NOT-GATE
def NOT_gate(a):
	if a==0:
		return 1
	else:
		return 0
#NOR-GATE
def NOR_gate(a,b):
        if a==b:
                return 1
        else:
                return 0
#EXOR-GATE
def EXOR_gate(a,b):
        if a==b:
                return 0
        else:
                return 1
#HALF-ADDER        
def HalfAdder(a,b):
	SUM = EXOR_gate(a,b)
	CARRY = AND_gate(a,b)
	return (SUM,CARRY)
#FULL-ADDER
def FullAdder(a,b,Cin=0):
	sum1, c1 = HalfAdder(a,b)
	sum2,c2 = HalfAdder(sum1,Cin)
	Cout = OR_gate(c1,c2)
	return (sum2,Cout)
#BINARY-ADDER
def BinaryAdder(a,b):
	c=0
	s=''
	for i in range(len(a and b)-1,-1,-1):
		summ,c= FullAdder(int(a[i]),int(b[i]),c)
		s+=str(summ)
	s+=str(c)
	s=s[::-1]
	return s
"""
@ Kaushal Gurung
Londonmet ID-19031057
"""


