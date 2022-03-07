# standard print
a=50
b=3
value=(10,20)
data={'rahul'=:2000,'sonam':3000}
print("{:,}".format())
print("{:_}".format())
print("{:.2}".format(a/b))
print("{:.2%}".format(a/b))
print("{0[0]}   {0[1]}".format(value))
print("{0[rahul]:d}  {0[sonam]:d}".format(data))
print("{d[rahul]:d}  {d[sonam]:d}".format(d=data))
print("{rahul}  {sonam}".format(**data))

