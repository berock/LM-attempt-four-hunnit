# tubing weight calculator
from sheets import *
import numpy as np
from numpy import arange

pipesize = {1:1.315, 1.25:1.660, 1.50:1.900, 2:2.375, 2.5:2.875, 3:3.500, 3.5:4.000, 4:4.500, 4.5:5.000, 5:5.563, 6:6.625, 7:7.625, 8:8.625, 9:9.625, 10:10.75, 11:11.75, 12:12.75}

def TubeCalc():
	d = float(input("Pipe or tubing size ---> "))
	wt = float(input("Tubing wall thickness to three decimals ---> "))
	dfh = df.loc[df['MT'] == 'PIPE']
	dfhss = dfh.drop(columns=['SIZE B'], axis=1)
	min = wt - .200
	max = wt + .200
	dmin = d - 2
	dmax = d + 2
	if d >= 14:	
		W = 10.68 * (d - wt) * wt
		saCol = dfhss.loc[dfhss['SIZE A'] == d]
		if saCol.empty:
			saCol = dfhss.loc[dfhss['SIZE A'].between(dmin, dmax)]
			if saCol.empty:
				print("\n"," -----> No Pipe sizes close to the one you're looking for have been quoted. <-----",
					"\n"," ----->", d, "X", wt, "wall pipe or tubing is approximately", str(round(W, 2)), "lbs per foot.",
					  "<-----" "\n" "  ----->", "The OD of", d, "inch pipe is", d, "<-----", "\n")
			else:
				print("\n"," -----> This pipe has not been priced yet, but here are pipe sizes that have been quoted. <-----")
				print(saCol.sort_values(by='DATE', ascending=False))
				print(" ----->",d, "X",wt , "wall pipe or tubing is approximately",str(round(W , 2)),"lbs per foot.", "<-----" "\n" " ----->","The OD of" , d, "inch pipe is", d,"<-----","\n")
		else:
			stdt = saCol.loc[saCol['WT'] == wt]
			if stdt.empty:
				print("\n", " -----> This pipe has not been priced yet. Here is a list of Pipes that are close. <-----")
				print(saCol.sort_values(by='DATE', ascending=False))
				print(" ----->", d, "X", wt, "wall pipe or tubing is approximately", str(round(W, 2)), "lbs per foot.",
					  "<-----" "\n" " ----->", "The OD of", d, "inch pipe is", d, "<-----", "\n")
			else:
				print("\n"" ----->", d, "X", wt, "wall pipe was last priced by", stdt.iloc[0, 3], "on",
					  stdt.iloc[0, 6], "for $", stdt.iloc[0, 4], "for a", stdt.iloc[0, 5], "foot stick." " <-----")
				print(" ----->", d, "X", wt, "wall pipe or tubing is approximately", str(round(W, 2)), "lbs per foot.",
					  "<-----" "\n" " ----->", "The OD of", d, "inch pipe is", d, "<-----", "\n")
	else:
		if d in pipesize:
			d1 = pipesize.get(d)
			W = 10.68 * (d1 - wt) * wt
			saCol = dfhss.loc[dfhss['SIZE A'] == d]
			if saCol.empty:
				saCol = dfhss.loc[dfhss['SIZE A'].between(dmin, dmax)]
				print("\n", " -----> This pipe has not been priced yet. Here is a list of Pipes that are close. <-----")
				print(saCol.sort_values(by='DATE', ascending=False))
				print("\n","----->",d, "X",wt , "wall pipe or tubing is approximately",str(round(W , 2)),"lbs per foot.","<-----" "\n" " ----->","The OD of" , d, "inch pipe is", pipesize.get(d),"<-----","\n")
			else:
				stdt = saCol.loc[saCol['WT'] == wt]
				if stdt.empty:
					stdt = saCol.loc[saCol['WT'].between(min, max)]
					print("\n"," -----> This pipe has not been priced yet. Here is a list of Pipes that are close. <-----")
					print(stdt.sort_values(by='DATE', ascending=False))
					print(" ----->", d, "X", wt, "wall pipe or tubing is approximately", str(round(W, 2)),
						  "lbs per foot.", "<-----" "\n" " ----->", "The OD of", d, "inch pipe is", pipesize.get(d),
						  "<-----", "\n")
				else:
					print("\n"" ----->", d, "X", wt, "wall pipe was last priced by", stdt.iloc[0, 3], "on",
						  stdt.iloc[0, 6], "for $", stdt.iloc[0, 4], "for a", stdt.iloc[0, 5], "foot stick." " <-----")
					print(" ----->", d, "X", wt, "wall pipe or tubing is approximately", str(round(W, 2)),
						  "lbs per foot.", "<-----" "\n" " ----->", "The OD of", d, "inch pipe is", pipesize.get(d),
						  "<-----", "\n")
		else:
			print("-----> Not a common pipe size <-----")

