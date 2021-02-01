from prompt import *


print("Welcome to Weight Calculator!!")
inp = input("Do you want to find some material weights? Y/N")

while inp == "Y" or inp =="y":
	WeightCalc()
	inp = input("Do you want to find more material weights? Y/N")
else:
	exit()
