#swap to bitwise
a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print('a=',a)
print('b=',b)
