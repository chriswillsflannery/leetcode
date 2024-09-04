cat = {'name': 'whiskers', 'age': 2, 'color': 'black'}
cat.values()

print(cat.values())
cat.keys()
cat.items()

for k, v in cat.items():
    print("this cat's %s is %s" % (k, v))

'name' in cat.keys() # True
'sugar' not in cat.values() # True

# use get with a fallback value in case value doesn't exist
print("What kind of %s does the cat have?" % (cat.get('name2', 'othername')))

message = 'Hey there'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)