"""
вміст файлу : Hello
"""
fh=open("example.txt","r")
fh.seek(2)
data=fh.read(3)
print(data)
fh.close()