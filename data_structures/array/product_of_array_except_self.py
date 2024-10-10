def product(arr):
    prods = [1] * len(arr)

    temp = 1

    for i in range(len(arr)):
        prods[i] = temp
        temp = temp * arr[i]

    temp = 1

    for i in reversed(range(len(arr))):
        prods[i] = prods[i] * temp
        temp = temp * arr[i]
    
    return temp
