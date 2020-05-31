#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   versual_version.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/29  20:24   xguo      1.0         None

'''
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="once")

def main():
    large = 22;
    med = 16;
    small = 12
    params = {'axes.titlesize': large,
              'legend.fontsize': med,
              'figure.figsize': (16, 10),
              'axes.labelsize': med,
              'axes.titlesize': med,
             'xtick.labelsize': med,
              'ytick.labelsize': med,
              'figure.titlesize': large}
    plt.rcParams.update(params)
    plt.style.use('seaborn-whitegrid')
    sns.set_style("white")
    # %matplotlib
    # inline

    # Version
    print(mpl.__version__)  # > 3.0.0
    print(sns.__version__)  # > 0.9.0


if __name__ == "__main__":
    main()