tuples = (1, 2, 3, 4, 5)
print(tuples)
print(tuples[0])
print(tuples[1])
print(tuples[2])

# tuples[0] = 10 # This will raise an error because tuples are immutable
# print(tuples)
# tuples.append(6) # This will raise an error because tuples do not have an append method
# print(tuples)
# tuples.insert(0, 100) # This will raise an error because tuples do not have an insert method

for i in tuples:
    print(i)
for i in range(len(tuples)):
    print(tuples[i])
print(len(tuples))
