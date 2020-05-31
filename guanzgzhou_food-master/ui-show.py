#!/usr/bin/env python
# coding: utf-8

# #  导入库与数据

# In[2]:


import pandas as pd
from IPython.display import display
import warnings # 忽略打印的警告
warnings.filterwarnings('ignore')


# In[3]:


a_food = pd.read_csv('A网站美食数据.csv',encoding='gbk')
b_food = pd.read_csv('B网站美食数据.csv',encoding='gbk')
local = pd.read_csv('店铺地图信息.csv',encoding='gbk')
display(a_food.head())
display(b_food.head())
display(local.head())


# # 合并数据集

# In[4]:


# 修改 A 的【名称】列为【店铺名称】，【类别】列为【菜系】
# 【人均价格】的【元】去掉
a_food.rename(columns={'名称':'店铺名称','类别':'菜系'},inplace=True)
a_food['人均价格'] = a_food['人均价格'].str.replace('元','')
a_food.head(1)


# In[5]:


# 纵向合并两个网站数据，去重
display(a_food.shape)
display(b_food.shape)
food = pd.concat([a_food,b_food],ignore_index=True).drop_duplicates()
display(food.shape)


# In[6]:


# 以【店铺id】为键进行合并，没有 ID 的店铺会丢掉
food1 = pd.merge(food,local,on='店铺ID')
food1.shape


# # 选择需要的列，查看缺失值，类型

# In[7]:


df = food1[['店铺名称','评论数','人均价格','菜系','商圈','推荐1','推荐2','推荐3',
           '口味评分','环境评分','服务评分','星级','纬度','经度','行政区名称']]
df.info()


# # 广州美食地图分布

# In[8]:


from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType
from pyecharts.globals import ThemeType

def geo():
    g = Geo(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
    g.add_schema(maptype='广州')

    # 定义坐标对应的名称，添加到坐标库中 add_coordinate(name, lng, lat)
    names = list(df['店铺名称'])
    lng = list(df['经度'])
    lat = list(df['纬度'])
    for i in range(len(names)):
        g.add_coordinate(names[i],lng[i],lat[i])

    # 定义数据对，
    data_pair = [(name,50) for name in names]

    # 将数据添加到地图上
    g.add('', data_pair, type_=GeoType.EFFECT_SCATTER, symbol_size=3)

    # 设置样式
    g.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    g.set_global_opts(
            visualmap_opts=opts.VisualMapOpts(is_show=False),
            title_opts=opts.TitleOpts(title="广州美食分布"),
        )
    g.render('广州美食分布.html')
    return g


# # 哪个行政区美食最多

# In[9]:


# 计算每个行政区的美食数
region = df['行政区名称'].value_counts()
region


# In[10]:


# 绘制饼图
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

def pie():
    x = ['天河区', '越秀区', '海珠区', '荔湾区', '番禺区', '白云区', '黄埔区']
    y = [164, 69, 68, 27, 23, 20, 1]

    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add("", [list(z) for z in zip(x, y)])
        .set_global_opts(title_opts=opts.TitleOpts(title="行政区美食占比"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    c.render('行政区美食占比.html')
    return c


# # 集中在哪些商圈

# In[103]:


bussiness_area = df['商圈'].value_counts()
bussiness_area


# In[104]:


from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

def bar():
    x = ['珠江新城','天河城/体育中心','北京路','江南西','天河北','机场路',
         '江南大道','高德置地/花城汇','石牌/龙口','兴盛路/跑马场']
    y = [60, 42, 34, 23, 22, 10, 10, 10, 10, 10]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add_xaxis(x)
        .add_yaxis("",y)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="商圈分布"),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)))
    )
    c.render('商圈分布.html')
    return c


# # 星级分布

# In[105]:


start = df['星级'].value_counts()
start


# In[106]:


from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

