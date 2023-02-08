# This is the main program which takes 2 number adds them and gives binary result.
print("           █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("           █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█")
print("           █░░║║║╠─║─║─║║║║║╠─░░█")
print("           █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
print("           █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
print("\n")
print("█▄▄ █ █▄░█ ▄▀█ █▀█ █▄█   ▄▀█ █▀▄ █▀▄ █▀▀ █▀█")
print("█▄█ █ █░▀█ █▀█ █▀▄ ░█░   █▀█ █▄▀ █▄▀ ██▄ █▀▄")
#print("\n")
from DecimalToBinary import DecimaltoBinary#Importing DecimaltoBinary function from decimalToBinary.py
from BinarytoDecimal import BinarytoDecimal#Importing BinarytoDecimal function from BinarytoDecimal.py
from byteadder import BinaryAdder#Importing BinaryAdder function from byteadder.py
from InputModule import Inputfunction #Importing Inputfunction from InputModule.py
Continue="yes"
Continue="y"
while Continue=="yes" or Continue=="y":
	x,y=Inputfunction()#Using Inputfunction function
	ConvertedBinaryNumberX=DecimaltoBinary(x)#Using DecimaltoBinary function
	ConvertedBinaryNumberY=DecimaltoBinary(y)#Using DecimaltoBinary function
	print("\n    The binary value of {} is: {}".format(x,ConvertedBinaryNumberX))#Using place holder [String format() method]
	print("    The binary value of {} is: {}".format(y,ConvertedBinaryNumberY))#Using place holder [String format() method]
	summ=BinaryAdder(str(ConvertedBinaryNumberX),str(ConvertedBinaryNumberY))#Using BinaryAdder function to calcuate the sum of user input numbers in binary.
	addition=BinarytoDecimal(int(summ))#Using BinarytoDecimal function to calcuate decimal value of summ.
	print("\n    The sum of {} and {} is: {} |[Binary]|".format(x,y,summ))#Using place holder [String format() method]
	print("    The sum of {} and {} is: {} |[Decimal]|\n".format(ConvertedBinaryNumberX,ConvertedBinaryNumberY,addition))#Using place holder [String format() method]
	Continue = input("    Do you want to continue?-[yes/no]: ")#Asking user for confirmation to continue the program or to end it.
print("\n-^~^-^~^-^~^-^~^-^~^-^~^-^~^-^~^-^~^-^~^-^~^-~^-^~^-^~^-^~^-^~^-^~^-^~^-^~^-^~^-")
print("|Thank-you for using Binary Adder!|")
print("\n Have a Great-day!")


"""
@ Kaushal Gurung
Londonmet ID-19031057
"""
                 
        



