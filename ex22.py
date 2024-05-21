"""
вміст файлу : Hello
"""
fh=open("example.txt","r")
for el in range(1,6):
    data=fh.read(1)
    print(data)
fh.close()