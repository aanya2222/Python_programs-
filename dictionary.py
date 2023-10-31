d1 = {1:"Hello", 2:"Hi", 'a':"Welcome"}

#to print keys
print(d1.keys())

#to print values
print(d1.values())

#to print keys & items
print(d1.items())

#to create copy of dictionary
newd = d1.copy()
print(newd)

#to remove specific element
print(d1.pop(1))
print(d1)
print(d1.pop(2))
print(d1)

#to remove last element
print(d1.popitem())
print(d1)



d2 = {4:"Welcome"}

#to add data
d1.update(d2)
print(d1)

d1.update([(5,"hii")])
print(d1)
#clear the dictionary
d1.clear()
print(d1)


d3 = {'a', 'b', 'c'}

d4 = dict.fromkeys(d3,1)
print(d4)