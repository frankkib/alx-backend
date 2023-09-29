import redis from 'redis';

const client = redis.createClient();

client.on('connect' , () => {
	console.log('Redis client connected to the sever');
});

client.on('error', (error) => {
	console.error(`Redis client not connected to the server: ${error.message}`);
});

function createAndDisplayHash() {
	client.hset(
		'HolbertonSchools',
		'portland',
		50,
		redis.print
	);
	client.hset(
		'HolbertonSchools',
		'seattle',
		80,
		redis.print
	);
	client.hset(
		'HolbertonSchools',
		'New York',
		20,
		redis.print
	);
	client.hset(
		'HolbertonSchools',
		'Bogota',
		20,
		redis.print
	);
	client.hset(
		'HolbertonSchools',
		'Cali',
		40,
		redis.print
	);
	client.hset(
		'HolbertonSchools',
		'Paris',
		2,
		redis.print
	);

	client.hgetall('HolbertonSchools', (err, hash) => {
		if (err) {
			console.error(`Error getting hash: ${err.message}`);
		} else {
			console.log('Hash stored in Redis:');
			console.log(hash);
		}
		client.quit();
	});
}
createAndDisplayHash();
