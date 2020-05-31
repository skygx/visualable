#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   count_v1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  13:15   xguo      1.0         None

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
    df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')

    # Draw Stripplot
    fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
    sns.stripplot(df_counts.cty, df_counts.hwy, size=df_counts.counts * 2, ax=ax)

    # Decorations
    plt.title('''Counts Plot - Size of circle is bigger as more points overlap''', fontsize = 22)
    plt.savefig('./jpg/counts.jpg')
    plt.show()


if __name__ == "__main__":
    main()