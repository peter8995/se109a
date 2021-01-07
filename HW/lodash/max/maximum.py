#Computes the maximum value of array. 
#If array is empty or falsey, undefined is returned


def maximum(array):
    if len(array) == 0:
        return None
    return max(array)