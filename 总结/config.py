###输入必要参数
#名字
name = 'skirt003'
#成本
product_cost = [15.8,15.8,15.8,15.8,15.8,15.8]
#产品成本利润率
product_cost_revernue_rate = 30/(min(product_cost))
# 产品基准售价
product_sale_price = 8
#重量
product_weight = [0.24,0.24,0.24,0.24,0.24,0.24]
#毛利
maoli =0.15
#尺码
size = ['XS','S','M','L','XL','XXL']
#颜色
color = ['黑色','白色','紫色','灰色','粉色格子','深灰色','浅灰色','藏青色','浅黄色','红色','蓝色']
##基本不变的参数
#费率
feilv =[56.50 ,
99.00 ,
98,
48.40 ,
65.40 ,
49,
54.88,
100.00 ,
99.00 ,
131.00 ,
66.10 ,
75.3,
50.08,
41.01,
46.85,
47.93,
27.00 ,
85.35 ,
47.35,
113.80 ,
51.23,
51.70 ,
51.13,
139.69 ,
132.04 ,
52.00 ,
53.87,
58.84
]
#挂号费
guahaofei = [16.50 ,
16.50 ,
19,
18.70 ,
13.65 ,
17.2,
20.32 ,
16.65 ,
33.50 ,
25.00 ,
24.50 ,
13.2,
17,
26,
18.01,
18.35,
15.50 ,
11.58 ,
18.01,
17.60 ,
23.01,
25.30 ,
17.02,
15.85 ,
15.85 ,
14.50 ,
21.67,
19
]
#28个国家
countrys = ["RU",
"US",
"CA",
"ES",
"FR",
"UK",
"NL",
"IL",
"BR",
"CL",
"AU",
"UA",
"BY",
"JP",
"TH",
"SG",
"KR",
"ID",
"MY",
"PH",
"VN",
"IT",
"DE",
"SA",
"AE",
"PL",
"TR",
"PT"
]
#手续费
shouxufei = 0.92
#折扣
zhekou = 0.71
#汇率
USD_to_RMB = 6.5
#颜色
Color = {'米黄色': 0, '黑色': 1, '蓝色': 2, '湖蓝色': 3, '褐色': 4, '金': 5, '灰色': 6, '深灰': 7, '绿色': 8, '军绿色': 9, '象牙白': 10, '卡其色': 11, '橙色': 12, '粉色': 13, '紫色': 14, '紫罗兰': 15, '红色': 16, '银色': 17, '白色': 18, '黄色': 19, '透明色': 20, '浅绿': 21, '酒红色': 22, '藏青色': 23, '紫红色': 24, '绿松石色': 25, '珊瑚红': 26, '薄荷色': 27, '香槟色': 28, '驼色': 29,'深灰色': 30,'浅灰色': 31,'粉色格子': 32,'浅黄色': 33}
#sku
sku_list = []
#折前价
zheqianjia = []
if len(size) != len(product_weight):
    print('重量和尺寸不匹配')
if len(size) != len(product_cost):
    print('成本和尺寸不匹配')