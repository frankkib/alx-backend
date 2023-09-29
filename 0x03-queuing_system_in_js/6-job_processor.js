const kue = require('kue');

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
	console.log(`Sennding notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message);
	done()
});

kue.app.listen(3000);
console.log('kue is running on http://localhost:3000');
