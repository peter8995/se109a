# TDD(先寫測試再寫程式)
## 實作
一、功能
```
Multiply two numbers.
```
二、寫測試
```
from multiply import multiply

"""
_.multiply(6, 4);
// => 24
"""

print("multiply(6, 4) = {}".format(multiply(6, 4)))
```
三、寫程式
```
def multiply(multiplier, multiplicand):
    return multiplier * multiplicand
```
四、測試
```
PS D:\codes\se109a\HW\lodash\mulitply> python .\multiplyTest.py
multiply(6, 4) = 24
```