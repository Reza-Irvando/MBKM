db.users.insertOne(
    {
        name: "sue",
        age: 26,
        status: "pending"
    }
)

db.users.updateMany(
    { age: {$lt : 18 } },
    { $set : {status: "reject"}}
)

db.users.deleteOne(
    {status: "pending"}
)