def pie_circle():
    x = ['四星商户','准五星商户','五星商户','准四星商户']
    y = [175,156,34,7]

    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add(
            "",
            [list(z) for z in zip(x,y)],
            radius=["40%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="星级占比"))
    )
    c.render('星级占比.html')
    return c


# # 美食类型

# In[107]:


kind = df['菜系'].value_counts()
kind


# In[108]:


from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

def bar_reserve():
    # 坐标轴不够，就取前 20
    x = ['西餐',
     '粤菜',
     '日本料理',
     '火锅',
     '面包甜点',
     '自助餐',
     '烧烤',
     '咖啡厅',
     '东南亚菜',
     '川菜',
     '茶餐厅',
     '韩国料理',
     '创意菜',
     '韩式料理',
     '湘菜',
     '素菜',
     '海鲜',
     '小龙虾',
     '茶餐馆',
     '江浙菜',
     '其他美食',
     '台湾菜',
     '快餐简餐',
     '西北菜',
     '私房菜',
     '新疆菜',
     '家常菜',
     '粥粉面']
    x = x[::-1][8:]
    y = [61,
     53,
     52,
     43,
     21,
     20,
     18,
     14,
     11,
     11,
     9,
     9,
     7,
     6,
     6,
     5,
     4,
     4,
     3,
     3,
     3,
     2,
     2,
     1,
     1,
     1,
     1,
     1]
    y = y[::-1][8:]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add_xaxis(x)
        .add_yaxis("", y)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="美食种类分布"))
    )
    c.render('美食种类分布.html')
    return c


# # 推荐美食词云

# In[109]:


# 将所有推荐美食连接起来
w1 = list(df['推荐1'])
w2 = list(df['推荐2'])
w3 = list(df['推荐3'])
w1 = ''.join(w1)
w2 = ''.join(w2)
w3 = ''.join(w3)
txt = w1 + w2 + w3

# 分词
import jieba
ls = jieba.lcut(txt)

# 计算词频
word = {}
for w in ls:
    word[w] = word.get(w,0) + 1

words = list(word.items())


# In[110]:


from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
from pyecharts.globals import ThemeType

def worldcloud():
    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
        .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    c.render('美食词云.html')
    return c


# # 评论数，人均价格，口味评分，环境评分，服务评分的相关性

# In[111]:


# 【人均价格】去掉【元】并转换为 float64，并计算相关性
num = df[['评论数','人均价格','口味评分','环境评分','服务评分']]
num['人均价格'] = num['人均价格'].astype(float)
num_corr = num.corr()
num_corr


# In[112]:


from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import HeatMap

def heat_corr():
    # 将上面的相关系数矩阵处理一下
    value = [[0,0,1.00],[0,1,0.04],[0,2,-0.07],[0,3,-0.05],[0,4,-0.28],
             [1,0,0.04],[1,1,1.00],[1,2,0.13],[1,3,0.40],[1,4,0.33],
             [2,0,-0.07],[2,1,0.13],[2,2,1.00],[2,3,0.25],[2,4,0.52],
             [3,0,-0.05],[3,1,0.40],[3,2,0.25],[3,3,1.00],[3,4,0.68],
             [4,0,-0.28],[4,1,0.33],[4,2,0.52],[4,3,0.68],[4,4,1.00]]

    c = (
        HeatMap(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add_xaxis(['评论数','人均价格','口味评分','环境评分','服务评分'])
        .add_yaxis(
            "",
            ['评论数','人均价格','口味评分','环境评分','服务评分'],
            value,
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="评论数，人均价格，口味评分，环境评分，服务评分相关性热力图",
                                     pos_left='center'),
            visualmap_opts=opts.VisualMapOpts(is_show=False,min_=-1,
                                              max_=1),
        )
    )
    c.render('相关性热力图.html')
    return c


# # 综合评分与人均价格关系

# In[113]:


'''
综合评分=（口味评分+环境评分+服务评分）/ 3 
'''
score = df[['人均价格','口味评分','环境评分','服务评分']]
score['人均价格'] = score['人均价格'].astype(float)
score['综合评分'] = (score['口味评分']+score['环境评分']+score['服务评分']) / 3
score.head(1)


# In[114]:


import pyecharts.options as opts
from pyecharts.charts import Scatter
from pyecharts.globals import ThemeType

def scatter():
    x_data = list(score['人均价格'])
    y_data = list(score['综合评分'])

    c = (
        Scatter(init_opts=opts.InitOpts(width="800px", height="500px",
                                       theme=ThemeType.PURPLE_PASSION))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="",
            y_axis=y_data,
            symbol_size=20,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_series_opts()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
                ,name='人均价格'
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                name='评分'
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
        )
    )
    c.render('人均消费与综合评分散点.html')
    return c


# # 仪表盘

# In[120]:


from pyecharts.charts import Page
def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        geo(),
        pie(),
        bar(),
        pie_circle(),
        bar_reserve(),
        worldcloud(),
        heat_corr(),
        scatter()
    )
    page.render('page.html')

    
if __name__ == "__main__":
    # page_draggable_layout()
    Page.save_resize_html('page.html', cfg_file='page.json',
                        dest='仪表盘.html')


# In[ ]:




