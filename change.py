## Importing Required Libraries ##
import pandas as pd
import os
import numpy as np

## Loading data ##
oct = pd.read_csv("oct.csv")
nov = pd.read_csv("nov.csv")

## Killing NA's ##
oct = oct.fillna(0)
nov = nov.fillna(0)

## Comparison between sets ##
comparison_values = oct.values == nov.values
print (comparison_values)

## Numpy where function ##
rows, cols=np.where(comparison_values==False)

## Identifying and marking changes ##
for item in zip(rows,cols):
    oct.iloc[item[0], item[1]] = '{} !!! {}'.format(oct.iloc[item[0], item[1]],nov.iloc[item[0], item[1]])

## Saving new sheet with differences noted ##
oct.to_excel('./novchange.xlsx',index=False,header=True)