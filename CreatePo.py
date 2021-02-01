from sheets import *

project_df = pt.loc[pt['STATUS'] != "closed"]
prjctnum = project_df[['PROJECT NUMBER', 'PROJECT NAME']]



project = (input("What project is this po for -----> "))

def CreatePo(num):
    if num in prjctnum:

