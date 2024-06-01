name=  ['apple', 'oranges', 'mango']
price = [200, 150, 500]
fruits = dict(zip(name, price))
print(fruits)
print(fruits.get('mango'))
print(fruits.get('banana', 60))

fruits['apple'] = {'small': 180, 'large': 270}
print(fruits) 
print(fruits.get('apple'), 225)
print(fruits)
new = {12:454, 78:'dksjf54'}
fruits.update(new)
print(fruits)
print('------------------------')
for i in fruits:
    print(fruits[i])


d = {'s': 3, 'r': 5}
print(d)