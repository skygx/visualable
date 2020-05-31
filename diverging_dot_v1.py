#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   diverging_dot_v1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  14:41   xguo      1.0         None

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
    df['colors'] = ['red' if x < 0 else 'darkgreen' for x in df['mpg_z']]
    df.sort_values('mpg_z', inplace=True)
    df.reset_index(inplace=True)

    # Draw plot
    plt.figure(figsize=(14, 16), dpi=80)
    plt.scatter(df.mpg_z, df.index, s=450, alpha=.6, color=df.colors)
    for x, y, tex in zip(df.mpg_z, df.index, df.mpg_z):
        t = plt.text(x, y, round(tex, 1), horizontalalignment='center',
                     verticalalignment='center', fontdict={'color': 'white'})

    # Decorations
    # Lighten borders
    plt.gca().spines["top"].set_alpha(.3)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(.3)
    plt.gca().spines["left"].set_alpha(.3)

    plt.yticks(df.index, df.cars)
    plt.title('Diverging Dotplot of Car Mileage', fontdict = {'size': 20})
    plt.xlabel(' $Mileage$ ')
    plt.grid(linestyle='--', alpha=0.5)
    plt.xlim(-2.5, 2.5)
    plt.savefig('./jpg/diverging_dot.jpg')
    plt.show()


if __name__ == "__main__":
    main()