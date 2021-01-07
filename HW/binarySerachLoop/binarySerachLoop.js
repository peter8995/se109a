// from https://gitlab.com/ccc109/se/-/blob/master/deno/alg/00-complexity/bigO/binSearchArray.js

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


  function search(a, o) {
     var n = a.length-1
     return bsearchLoop(a, o, 0, n)
  }
  
  var t = search([1, 3, 4, 6, 7, 8], 4)
  console.log('t=', t)
  var t = search([1, 3, 4, 6, 7, 8], 5)
  console.log('t=', t)
  var t = search([1, 3, 4, 6, 7, 8], 8)
  console.log('t=', t)
  var t = search([1, 3, 4, 6, 7, 8], 9)
  console.log('t=', t)
  