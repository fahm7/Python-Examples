population={ 2, 3, 5, 1, 11, 10,}


print("_____________________ADD__________________________________")
countries={'china','india', 'usa','canada'}
countries.add('london')
print("Countries after adding london",countries)

countries.add('india')
countries.add('germany')
countries.add('france')
countries.add('spain')

print("Countries after  adding india",countries)


print("______________________FROZEN SET__________________________________")

mylist=['a','e','i','0','u']
print(mylist)
mylist=frozenset(mylist)
print("mylist after frozen: \n",mylist)

population= frozenset(population)
print("population set after frozen\n",population)
#population.add(50)

print("___________________DISCARD_________________________________")

print(countries)
countries.discard('china')
print("After discard china 1")
print(countries)
print("After discard china 2")
countries.discard('china')
print(countries)


print("___________________REMOVE___________________________________")
print(countries)
countries.remove('spain')
print("After remove spain 1")
print(countries)
print("After remove spain 2")
#countries.remove('spain')
print(countries)

print("___________________COPY__________________________________")

countries_backup=countries.copy()
print("Countries Set :        ",countries)
print("Countries BACKUP Set : ",countries_backup)
print("___________________CLEAR__________________________________")
countries.clear()

print("countries = ",countries)

print("___________________DIFFERENCE__________________________________")

x_set = {"a","b","c","d","e"}
y_set = {"b","c"}
z_set = {"c","d"}

print(x_set-y_set)
print(x_set.difference(y_set))
print("___________________INTERSECTION__________________________________")

print(x_set.intersection(y_set))
print(x_set & y_set)

print()

print("___________________UNION__________________________________")

x_set = {"a","b","c","d","e"}
y_set = {"b","c","m"}

print(x_set|y_set)
print(x_set.union(y_set))

print("___________________SUBSET__________________________________")

x_set = {"a","b","c","d","e"}
y_set = {"b","c",}

print(x_set.issubset(y_set))
print(x_set<=y_set)

print("___________________SUPERSET__________________________________")


x_set = {"a","b","c","d","e"}
y_set = {"b","c",}

print(x_set.issuperset(y_set))
print(x_set<=y_set)

print("___________________SUBSET__________________________________")
