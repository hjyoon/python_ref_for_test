def upper_bound(s, e, d, l):
    while(e - s > 0):
        m = (s+e)//2
        if(l[m] <= d):
            s = m+1
        else:
            e = m
    return e+1

def lower_bound(s, e, d, l):
    while(e - s > 0):
        m = (s+e)//2
        if(l[m] < d):
            s = m+1
        else:
            e = m
    return e+1

L = [10,10,20,20,20,30,30,40,40,40,40,50,50,60]

print(upper_bound(0, len(L), 15, L))
print(lower_bound(0, len(L), 15, L))