#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   scatt_v1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/29  20:29   xguo      1.0         None

'''
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="once")


def main():
    midwest = pd.read_csv("./data/midwest_filter.csv")

    # Prepare Data
    # Create as many colors as there are unique midwest[ category ]
    categories = np.unique(midwest["category"])
    colors = [plt.cm.tab10(i / float(len(categories) - 1)) for i in range(len(categories))]

    # Draw Plot for Each Category
    plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

    for i, category in enumerate(categories):
        plt.scatter("area", "poptotal",
                    data=midwest.loc[midwest.category == category, :],
                    s=20, c=colors[i], label=str(category))

    # Decorations
    plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
                  xlabel="Area", ylabel="Population")

    plt.xticks(fontsize=12);
    plt.yticks(fontsize=12)
    plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
    plt.legend(fontsize=12)
    plt.savefig('./jpg/scatt.jpg')
    plt.show()


if __name__ == "__main__":
    main()