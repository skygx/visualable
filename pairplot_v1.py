#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   pairplot_v1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  14:08   xguo      1.0         None

'''

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="once")

def main():
    # Load Dataset
    # df = sns.load_dataset('iris')
    df=pd.read_csv('./data/iris.csv')
    # Plot
    plt.figure(figsize=(10, 8), dpi=80)
    sns.pairplot(df, kind="scatter", hue="species", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
    plt.savefig('./jpg/pairplot.jpg')
    plt.show()


if __name__ == "__main__":
    main()