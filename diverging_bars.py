#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   diverging_bars.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  14:35   xguo      1.0         None

'''
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="once")

def main():
    # Prepare Data
    df = pd.read_csv("./data/mtcars.csv")
    x = df.loc[:, ['mpg']]
    df['mpg_z'] = (x - x.mean()) / x.std()
    df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
    df.sort_values('mpg_z', inplace=True)
    df.reset_index(inplace=True)

    # Draw plot
    plt.figure(figsize=(14, 10), dpi=80)
    plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)

    # Decorations
    plt.gca().set(ylabel= '$Model$', xlabel =' $Mileage$ ')
    plt.yticks(df.index, df.cars, fontsize=12)
    plt.title('''Diverging Bars of Car Mileage''', fontdict = {'size': 20})
    plt.grid(linestyle='--', alpha=0.5)
    plt.savefig('./jpg/diverging_bars.jpg')
    plt.show()

if __name__ == "__main__":
    main()