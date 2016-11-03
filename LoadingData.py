import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/pima-data.csv')
df.shape
print(df.head(5))
print(df.isnull().values.any())
