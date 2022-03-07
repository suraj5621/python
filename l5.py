# to find compound interest
p=float(input('enter the principle amount'))
r=float(input('enter the rate'))
t=float(input('enter the time'))
a=p*((1+(r/100))**t)
ci=a-p
print('compound intrest is ',ci)
