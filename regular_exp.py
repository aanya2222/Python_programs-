import re 
s = "This is a python program portal"
match = re.search('portal', s)
print("Start Index:",match.start())
print("End Index:",match.end())
print(match)

print("\nFinding Numbers From String")
string = "A Hello my no. is 123456789 & another 987654321"
regex = '\d+'
match = re.findall(regex,string)
print(match)

print("\nFinding Matching Pattern From String")
string = "Hello my no. is 123456789 & another 987654321"
regex = r'H..l'
match = re.findall(regex, string)
print(match)

print("\nFinding Matching Pattern From String")
string = "Hello my no. is 123456789 & another 987654321"
regex = r'Hello$'
match = re.findall(regex, string)
print(match)

print("\"Hello\"")