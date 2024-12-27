// mongo-init.js
// Initialize qmeter database
db = db.getSiblingDB('qmeter');
db.createUser({
    user: 'qmeteruser',
    pwd: 'qmeterpassword',
    roles: [{ role: 'readWrite', db: 'qmeter' }]
});

// Create user collection in qmeter
db.createCollection('user');

// // Initialize qmeter1 database
// db = db.getSiblingDB('qmeter1');
// db.createUser({
//     user: 'qmeter1user',
//     pwd: 'qmeter1password',
//     roles: [{ role: 'readWrite', db: 'qmeter1' }]
// });

// // Create user collection in qmeter1
// db.createCollection('user');

// The data import will be handled by mongoimport in the docker-compose file