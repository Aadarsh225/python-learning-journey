# mydict = [{"name":"aadarsh","age":20,"city":"birgunj"},{"name":"tony","age":30,"city":"new york"},{"name":"susan","age":25,"city":"london"}]
# print(mydict[0]["name"])
# mydict[0]["name"] = "adarsh"
# print(mydict[0]["name"])
# mydict.append({"name":"john","age":35,"city":"paris"})
# print(mydict)
# mydict.insert(1, {"name":"michael","age":40,"city":"berlin"})
# print(mydict)
# mydict.extend([{"name":"emily","age":28,"city":"rome"},{"name":"david","age":32,"city":"madrid"}])
# print(mydict)
# mydict.remove({"name":"michael","age":40,"city":"berlin"})
# print(mydict)
# for i in mydict:
#     print(i)

# for i in range(len(mydict)):
#     print(mydict[i])

# print(len(mydict))
# mydict.pop()
# print(mydict)
# mydict.sort(key=lambda x: x["age"])
# print(mydict)


user = {"name":"aadarsh","age":20,"city":"birgunj"}
print(user["name"])

user["age"] = 21
print(user["age"])
user["country"] = "nepal"
print(user)

print(user.get("name"))


for key,value in user.items():
    print(key,value)

print(user.keys())
print(user.values())
print(user.items())


user["city"] = "Kathmandu"
del user["age"]
print(user)




