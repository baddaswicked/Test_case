"""
вміст файлу : Hello
"""
with open("example.txt","w") as fh:
    data=fh.write(" World")
    print(data)
