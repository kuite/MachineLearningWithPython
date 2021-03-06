import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# DIAGRAM WORKS ONLY IN DEBUG MODE

def plot_corr(df, size=10):
    """
    Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot

    Displays:
        matrix of correlation between columns.  Blue-cyan-yellow-red-darkred => less to more correlated
                                                0 ------------------>  1
                                                Expect a darkred line running from top left to bottom right
    """

    corr = df.corr()  # data frame correlation function
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)  # color code the rectangles by correlation value
    plt.xticks(range(len(corr.columns)), corr.columns)  # draw x tick marks
    plt.yticks(range(len(corr.columns)), corr.columns)  # draw y tick marks

df = pd.read_csv('data/pima-data.csv')
df.shape
print('----------1-----')
print(df.head(5))
print('--------2-----')
print(df.shape)
print('------3--------')

# print(plot_corr(df))
plot_corr(df)
print('--------4----------')
df.corr()

print(df.corr())

del df['skin']
print(df.head())

plot_corr(df)
input("Press ENTER to continue.")
