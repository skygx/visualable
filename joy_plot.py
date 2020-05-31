#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   joy_plot.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/31  19:57   xguo      1.0         None

'''

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import joypy
warnings.filterwarnings(action="once")

def main():
    # !pip install joypy
    # Import Data
    mpg = pd.read_csv("./data/mpg_ggplot2.csv")

    # Draw Plot
    plt.figure(figsize=(16, 10), dpi=80)
    fig, axes = joypy.joyplot(mpg, column=['hwy', 'cty'], by="class", ylim='own', figsize=(14, 10))

    # Decoration
    plt.title('Joy Plot of City and Highway Mileage by Class', fontsize = 22)
    plt.savefig('./jpg/joy_plot.jpg')
    plt.show()


if __name__ == "__main__":
    main()