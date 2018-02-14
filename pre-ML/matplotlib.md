# Matplotlib

### 基礎應用

```py
x = np.linspace(-1, 1, 50)
y = 2*x + 1
# 使用plt.figure定义一个图像窗口. 使用plt.plot画(x ,y)曲线. 使用plt.show显示图像.
plt.figure()
plt.plot(x, y)
plt.show()
```

### 設置座標軸

```py
plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# 使用plt.xlim设置x坐标轴范围 使用plt.ylim设置y坐标轴范围
# 使用plt.xlabel设置x坐标轴名称 使用plt.ylabel设置y坐标轴名称
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')
plt.show()

# 使用plt.xticks设置x轴刻度
# 使用plt.yticks设置y轴刻度以及名称
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()

# get current axis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()

# 使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置：
# bottom.（所有位置：top，bottom，both，default，none）
ax.xaxis.set_ticks_position('bottom')

# 使用.spines设置边框：x轴；使用.set_position设置边框位置：
# y=0的位置；（位置所有属性：outward，axes，data）
ax.spines['bottom'].set_position(('data', 0))
plt.show()
```

### Legend圖例

```py
# 第一種方法
# set line labels
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
plt.legend(loc='upper right')
# 第二種方法-handles
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
```

### Annotation

```py
x0 = 1
y0 = 2*x0 + 1
# 畫線 black and dotted
# [x0, x1] [y0, y1]
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5) 
# set dot styles
# s: size
plt.scatter([x0, ], [y0, ], s=50, color='b')
# 添加注釋
# xycoords: 基於數據的值來選位置, xytext: 對標注位置的描述和xy偏差值
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
# (-3.7, 3) 選取text位置
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})
```

### tick可見度

```py
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
	# 其中label.set_fontsize(12)重新调节字体大小
	# bbox设置目的内容的透明度相关参，facecolor调节 box 前景色
	# edgecolor 设置边框， alpha设置透明度
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))
plt.show()
```

### scatter

```py
import matplotlib.pyplot as plt
import numpy as np

n = 1024    # data size
X = np.random.normal(0, 1, n) # 每一个点的X值
Y = np.random.normal(0, 1, n) # 每一个点的Y值
T = np.arctan2(Y,X) # for color value
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.show()
```

### bar

```py
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
```

### contours 等高線圖

```py
def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)
# use plt.contourf to filling contours
# X, Y and value for (X,Y) point
# 8: 分成幾層
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

# 添加高度數字
plt.clabel(C, inline=True, fontsize=10)
plt.xticks(())
plt.yticks(())
```

### image 圖片

```py

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()
```

### 3D

```py
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)
# 畫立體圖
# rstride, cstride: x, y的跨度
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# 等高線 投影到xy平面上
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
```

### subplot

```py
plt.figure()
plt.subplot(2,2,1)
# 使用plt.subplot来创建小图. plt.subplot(2,2,1)表示将整个图像窗口分为2行2列, 当前位置为1. 
# 使用plt.plot([0,1],[0,1])在第1个位置创建一个小图.
# x: [0,1], y: [0,1]
plt.plot([0,1],[0,1])
...
plt.show()  # 展示
```

```py
# method1: subplot2grid
# 使用plt.subplot2grid来创建第1个小图
# (3,3)表示将整个图像窗口分成3行3列, (0,0)表示从第0行第0列开始作图
# colspan=3表示列的跨度为3, rowspan=1表示行的跨度为1. colspan和rowspan缺省, 默认跨度为1.
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax1.plot([1, 2], [1, 2])    # 画小图
ax1.set_title('ax1_title')  # 设置小图的标题

# method2: gridspec
gs = gridspec.GridSpec(3, 3)
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])

# method3: subplots
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])
plt.tight_layout()
plt.show()
```

### 圖中圖

```py
# 大圖
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')
# 小圖
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(y, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')
```