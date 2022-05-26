# create a function of sum of digit
def su_m(a):
	s=0
	while a:
		rem=a%10
		s=s+rem
		a=a//10
	print('sum of digit =',s)


# create a function to find reverse of no
def rev(b):
	s=0
	while b:
		rem=b%10
		s=s*10+rem
		b=b//10
	print('rev =',s)


# create a function of palindrome
def pal(b):
	s=0
	a=b
	while b:
		rem=b%10
		s=s*10+rem
		b=b//10
	if a==s:
		print('palindrome')
	else:
		print('not palindrome')


# create a function of armstrong no
def arm(c):
	v=str(c)
	n=c
	m=c
	l=0
	while m:
		m=m//10
		l=l+1 
	s=0
	while c:
		rem=c%10
		s=s+(rem**l)
		c=c//10
	if s==n:
		print('armstrong no.')
	else:
		print('not armstrong')


# create a function digit is perfect no. or not
def per(d):
	s=0
	n=d
	i=1
	while i<d:
		if d%i==0:
			s=s+i
		i=i+1
	if n==s:
		print('perfect no.')
	else:
		print('not perfect no.')


# create a function to check digit is strong no. or not
def strong(e):
	s=0
	v=e
	while e:
		r=e%10
		i=1
		f=1
		while i<=r:
			f=f*i
			i=i+1
		s=s+f
		e=e//10
	if s== v:
		print('strong')
	else:
		print('not strong')
	


# create a function to check calue is neon or not
def neon(f):
	s=f**2
	c=0
	while s:
		rem=s%10
		c=c+rem
		s=s//10
	if c==f:
		print('neon')
	else:
		print('not neon')

def prime(g):
	i=1
	c=0
	while i<=g:
		if g%i==0:
			c=c+1
		i=i+1
	if c==2:
		print('prime')
	else:
		print('not prime')


# create a function to check inputted no. is magic no. or not
def magic(h):
	s=0
	while h:
		rem=h%10
		s=s+rem
		h=h//10
	c=0
	while s:
		r=s%10
		c=c+r
		s=s//10
	v=0
	while c:
		re=c%10
		v=v+re
		c=c//10
	if v==1:
		print('magic no.')
	else:
		print('not magic no.')




# create a function to check input no. is weird or not
def weird(i):
	if i&1:	
		print('weird')
	elif (i>1 and i<6) or i>20:
		print('not weird')
	elif i>6 and i<21:
		print('weird')

n=int(input())
su_m(n)
rev(n)
pal(n)
arm(n)
per(n) 
strong(n)
neon(n)
prime(n)
magic(n)
weird(n)
