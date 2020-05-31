#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   correlogram_v1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  14:06   xguo      1.0         None

'''

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="once")

def main():
    # Import Dataset
    df = pd.read_csv("./data/mtcars.csv")

    # Plot
    plt.figure(figsize=(12, 10), dpi=80)
    sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0,
                annot=True)

    # Decorations
    plt.title('Correlogram of mtcars', fontsize = 22)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig('./jpg/correlogram.jpg')
    plt.show()


if __name__ == "__main__":
    main()