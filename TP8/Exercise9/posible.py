def pos(lis, k, pref = ""):
     if k == 0:
        print(pref)
     else:
        for i in lis:
            pos(lis, k - 1, pref + i)
