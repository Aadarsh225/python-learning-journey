mylst = [1,2,3,4,5]
print(mylst)
print(mylst[0]) 
print(mylst[1])
print(mylst[2])
mylst[0] = 10
print(mylst)
mylst.append(6)
print(mylst)
mylst.insert(0, 100)
print(mylst)
mylst.extend([7,8,9])
print(mylst)
mylst.remove(100)
print(mylst)


for i in mylst:
    print(i)

for i in range(len(mylst)):
    print(mylst[i])

print(len(mylst))

mylst.pop()
print(mylst)

mylst.sort()
print(mylst)

mylst.reverse()
print(mylst)

print(mylst[1:4])

print(3 in mylst)

square = [x**2 for x in range(10)]
print(square)

square1 = [x**2 for x in mylst]
print(square1)