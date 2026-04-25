use("practiceDB");

// Delete a single document
// db.users.deleteOne({ name: "Alice" });

// Delete multiple documents
 db.users.deleteMany({ age: { $gt: 30 } });

// Delete with logical operator
 db.users.deleteMany({ $or: [ { name: "Bob" }, { name: "Charlie" } ] });