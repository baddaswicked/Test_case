"""
вміст файлу : Hello
"""
with open("example.txt","a") as fh:
    data=fh.write(" World")
    print(data)
