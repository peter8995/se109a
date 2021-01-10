# 雞尾酒排序法
雞尾酒排序法，一種泡沫排序法的變形，與泡沫排序法之差別為其在排序時是雙向進行的，而泡沫排序法是單向進行。
## 想法
從陣列中第一個數字開始，若比後面一個數字大，則調換位置，同時最後一個數字若是比前一個數字小，則調換位置。
## 程式碼
```
def cocktailSort(unsorteList):
    listLenth = len(unsorteList)-1

    for i in range(listLenth, 0 , -1):
        # 定義一個是否有做調換的布林值
        isSwapped = False

        for j in range (i, 0, -1):
            # 若j的值比前一個數字小，則對調位置
            if unsorteList[j] < unsorteList[j-1]:
                unsorteList[j], unsorteList[j-1] = unsorteList[j-1], unsorteList[j]
                isSwapped = True
        for j in range (i):
            # 若j的值比其後一個數字大，則對調位置
            if unsorteList[j] > unsorteList[j+1]:
                unsorteList[j], unsorteList[j+1] = unsorteList[j+1], unsorteList[j]
                isSwapped = True

        if not isSwapped:
            return unsorteList      # 若是都沒有調換位置，則代表排序完成
```
## 測試程式
```
from cocktail_sort import cocktailSort

"""
>>> cocktail_sort([3, 8, 2, 1, 2])
[1, 2, 2, 3, 8]
>>> cocktail_sort([-6, 8, 0, 3, 2, 18])
[-6, 0, 2, 3, 8, 18]
>>> cocktail_sort([0.3, -3.5, 6.7, 1.5])
[-3.5, 0.3, 1.5, 6.7]
>>> cocktail_sort([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]
>>> cocktail_sort([-8, -15, -6, -2, -25])
[-25, -15, -8, -6, -2]
"""
list1 = [3, 8, 2, 1, 2]
list2 = [-6, 8, 0, 3, 2, 18]
list3 = [0.3, -3.5, 6.7, 1.5]
list4 = [1, 2, 3, 4, 5]
list5 = [-8, -15, -6, -2, -25]

print("cocktail_sort([3, 8, 2, 1, 2]) = {}".format(cocktailSort(list1)))
print("cocktail_sort([-6, 8, 0, 3, 2, 18]) = {}".format(cocktailSort(list2)))
print("cocktail_sort([0.3, -3.5, 6.7, 1.5]) = {}".format(cocktailSort(list3)))
print("cocktail_sort([1, 2, 3, 4, 5]) = {}".format(cocktailSort(list4)))
print("cocktail_sort([-8, -15, -6, -2, -25]) = {}".format(cocktailSort(list5)))
```
## 測試結果
```
PS D:\codes\se109a\HW\algorithm\cocktail_sort> python .\cocktail_sort_test.py
cocktail_sort([3, 8, 2, 1, 2]) = [1, 2, 2, 3, 8]
cocktail_sort([-6, 8, 0, 3, 2, 18]) = [-6, 0, 2, 3, 8, 18]
cocktail_sort([0.3, -3.5, 6.7, 1.5]) = [-3.5, 0.3, 1.5, 6.7]
cocktail_sort([1, 2, 3, 4, 5]) = [1, 2, 3, 4, 5]
cocktail_sort([-8, -15, -6, -2, -25]) = [-25, -15, -8, -6, -2]
```
## 時間複雜度分析
1. 最外層迴圈
```
for i in range(listLenth, 0 , -1):
```
>>n

2. 裡面的兩個迴圈
```
for j in range (i, 0, -1):
```
```
for j in range (i):
```
>>2n

所以複雜度應該是n*2n但是因為計算複雜度時不考慮係數，所以複雜度也是O(n^2)。
