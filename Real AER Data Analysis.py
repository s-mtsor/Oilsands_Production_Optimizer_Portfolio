import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import os

#Load AER Data Set
df_AER = pd.read_csv('ST39.csv', encoding='latin-1')

#Inspecting the data to understand its structure and contents
print("\nColumnd:")
print(df_AER.columns.tolist())

print("\nSample data:")
print(df_AER.head(10))

print("\nInfor:")
print(df_AER.info())
