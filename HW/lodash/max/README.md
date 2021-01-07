# 傳統方法(先程式再測試)
## 實作
一、功能
```
Computes the maximum value of array. If array is empty or falsey, undefined is returned.
```
二、寫程式
```
def maximum(array):
    if len(array) == 0:
        return None
    return max(array)
```
三、寫測試程式
```
from maximum import maximum

"""
_.max([4, 2, 8, 6]);
// => 8
 
_.max([]);
// => undefined
"""
print("max([4, 2, 8, 6]) = {}".format(maximum([4, 2, 8, 6])))
print("max([]) = {}".format(maximum([])))
```
四、測試
```
PS D:\codes\se109a\HW\lodash\max> python maxTest.py
max([4, 2, 8, 6]) = 8
max([]) = None
```