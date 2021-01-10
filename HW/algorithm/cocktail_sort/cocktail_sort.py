def cocktailSort(unsorteList):
    listLenth = len(unsorteList)-1

    for i in range(listLenth, 0 , -1):
        isSwapped = False

        for j in range (i, 0, -1):
            if unsorteList[j] < unsorteList[j-1]:
                unsorteList[j], unsorteList[j-1] = unsorteList[j-1], unsorteList[j]
                isSwapped = True
        for j in range (i):
            if unsorteList[j] > unsorteList[j+1]:
                unsorteList[j], unsorteList[j+1] = unsorteList[j+1], unsorteList[j]
                isSwapped = True

        if not isSwapped:
            return unsorteList