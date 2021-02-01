# calculation for square tube wt/ft
from sheets import *

def SquareCalc():
    h = float(input("Square tube dimension ----> "))
    w = h
    wt = float(input("Wall thickness ----> "))
    hmin = h - 1
    hmax = h + 1
    stwt = (2 * wt * (h + w - 8 * wt) + 9.4248 * (wt * wt)) * 3.40277

def SquareCost(h, w, wt):
    dfhss = df.loc[df['MT'] == 'HSS']
    saCol = dfhss.loc[dfhss['SIZE A'] == h]
    if saCol.empty:
        saCol = dfhss.loc[dfhss["SIZE A"].between(hmin, hmax)]
        print("\n -----> That material size has not been quoted. <-----")
        print(saCol.sort_values(by='DATE'))
        print(" ----->", h, "X", w, "X", wt, "square tube is approximately", str(round(stwt, 2)), "lbs per foot. <----- \n",
            "-----> Structural tubing is generally available in 20', 24', 30', 32', 34', 40', 48', 56' and 60' lengths. <----- \n")
    else:
        sbCol = saCol.loc[saCol['SIZE B'] == w]
        if sbCol.empty:
            print("\n"" -----> That material size has not been quoted. Here is a list of like material <-----")
            print(saCol.sort_values(by='DATE', ascending=False))
            print(" ----->", h, "X", w, "X", wt, "square tube is approximately", str(round(stwt, 2)), "lbs per foot.",
                  "<-----")
            print(" ----->",
                  "Structural tubing is generally available in 20', 24', 30', 32', 34', 40', 48', 56' and 60' lengths. <-----",
                  "\n")
        else:
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
                print("\n"" ----->", h, "X", w, "X", wt, "was last priced by", stdt.iloc[0, 4], "on", stdt.iloc[0, 7], "for $",stdt.iloc[0, 5], "for a", stdt.iloc[0, 6], "foot stick." " <-----")
                print(" ----->", h, "X", w, "X", wt, "square tube is approximately", str(round(stwt, 2)), "lbs per foot.","<-----")
                print(" ----->","Structural tubing is generally available in 20', 24', 30', 32', 34', 40', 48', 56' and 60' lengths. <-----",
                      "\n")