// Reading from the data base

use("practiceDB");

// // find() method is used to read the data from the collection. It returns a cursor to the documents that match the query criteria.

// // To read all the documents from the collection, we can use an empty query object.
// db.users.find({})

// // To read specific fields from the documents, we can use the projection parameter. The projection parameter is an object that specifies the fields to include or exclude in the result set.
// db.users.find({}, { name: 1, age: 1 })

// To read documents that match specific criteria, we can use a query object. The query object is an object that specifies the criteria for selecting documents.
// db.users.find({ age: { $gt: 25 } })

// // To read a single document that matches specific criteria, we can use the findOne() method. The findOne() method returns the first document that matches the query criteria.
// db.users.findOne({ name: "John Tony" })

// db.users.findOne({ name: "John Tony" }, { name: 1, age: 1 })


// db.users.find({ age: { $gt:25}}, {isActive: true})

// Logical operators 

//  db.users.find({ $or: [{ age: { $gt: 25 } }, { isActive: true }] })

// db.users.find({ $and: [{ age: { $gt: 25 } }, { isActive: true }] })

db.users.find().sort({ age: 1 }) // Sort by age in ascending 

db.users.find().limit(2)