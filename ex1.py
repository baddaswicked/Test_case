base=40
per_km=10
total_trip=0

def fn (a):
    global total_trip
    total_trip+=1
    return base+(a*per_km)
print(f"Ваш проїзд обійдеться в {fn(9)} гривень")
print(f"Це ваша {total_trip} поїздка")