for i in range(5):
    print("Hello, World!")

for i in range(1, 11):
    print(i)
    if i ==4:
        break

for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
    if i == 6:
        continue
count=0
while count < 5:
    print("This will run 5 times!")
    count +=1

lst = [1,2,3,4,5]
for i in lst:
    print(i)

dict = {"name": "Alice", "age": 30, "city": "New York"}
for key,value in dict.items():
    print(f"{key}: {value}")

fruit ={"apple", "banana", "cherry"}
for f in fruit:
    print(f)

tuple1 = (1, 2, 3, 4, 5)
for t in tuple1:
    print(t)


