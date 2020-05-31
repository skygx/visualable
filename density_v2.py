#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   density_v2.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  19:53   xguo      1.0         None

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

    # Draw Plot
    plt.figure(figsize=(13, 10), dpi=80)
    sns.distplot(df.loc[df['class'] == 'compact', "cty"], color="dodgerblue", label="Compact", hist_kws={'alpha':.7

    }, kde_kws = {'linewidth': 3})
    sns.distplot(df.loc[df['class' ] == 'suv', "cty"], color="orange", label="SUV", hist_kws={'alpha':.7

    }, kde_kws = {'linewidth': 3})
    sns.distplot(df.loc[df['class'] == 'minivan', "cty"], color="g", label="minivan", hist_kws={'alpha':.7

    }, kde_kws = {'linewidth': 3})
    plt.ylim(0, 0.35)

    # Decoration
    plt.title('Density Plot of City Mileage by Vehicle Type', fontsize = 22)
    plt.savefig('./jpg/density-1.jpg')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()