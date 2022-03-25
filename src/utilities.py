def findObject(arr, attr, value):
    for x in arr:
        if x[attr] == value:
            return x
