# database
d={}
ss={}
avg={}
per={}
n=int(input('enter how many no. of students database you want to create'))
for i in range(n):
	roll=int(input('enter the university rollno.'))
	d1={}
	for j in range(5):
		sub=input('enter the subject name')
		values=int(input('enter the marks'))
		d1.update({sub:values})
	d.update({roll:d1})
	s=sum(d1.values())
	ss.update({roll:s})
	avg.update({roll:s/5})
	per.update({roll:(s/500)*100})
print('dictonary =',d)
print('sum =',ss)
print('average =',avg)
print('percentage =',per)