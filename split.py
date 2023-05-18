import re
pattern='\s'
string='hello 12 hi 89.Howdy'
output=re.split(pattern,string,2)
print(output)
