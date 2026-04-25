use("practiceDB");

db.users.insertOne({
    name: "John Tony",
    email: "john.tony@example.com",
    age: 30,
    isActive: true
})

db.users.insertMany([
    {
        name: "Alice",
        email: "alice@example.com",
        age: 25,
        isActive: true
    },
    {
        name: "Bob",
        email: "bob@example.com",
        age: 35,
        isActive: false
    },
    {
        name: "Charlie",
        email: "charlie@example.com",
        age: 28,
        isActive: true
    }

])

