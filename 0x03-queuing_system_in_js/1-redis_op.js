import redis from 'redis';

const client = redis.createClient();

client.on('connect' , () => {
	console.log('Redis client connected to the sever');
});

client.on('error', (error) => {
	console.error(`Redis client not connected to the server: ${error.message}`);
});


function setNewSchool(schoolName, value) {
	client.set(schoolName, value, (err, reply) => {
		if (err) {
			console.error(`Error setting value for key${schoolName}: ${err.message}`);
		} else {
			console.log(`Value set for key ${schoolName}`);
			console.log(reply);
		}
	});
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, value) => {
		if (err) {
			console.error(`Error getting value for key ${schoolName}: ${err.message}`);
		} else if (value == null) {
			console.log(`Key ${schoolName} does not exist in redis.`);
		} else {
			console.log(`Value for key ${schoolName}: ${value}`);
		}
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
