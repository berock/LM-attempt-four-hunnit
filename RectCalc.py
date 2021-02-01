# calculation for rect tube wt/ft
from sheets import *


def RectCalc():
	h = float(input("Rect tube long dimension ----> "))
	w = float(input("Rect tube short dimension ----> "))
	wt = float(input("Wall thickness ----> "))

	stwt = (2 * (wt) * (h + w - 8 * (wt)) + 9.4248 * (wt * wt)) * 3.40277
	dfhss = df.loc[df['MT'] == 'HSS']
	saCol = dfhss.loc[dfhss['SIZE A'] == h]
	if saCol.empty:
		print("\n"" -----> That material size has not been quoted. <-----")
	else:
		sbCol = saCol.loc[saCol['SIZE B'] == w]
		if sbCol.empty:
			print("\n"" -----> That material size has not been quoted. Here is a list of like material <-----")
			print(saCol.sort_values(by='DATE', ascending=False))
			print(" ----->", h, "X", w, "X", wt, "square tube is approximately", str(round(stwt, 2)),
				  "lbs per foot.", "<-----")
			print(" ----->",
				  "Structural tubing is generally available in 20', 24', 30', 32', 34', 40', 48', 56' and 60' lengths. <-----",
				  "\n")
		else:
			# print (sbCol)
			stw = sbCol.loc[sbCol['WT'] == wt]
			if stw.empty:
				print("\n"" -----> That material size has not been quoted. Here is a list of like material <-----")
				print(sbCol.sort_values(by='DATE', ascending=False))
				print(" ----->", h, "X", w, "X", wt, "square tube is approximately", str(round(stwt, 2)),
					  "lbs per foot.", "<-----")
				print(" ----->",
					  "Structural tubing is generally available in 20', 24', 30', 32', 34', 40', 48', 56' and 60' lengths. <-----",
					  "\n")
			else:
				stdt = stw.sort_values(by='DATE', ascending=False)
				print("\n"" ----->", h, "X", w, "X", wt, "was last priced by", stdt.iloc[0, 4], "on", stdt.iloc[0, 7],
					  "for $",stdt.iloc[0, 5], "for a", stdt.iloc[0, 6], "foot stick." " <-----")
				print(" ----->", h, "X", w, "X", wt, "square tube is approximately", str(round(stwt, 2)),
					  "lbs per foot.", "<-----")
				print(" ----->",
					  "Structural tubing is generally available in 20', 24', 30', 32', 34', 40', 48', 56' and 60' lengths. <-----",
					  "\n")