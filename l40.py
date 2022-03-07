# palindrome or not



n=int(input('enter the no.'))
s=0
b=n
while n:
	rem=n%10
	s=s*10+rem
	n=n//10
	
if s==b:
	print("palindrome")
else:
	print("not palindrom")	
