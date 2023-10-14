//console.log(process.arch);
//console.log(process.argv);
//console.log(process.env);
//console.log(process.pid)
//console.log(process.platform);


//process.stdin.on("data",data=>{
//    data = data.toString().toUpperCase()
//    process.stdout.write(data+'\n')
//})


//  Methods/functions
//console.log(process.cwd());
//console.log(process.hrtime());
//console.log(process.memoryUsage());
//console.log(process.kill(process.pid,'SIGINT'))
//console.log(process.uptime());
//process.exit();


//example
//const displayInfo=()=>{
//    console.log("hey there");
//}
//process.on('SIGHUP',displayInfo);
//setTimeout(()=>{
//    console.log('interval');
//    process.exit(0);
//},100);
//
//process.kill(process.pid,'SIGHUP')

const displayInfo = () => {
    console.log('Acknowledged SIGHUP signal in nodeJS.');
}

// Initiating a process
process.on('SIGINT', displayInfo);

setTimeout(() => {
    console.log('Exiting.');
    process.exit(0);
    }, 100);

// kill the process with pid and signal = 'SIGHUP'     
process.kill(process.pid, 'SIGINT');

