car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(car) #before the change
print(x)

car["color"] = "red"

print(car) #after the change
print(x)






y = thisdict.items()
print(y)





car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change









for x, y in thisdict.items():
  print(x, y)  #most hightech










#copy dictonary other method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)








# from keys function

x = ('key1', 'key2', 'key3')
y = 0,1,2,3

thisdict = dict.fromkeys(x, y)

print(thisdict)






x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict) # in value get none






# setdefault =  agar koi key phle se hai to set default koi change nhi krta hai h agar nhi hai to set default add kr deta hai usme