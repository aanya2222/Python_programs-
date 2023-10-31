str1='neeta'
print(str1)

#accessing particular index
print(str1[1])

#string slicing
print(str1[1:4])

#printing another string
str2='dypcet'
print(str2)

#combining 2 string
str3=str1+str2
print(str3)

#printing string multiple times
str4 = str1 * 2
print(str4)

#string reverse
print(str1[::-1])

#char updation
str5 = 'chetana'
list1 = list(str5)
list1[2] = 'a'
str5 = ''.join(list1)
print(str5)

#delete entire string
str6 = 'sakshi'
print(str6)
del str6


#to delete char
str7 = 'shivendra'
print(str7)
str8 = str7[0:4]
print(str8)

#to escape seq
str9 = "Hello\ 'how are you'"
print(str9)

#formatting
str10 = "{} {} {}".format('Hello','Hi','WEelcome')
print(str10)

#positioning order
str11 = "{1} {2} {0}".format('Hello','Hi','WEelcome')
print(str11)

#keyword order
str12 = "{l} {f} {g}".format(g='Hello',f='Hi',l='WEelcome')
print(str12)

#alignment text
str13 = "{:<20} {:^20} {:>20}".format('Hello','Hi','WEelcome')
print(str13)