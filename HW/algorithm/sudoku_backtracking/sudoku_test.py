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