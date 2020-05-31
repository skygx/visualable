#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   pairplot_v2.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  14:33   xguo      1.0         None

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
    df = sns.load_dataset('iris')
    # df = pd.read_csv('./data/iris.csv')
    # Plot
    plt.figure(figsize=(10, 8), dpi=80)
    sns.pairplot(df, kind="reg", hue="species")
    plt.savefig('./jpg/pairplot1.jpg')
    plt.show()


if __name__ == "__main__":
    main()