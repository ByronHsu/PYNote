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