import pandas as pd
import numpy as np
import matplotlib as plt
import openpyxl

PA_Data = pd.read_excel(r"F:\360MoveData\Users\Dell\Desktop\2019MCM_C\2019MCM_C\data\2018_MCMProblemC_DATA\PA.xlsx")
year = set(PA_Data['YYYY'].values)

for i in year:
  test = PA_Data.loc[PA_Data['YYYY'] == i]
  test.to_csv(r'F:\360MoveData\Users\Dell\Desktop\2019MCM_C\2019MCM_C\data\2018_MCMProblemC_DATA\PA_{0}.csv'.format(i))

