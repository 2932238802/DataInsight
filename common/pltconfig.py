

PLTWIDTH = [5,6,7,8,9,10,11,12,13,14]
PLTHEIGHT = [4,5,6,7,8,9,10]


COLOR= [
    'blue',     # 蓝色（全称）
    'green',    # 绿色（全称）
    'red',      # 红色（全称）
    'cyan',     # 青色（全称）
    'magenta',  # 品红色（全称）
    'yellow',   # 黄色（全称）
    'black',    # 黑色（全称）
    'white',    # 白色（全称）
    'steelblue',# 钢蓝色
    'coral',    # 珊瑚色
    'purple',   # 紫色
    'orange',   # 橙色
    'pink',     # 粉红色
    'gray',     # 灰色（美式拼写）
    'grey',     # 灰色（英式拼写）
    'olive',    # 橄榄色
    'teal',     # 青绿色
    'indigo',   # 靛蓝色
]

PLTKIND = {
    "实线": "-",
    "虚线": "--",
    "点划线": "-.",
    "点线": ":",
}


LEGEND_LOC = {
    "最佳位置": "best",      
    "右上角": "upper right", 
    "左上角": "upper left", 
    "左下角": "lower left",   
    "右下角": "lower right", 
    "右侧中部": "right",     
    "左侧中部": "center left",
    "右侧中部": "center right",
    "底部中部": "lower center",
    "顶部中部": "upper center",
    "正中间": "center",       
}


# 中文到英文颜色映射字典（键值对互换）
CMAP_DICT= {
    '维里迪斯（蓝绿黄渐变）': 'viridis',
    '等离子（深蓝到粉紫渐变）': 'plasma',
    '炼狱（黑红橙渐变）': 'inferno',
    '岩浆（黑红亮黄渐变）': 'magma',
    '公民（蓝绿黄渐变，适合色盲）': 'cividis',
    '灰色系': 'Greys',
    '紫色系': 'Purples',
    '蓝色系': 'Blues',
    '绿色系': 'Greens',
    '橙色系': 'Oranges',
    '红色系': 'Reds',
    '黄橙棕': 'YlOrBr',
    '黄橙红': 'YlOrRd',
    '橙红': 'OrRd',
    '紫粉': 'PuRd',
    '红紫': 'RdPu',
    '蓝紫': 'BuPu',
    '绿蓝': 'GnBu',
    '紫蓝': 'PuBu',
    '黄绿蓝': 'YlGnBu',
    '紫蓝绿': 'PuBuGn',
    '蓝绿': 'BuGn',
    '黄绿': 'YlGn',
    
    '冷暖（蓝白红）': 'coolwarm',
    '蓝白红': 'bwr',
    '地震（蓝白红）': 'seismic',
    '红蓝': 'RdBu',
    '红灰': 'RdGy',
    '紫绿': 'PRGn',
    '粉绿': 'PiYG',
    '棕绿': 'BrBG',
    '紫橙': 'PuOr',
    
    '色相环': 'hsv',
    '暮光': 'twilight',
    '偏移暮光': 'twilight_shifted',
    
    '表格10色': 'tab10',
    '表格20色': 'tab20',
    '表格20色变体b': 'tab20b',
    '表格20色变体c': 'tab20c',
    '柔和色系1': 'Pastel1',
    '柔和色系2': 'Pastel2',
    '配对色系': 'Paired',
    '强调色系': 'Accent',
    '深色系2': 'Dark2',
    '集合1': 'Set1',
    '集合2': 'Set2',
    '集合3': 'Set3',
    
    '冷色': 'cool',
    '热色': 'hot',
    '秋季': 'autumn',
    '冬季': 'winter',
    '春季': 'spring',
    '夏季': 'summer',
    '铜色': 'copper',
    '黑白': 'binary',
    '反色灰阶': 'gist_yarg',
    '灰阶': 'gist_gray',
    '灰度': 'gray',
    '骨色': 'bone',
    '粉色': 'pink',
    '立方螺旋': 'cubehelix',
    '彩虹': 'rainbow',
    '喷气（避免使用，易产生伪影）': 'jet',
    '光谱': 'nipy_spectral',
    '多色': 'gist_ncar',
    
    '海科（蓝黑渐变）': 'mako',
    '冠（青绿渐变）': 'crest',
    '火箭（黑红渐变）': 'rocket',
    '火焰（黄绿红渐变）': 'flare',
    '红蓝发散': 'vlag'
}

