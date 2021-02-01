# calculate the weight of carbon steel plates


def PlateCalc():
	l = float(input("Length of Plate in inches ----> "))
	w = float(input("Length of Plate in inches ----> "))
	t = float(input("Thickness of Plate ----> "))
	d = .284


	wt = w * l * t * d
	print(" ----->", "The weight of a", l, "X", w, "X", t, "plate is appoximately", str(round(wt, 2)),
		  "pounds" "<-----", "\n")
	pltwt = input("Do you want to see if we have pricing? ----->")
	if pltwt == "y" or pltwt == "Y" or pltwt == "yes" or pltwt == "Yes":
		PlateCost(l,w,t)
	else:
		pass



def PlateCost(l, w, t):
	tmin = t - .250
	tmax = t + .250
	from sheets import GetDf
	GetDf()
	newdf = dtframe.DataF()
	dfh = newdf.loc[df['MT'] == 'PLATE']
	dfhss = dfh.drop(columns='LEN PUR')
	stdt = dfhss.loc[dfhss['WT'] == t]

	if stdt.empty:
		stdt = dfhss.loc[dfhss['WT'].between(tmin, tmax)]
		print("\n", " -----> This plate thickness has not been priced yet. Here is a list of plates that are close. <-----")
		print("**ALL DIMENSIONS SHOWN IN INCHES** \n", stdt.sort_values(by='DATE', ascending=False))
	else:
		print("\n"" ----->", t, "inch thick plate was last priced by", stdt.iloc[0, 4], "on", stdt.iloc[0, 6],
			  "for $", stdt.iloc[0, 5], "for a", stdt.iloc[0, 1], "inch X", stdt.iloc[0,2],"inch piece. <-----")





