"""
вміст файлу : Hello
"""
fh=open("example.txt","r")
data=fh.read(3)
print(data)
fh.close()