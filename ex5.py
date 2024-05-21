a=[2,4,6,8,3,10,5]
def fn(a):
    k=0
    for b in a:
        if k<b:
            k=b
    return k
print(fn(a))