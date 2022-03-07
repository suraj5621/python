# WAP to enter the coordinates of 2 points (x1, y1)  and (x2, y2) and then find the distance between these two points.

x1=float(input('enetr x1'))
y1=float(input('enetr y1'))
x2=float(input('enetr x2'))
y2=float(input('enetr y2'))

d=((x2-x1)**2 + (y2-y1)**2)**0.5
print('distance is ',d)
