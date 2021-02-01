from sheets import *
from TubeCalc import *
from SquareCalc import *
from RectCalc import *
from AngleCalc import *
from PlateCalc import *

from SquareCalc import *


def SqTbCost(h,w):
    dfhss = df.loc[df['MT'] == 'HSS']
    dfhss_sqtb = df.loc[(df['SIZE A'] == SquareCalc.h) & (df['SIZE B'] == SquareCalc.w)]
    stdt = dfhss_sqtb.sort_values(by=['DT QT'])
    print (stdt.iloc[0,:])









