l1 = [6, 5, 3, 1, 8, 7, 2, 4]
def maindef(l1):
    if len(l1) < 2:
        return l1
    
    dnd = len(l1) // 2
    nach = l1[:dnd]
    konec = l1[dnd:]


    nach = maindef(nach)
    konec = maindef(konec)

    i = 0
    j = 0
    arr = []

    while i < len(nach) and j < len(konec):
        if nach[i] < konec[j]:
            arr.append(nach[i])
            i += 1
        elif nach[i] == konec[j]:
            arr.append(nach[i], konec[j])
            i += 1
            j += 1
        else:
            arr.append(konec[j])
            j += 1
        print(arr)
    if len(nach) > len(konec):
        while i != len(nach):
            arr.append(nach[i])
            i += 1
    else:
        while j != len(konec):
            arr.append(konec[j])
            j += 1
        

    return arr

print(maindef(l1))