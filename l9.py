# input universityroll and sum of last three digit of university roll no.
a=int(input('enter the university roll no'))
b=a%10
a=a//10
c=a%10
a=a//10
d=a%10
sum=b+c+d
print('sum of last three digit of univ.rollno. is ',sum)
