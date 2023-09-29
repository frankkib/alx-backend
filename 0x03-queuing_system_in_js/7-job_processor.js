const kue = require('kue');

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
	if (blacklistedNumbers.includes(phoneNumber)) {
		const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
		return done(new Error(errorMessage));
	}
	job.progress(0, 100);
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

	job.progress(50, 100);
	setTimeout(() => {
		done();
	}, 1000);
}


queue.process('push_notification_code_2', 2, (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message, job, done);
});


kue.app.listen(3000);
console.log('Kue is running on http://localhost:3000');

