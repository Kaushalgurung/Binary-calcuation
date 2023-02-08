#This module takes Decimal value and converts the value to Binary and returns Binary value
def DecimaltoBinary(n):
	n=int(n)
	bit=[]
	BinaryList=[]
	BinaryNumber=""
	while n !=0:
		r=n%2
		bit.append(r)
		n=n//2
	for i in range(len(bit)-1,-1,-1):
		BinaryList.append(bit[i])
		BinaryNumber = BinaryNumber +str(bit[i])
		l = len(BinaryNumber)
	if len(BinaryNumber)<8:
		for i in range(l,8):
			BinaryNumber="0"+BinaryNumber
	return (BinaryNumber)
"""
@ Kaushal Gurung
Londonmet ID-19031057
"""




        


        
