import pandas as pd
import numpy as np
import matplotlib as plt
import openpyxl

State = ['KY', 'VA', 'OH', 'PA', 'WV']
def writeData(df, name, nan_excel):
  data = df[df['State'].isin([name])]
  data.to_excel(r"F:\360MoveData\Users\Dell\Desktop\2019MCM_C\2019MCM_C\data\2018_MCMProblemC_DATA\{0}.xlsx".format(name))


df = pd.read_excel(r"F:\360MoveData\Users\Dell\Desktop\2019MCM_C\2019MCM_C\data\2018_MCMProblemC_DATA\MCM_NFLIS_Data.xlsx",
                  sheet_name = 'Data')

df = pd.DataFrame(df)

nan_excel = pd.DataFrame()
for i in State:
  writeData(df, i, nan_excel)

