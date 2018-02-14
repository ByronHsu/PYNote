# python-basic

### 變數範圍
1. 變數範圍的建立是在指定時發生，而不是在取用時發生

2. 實際上，在Python中變數可以在四個範圍中建立或尋找。
	1. 函式（Local functon）
	2. 外包函式（Endosing function）
	3. 全域（Global）
	4. 內建（Builtin）
	
	```py
	x = 10       　　# 全域
	
	def outer():
		y = 20        # 在 outer() 函式範圍
	
		def inner():
			z = 30    # 在 inner() 函式範圍
			print(x)  # 往外找到global的x
			print(y)  # 往外找到outer的x
	
	print(x)       # 往外找到global的x
	```
3. ``global`` and ``nonlocal``
	1. ``global``: 表明為global變數, 不會再重新創建
	
	```py
	x = 10
	def some():
		global x
		x = 20
	```
	
	2. ``nonlocal``: 表明為非local變數, 不會再重新創建
		