use("practiceDB");

// // Update a single document
// db.users.updateOne(
//   { name: "Alice" }, // Filter
//   { $set: { age: 30 } } // Update operation
// );

// // Update multiple documents
// db.users.updateMany(
//   { age: { $gt: 25 } }, // Filter
//   { $set: { isActive: true } } // Update operation
// );

// // Upsert: Update if exists, insert if not
// db.users.updateOne(
//    { name: "Bob"},
//    { 
//      $set: { 
//        age: 28,
//        isActive: false,
//        message: "Hi I am Bob"
//      }
//    }
// );

// update with two conditions

// db.users.updateOne(
//     { name: "Charlie", age: { $gt: 20 } }, // Filter with two conditions
//     { $set: { isActive: true } } // Update operation
// );

// // update with logical operator
// db.users.updateMany(
//     { $or: [ { name: "Alice" }, { name: "Bob" } ] }, // Filter with logical operator
//     { $set: { isActive: false } } // Update operation
// );

// and 
// db.users.updateMany(
//     { $and: [ { age: { $gt: 25 } }, { isActive: true } ] }, // Filter with logical operator
//     { $set: { isActive: false } } // Update operation
// );

db.users.updateOne(
    { name: "David"},
    { $inc: { age: 1 } } // Increment age by 1
)

db.users.updateOne(
    { name: "Charlie"},
    { $inc: { age: -1 } } // Decrement age by 1
)

