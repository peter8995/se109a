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
