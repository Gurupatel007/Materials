var events = require('events');
var eventsEmitter = new events.EventEmitter();
eventsEmitter.on('myevent', (msg) => console.log(msg)); //fired an event
eventsEmitter.emit('myevent','Event-1');
eventsEmitter.emit('myevent','Event-2');

eventsEmitter.removeListener(events.EventsEmitter,()=>{
    console.log('removed');
})
eventsEmitter.emit('myevent','Event-1');
// removeAllListeners(['myevent'])
