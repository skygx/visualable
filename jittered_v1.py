#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   jittered_v1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  13:11   xguo      1.0         None

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

    # Draw Stripplot
    fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
    sns.stripplot(df.cty, df.hwy, jitter=0.25, size=8, ax=ax, linewidth=.5)

    # Decorations
    plt.title('''Use jittered plots to avoid overlapping of points''', fontsize = 22)
    plt.savefig('./jpg/jittered.jpg')
    plt.show()

if __name__ == "__main__":
    main()