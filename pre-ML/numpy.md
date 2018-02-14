# numpy

### 簡介
- 用c寫, 底層, 比python快很多

### 屬性

- import

```py
import numpy as np
array = np.array([[1,2,3],[2,3,4]])
```

- ndim: 維度
- shape: m x n
- size: 元素個數
- array([], dtype): 創建數組
- zeros: 全為0
- arange: 按指定範圍創建數組
- linshape: 創造線段
- reshpae: 改變形狀

### 運算

- ``+ - * /``

	每個對應元素各自做運算
	
- dot
	矩陣相乘
- sum(), min(), max()
	找行/列中的最小值
- argmin(), argmax(), mean()
	找整個矩陣中的最小值
- cumsum(), diff(), nonzero()
	累加, 差值, 非零元素
- transpose(), clip()
	轉置, 限制元素範圍
	
### Array合併&分割

- concatenate

```py
np.concatenate((arr,arr,arr...), axis=)
```

- split

```py
np.split(arr, chunks, axis=)
np.array_split //不等量
```
