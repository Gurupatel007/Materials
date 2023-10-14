const r = require('readline');
const r1 = r.createInterface({
    input:process.stdin,
    output:process.stdout
})
var arr = [];
r1.question('what\'s your name?',(name)=>{
    r1.question('what is your phone number?',(phone)=>{
        if(phone.length==10) {
            arr.push(name,phone);
            console.log(arr);
        }
        else{
            console.error('\nNumber should be of 10-digits only')
        }
        r1.close();
    })
})