# reverse of three digit no. without loop
a=int(input('enter three digit no.'))
b=a%10
a=a//10
c=a%10
a=a//10
d=a%10
print('reverse of three digit no is' ,b,c,d)
