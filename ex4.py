def fnc(a,b=10, c=2):
    c+=a+b
    return c
result=fnc(10)+fnc(2,5)
print(result)