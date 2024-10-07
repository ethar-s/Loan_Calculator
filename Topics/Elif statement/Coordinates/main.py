def point_location(x, y):
    if x > 0 and y > 0:
        return 'I'
    elif  x > 0 and y < 0:
        return 'IV'
    elif x < 0 and y > 0:
        return 'II'
    elif x < 0 and y < 0:
        return 'III'
    elif (x == 0 and y != 0) or (x != 0 and y == 0):
        return 'One of the coordinates is equal to zero!'
    else:
        return "It's the origin!"

x = float(input())
y = float(input())

print(point_location(x, y))
