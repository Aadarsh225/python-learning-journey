fruits = {"apple", "banana", "cherry"}
print(fruits)
print("apple" in fruits)
fruits.add("orange")
print(fruits)
fruits.remove("banana")
print(fruits)
for i in fruits:
    print(i)

fruits1 = {"grape", "melon", "kiwi"}
fruits.update(fruits1)
print(fruits)
    
a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

