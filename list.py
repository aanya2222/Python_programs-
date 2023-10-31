l1= [1,2,"Hello",3.4]
print(type(l1))

print(l1[0:])
print(l1[ : ])
print(l1[2:4])
print(l1[ :4])
print(l1[1:4:2])
print(l1[-1])
print(l1[-3:-1])

l1[2]=10
print(l1)
l1[3:4]=[89,36]
print(l1)

#repetiton
l2=l1*2
print(l2)

#concatenation
l3 = l1 + l2
print(l3)

#membership
print(1 in l1)

#adding element in list
l4=[]
n=int(input("Enter no. of elements"))

for i in range(0,n):
    l4.append(input("ENter elements"))
    
for i in l4:
    print(i,end=' ')

#to remove
l5=[1,2,3,4]
l5.remove(2)
print("\n",l5)

#printing length
print(len(l5))

#printing min element
print(min(l5))

#printing max element
print(max(l5))