import re
pattern="\S"
string="hello 12 hi 89.Howdy"
output=re.findall(pattern,string,2)
print(output)
