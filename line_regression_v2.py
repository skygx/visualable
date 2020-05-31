#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   line_regression_v2.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  13:08   xguo      1.0         None

'''

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="once")

def main():
    # Import Data
    df = pd.read_csv("./data/mpg_ggplot2.csv")
    df_select = df.loc[df.cyl.isin([4, 8]), :]

    # Each line in its own column
    sns.set_style("white")
    gridobj = sns.lmplot(x="displ", y="hwy",
                         data=df_select,
                         height=7,
                         robust=True,
                         palette='Set1',
                         col="cyl",
                         scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

    # Decorations
    gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
    plt.savefig('./jpg/line_regression1.jpg')
    plt.show()


if __name__ == "__main__":
    main()