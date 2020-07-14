# zip, 'packing'
a = [1, 'a', {1: '9'}, False, [1, 'a']]
b = [True, 1, 2, 'string']
z = zip(a, b)

# 'unzip', unpacking
z = [(1,2), (False, {'a': 20}), ('string', 2)]
a, b = zip(*z)
print(a)
print(b)

a = [True, 1, 2, 'string']
# enumerate
for item in enumerate(a):
    print(item)

