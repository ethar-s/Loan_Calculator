import math

def area_of_circle(r):
    return round(math.pi * math.pow(r, 2), 2)

num = int(input())
print(area_of_circle(num))