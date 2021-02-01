# calculation for wt/ft for structural angle
from sheets import *


def AngleCalc():
	s1 = float(input("Dimension of long side of angle ---> "))
	s2 = float(input("Dimension of short side of angle ---> "))
	wt = float(input("Wall thickness of angle ---> "))
	s1min = s1 - 1
	s1max = s1 + 1
	l = 12

	sd1 = l * s1 * wt
	sd2 = l * (s2 - wt) * wt

	wtft = (sd1 + sd2) * .2845
	dfhss = df.loc[df['MT'] == 'ANGLE']
	saCol = dfhss.loc[dfhss['SIZE A'] == s1]
	if saCol.empty:
		saRange = saCol.loc[saCol['SIZE A'].between(s1min, s1max)]
		if saRange.empty:
			print("\n -----> That material hasn't been quoted, and we have no information on like material. <----- ")
			print(" ----->", s1, "X", s2, "X", wt, "angle is approximately", str(round(wtft, 2)), "lbs per foot.",
				  "<-----")
		else:
			print(saRange.sort_values(by='DATE', ascending=False))
	else:
		sbCol = saCol.loc[saCol['SIZE B'] == s2]
		if sbCol.empty:
			print("\n"" -----> That material size has not been quoted. Here is a list of like material <-----")
			print(saCol.sort_values(by='DATE', ascending=False))
			print(" ----->", s1, "X", s2, "X", wt, "angle is approximately", str(round(wtft, 2)), "lbs per foot.",
				  "<-----")
			print(" ----->",
				  "Structural tubing is generally available in 20', 24', 30', 32', 34', 40', 48', 56' and 60' lengths. <-----",
				  "\n")
		else:
			stw = sbCol.loc[sbCol['WT'] == wt]
			if stw.empty:
				print("\n", " -----> That material size has not been quoted. Here is a list of like material <-----")
				print(sbCol.sort_values(by='DATE', ascending=False))
				print("  ----->", s1, "X", s2, "X", wt, "angle is approximately", str(round(wtft, 2)),
					  "lbs per foot.", "<-----")
				print("  ----->",
					  "Structural tubing is generally available in 20', 24', 30', 32', 34', 40', 48', 56' and 60' lengths. <-----",
					  "\n")
			else:
				stdt = stw.sort_values(by='DATE', ascending=False)
				print("\n"" ----->", s1, "X", s2, "X", wt, "angle was last priced by", stdt.iloc[0, 4], "on", stdt.iloc[0, 7],
					  "for $", stdt.iloc[0, 5], "for a", stdt.iloc[0, 6], "foot stick." " <-----")
				print(" ----->", s1, "X", s2, "X", wt, "angle is approximately", str(round(wtft, 2)),
					  "lbs per foot.", "<-----")
				print(" ----->",
					  "Structural tubing is generally available in 20', 24', 30', 32', 34', 40', 48', 56' and 60' lengths. <-----",
					  "\n")