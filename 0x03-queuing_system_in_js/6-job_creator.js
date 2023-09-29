const kue = require('kue');
const queue = kue.createQueue();


const jobData = {
	phoneNumber: '',
	message:''
};
const job = queue.create('push_notification_code', jobData);

job.on ('complete', () => {
	console.log('Notification job completed');
});

job.on('failed', () => {
	console.log('Notification job failed');
});

job.save((err) => {
	if (!err) {
		console.log(`Notification job created: ${job.id})`);
	} else {
		console.error(`Error creating notification job ${err}`);
	}
});

kue.app.listen(3000);
console.log('Kue is running on localhost');
