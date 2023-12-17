import re
file_path = 'Task Regular Expressions.txt'

with open(file_path, 'r') as file:
    file_contents = file.read()

pattern = re.compile( r'(\s?[a-zA-Z]+\s[a-zA-Z]+)\s?')
matches = pattern.finditer(file_contents)
names = []
for match in matches:
    names.append(file_contents[match.span()[0] : match.span()[1]])
                   
print(names)        

pattern = re.compile(r"[a-zA-Z0-9_+.]+@[a-zA-Z0-9_+.]+\.\w{3}")
matches = pattern.finditer(file_contents)
mails =[]
for match in matches:
    mails.append(file_contents[match.span()[0]   : match.span()[1]])
print(mails)

pattern = re.compile(r"01\d+")
matches = pattern.finditer(file_contents)
numbers=[ ]
for match in matches:
    numbers.append(file_contents[match.span()[0]   : match.span()[1]])

                   
print(numbers)                   
                   