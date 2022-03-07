# ek adami ke pass kuch apple hai usko 7-7 ke set is prakar se banane hai ki agar 7-7 ke set ho to koi apple na bache agar 6-6 , 5-5, 4-4, 3-3, 2-2 ke set ho to ek apple bache

a=int(input('enter the no. of apples'))
if a%7==0 and a%6==1 and a%5==1 and a%4==1 and a%3==1 and a%2==1:
	print('yes')
else:
	print('no')
