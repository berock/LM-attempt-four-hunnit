from TubeCalc import *
from SquareCalc import *
from RectCalc import *
from AngleCalc import *
from PlateCalc import *




def WeightCalc():
	mat = input("Angle | HSS (rect or square tube) | Tube (tubing or pipe) | Plate --->")
	if mat == "L" or mat == "l" or mat == "angle" or mat =="ANGLE":
		AngleCalc()
	elif mat == "HSS" or mat == "hss" or mat == "H" or mat == "h":
		equal = input("Is your tubing square? Y/N ")
		if equal == "y" or equal == "Y":
			SquareCalc()
		elif equal == "n" or equal == "N":
			RectCalc()
		else:
			print("Read Directions. Must be 'Y' for yes or 'N' for no")
	elif mat == "T" or mat == "t" or mat == "tube" or mat =="Tube" or mat == "pi" or mat == "PI":
		TubeCalc()
	elif mat == "Pl" or mat == "pl" or mat == "PL" or mat == "Plate" or mat =="plate":
		PlateCalc()
	else:
		print("Not a recognized material type!!\nType: L or Angle | HSS for rectangular or square tubing | Tube for pipe or round tuubing. ")

	