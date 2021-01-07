# 將二分搜尋法 binSearchArray.js 改為迴圈版
## 迴圈版本的二分搜尋函式
```
function bsearchLoop(a, o, from, to){
    var top = to    //last
    var bot = from  //0

    if (bot > top) return null
    var mid = Math.floor((top+bot)/2)

    while (a[mid] != o){
        var mid = Math.floor((top+bot)/2)
        if (bot > top) return null
        if (mid > to) return null
        if (o > a[mid]) bot = mid + 1;
        else if (o < a[mid]) top = mid - 1
        //console.log(mid)
    }
    return mid
}  
```
## 執行結果
```
PS D:\codes\se109a\HW\binarySerachLoop> deno run .\binarySerachLoop.js
t= 2
t= null
t= 5
t= null
```