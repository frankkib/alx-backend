import redis from 'redis';

const client = redis.createClient();

client.on('connect' , () => {
	console.log('Redis client connected to the sever');
});

client.on('error', (error) => {
	console.error(`Redis client not connected to the server: ${error.message}`);
});
