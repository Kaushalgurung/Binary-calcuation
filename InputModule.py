#This module is for taking 2 valid number from uuser as input.
def Inputfunction():
	sucess=False
	while sucess==False:
		try:
			x =int(input("\n    Enter the First-Number :"))
			if x>=255 or 0>x:
				print("    ║The number must be between 0 and 255║")
			else:
				sucess=True
		except:
			print("    ║[INVALID First-Number!! Please enter a Valid Number/Value!]║")
	sucess=False
	while sucess==False:
		try:
			y =int(input("    Enter the Second-Number:"))
			if y>=255 or 0>y:
				print("    ║The number must be between 0 and 255║")
			else:
				sucess=True
		except:
			print("    ║[INVALID Second-Number!! Please enter a Valid Number/Value!]║")
	return (x,y)
"""
@ Kaushal Gurung
Londonmet ID-19031057
"""
