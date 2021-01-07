# BDD(口語化的測試語法)
## 參考文件
https://github.com/behave/behave

## 實作
一、安裝behave
```
pip install behave
```
二、在features資料夾下建立sum.feature場景測試文件      

sum.feature
```
Feature: Sum several numbers together

  Scenario: Sum several numbers in a list
    Given we have a list of values
     When we SUM these values
     Then we will get the SUM of the values
```
三、建立steps資料夾，並建立TestSUM.py測試檔案

TestSUM.py
```
from behave import given, when, then
from SUM import SUM

@given('we have a list of values')
def step_impl(context):
    context.array = [4, 2, 8, 6]

@when('we SUM these values')
def step_impl(context):
    context.sum = SUM(context.array)

@then('we will get the SUM of the values')
def step_impl(context):
    print(context.sum)
```
四、建立SUM函式

SUM.py
```
# Computes the sum of the values in array.

def SUM(array):
    return sum(array)
```
五、測試
```
PS D:\codes\se109a\HW\lodash\sum\features> behave sum.feature
Feature: Sum several numbers together # sum.feature:1

  Scenario: Sum several numbers in a list  # sum.feature:3
    Given we have a list of values         # steps/TestSUM.py:4
    When we SUM these values               # steps/TestSUM.py:8
    Then we will get the SUM of the values # steps/TestSUM.py:12

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.003s
```