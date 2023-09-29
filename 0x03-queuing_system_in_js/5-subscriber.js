import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect' , () => {
	console.log('Redis client connected to the sever');
});

subscriber.on('error', (error) => {
	console.error(`Redis client not connected to the server: ${error.message}`);
});

subscriber.subscribe('holbertone school channel');

subscriber.on('message', (channel, message) => {
	console.log(`Message recieved on channel "${channel}": ${message}`);
	if (message === 'KILL_SERVER') {
		subsrcibe.unsubscribe('holberton school channel');
		subscriber.quit();
	}
});
