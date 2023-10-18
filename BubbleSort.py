def burbuja_optimus(lis):
    n = len(lis)
  
    for i in range(n-1):
        for j in range(n-1-i):
            if lis[j] > lis[j+1] :
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis