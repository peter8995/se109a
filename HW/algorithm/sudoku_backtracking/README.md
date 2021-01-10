# 數獨-使用Backtracking解決
## 釐清問題
先找出需要填入數字的格子，在一個一個數字填進去，判斷是否符合規則，是的話就繼續下一隔，否的話就回上一步。
### 先創一個矩陣裡面放置要解決的數獨題目
```
question = [
    [0,7,0,5,3,0,0,0,0],
    [8,0,1,6,0,0,2,0,7],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,4,0,6,0,0,0],
    [3,0,0,0,0,0,7,4,5],
    [0,8,0,0,0,0,0,0,6],
    [4,0,5,0,0,0,0,7,0],
    [0,0,3,1,0,0,0,2,9],
    [0,0,0,0,0,0,5,0,0]
]
```
#### 建立顯示數獨的函數
```
def print_sudoku(board):
    rowCount = len(board)
    colCount = len(board[0])

    # print row
    for i in range (rowCount):
        if i % 3 == 0 and i != 0:
            print("----------------------") 
        # print column
        for j in range (colCount):
            if j % 3 == 0 and j != 0:
                print("| ", end = '')
            if j != 8:
                print("{} ".format(board[i][j]), end = '')
            else:
                print(board[i][j])
```
### 解題
```
def solve (board):
    emptySpot = findEmpty(board)
    if not emptySpot:
        return True
    else row, col = emptySpot

    for i in range (1, 10):
        # if the valus is available fill it into board
        if available(board, i, row, col):
            board[row][col] = i
            
            # after fill it into board keep solve this question
            if solve(board):
                return True
            
            board[row][col] = 0
    return False
```
#### 找出空白的格子
```
def findEmpty(board):
    rowCount = len(board)
    colCount = len(board[0])

    for i in range (rowCount):
        for j in range (colCount):
            if board[i][j] == 0:
                return (i, j)       # i = row, j = col
    return None
```
#### 判斷是否符合規則
```
def available(board, ans, row, col):
    # check row
    for i in range (9):
        if board[row][i] == ans and col != i:
            return False
    
    # check column
    for i in range (9):
        if board[i][col] == ans and row != i:
            return False
        
    # check 3*3
    boxIndexR = row // 3
    boxIndexC = col // 3
    
    for i in range (boxIndexR * 3, boxIndexR * 3 + 3):
        for j in range (boxIndexC * 3, boxIndexC *3 + 3):
            if board[j][i] == ans and (j, i) != (row, col):
                return False
    return True
```
## 測試程式
### 程式碼
```
from sudoku import printSudoku
from sudoku import startSolve

sudoku = [
    [0,7,0,5,3,0,0,0,0],
    [8,0,1,6,0,0,2,0,7],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,4,0,6,0,0,0],
    [3,0,0,0,0,0,7,4,5],
    [0,8,0,0,0,0,0,0,6],
    [4,0,5,0,0,0,0,7,0],
    [0,0,3,1,0,0,0,2,9],
    [0,0,0,0,0,0,5,0,0]
]

printSudoku(sudoku)
solvedSudoku = startSolve(sudoku)
print("************************") 
printSudoku(solvedSudoku)
```
### 結果
```
PS D:\codes\se109a\hw\algorithm\sudoku_backtracking> python .\sudoku_test.py
0 7 0 | 5 3 0 | 0 0 0
8 0 1 | 6 0 0 | 2 0 7
0 0 0 | 0 0 0 | 0 1 0
----------------------
0 0 0 | 4 0 6 | 0 0 0
3 0 0 | 0 0 0 | 7 4 5
0 8 0 | 0 0 0 | 0 0 6
----------------------
4 0 5 | 0 0 0 | 0 7 0
0 0 3 | 1 0 0 | 0 2 9
0 0 0 | 0 0 0 | 5 0 0
************************
6 7 2 | 5 3 1 | 9 8 4
8 3 1 | 6 4 9 | 2 5 7
5 4 9 | 8 2 7 | 6 1 3
----------------------
1 5 7 | 4 9 6 | 8 3 2
3 9 6 | 2 1 8 | 7 4 5
2 8 4 | 7 5 3 | 1 9 6
----------------------
4 1 5 | 9 6 2 | 3 7 8
7 6 3 | 1 8 5 | 4 2 9
9 2 8 | 3 7 4 | 5 6 1
```
## 時間複雜度分析
假設有m個格子要解決，每個格子有n種可能性，複雜度就為O(n*m)。