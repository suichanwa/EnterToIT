const EventEmiiter = require('events');

class Logger extends EventEmiiter {
    log(message) {
        this.emit('message', `${message} ${Date.now()}`);
    }
}

const log = new Logger();

log.on('message', data => {
    console.log(data);
});

log.log('Hello World!');