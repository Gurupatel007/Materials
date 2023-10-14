const readline = require('readline')
const a1 = readline.createInterface(process.stdin, process.stdout)
a1.question('Enter your Name : ', (name) => {
  a1.question('Enter mobile number : ', (num) => {
    if (num.length == 10) {
      console.log(`Your Name is : ${name}`)
      console.log(`Your Mobile Number is : ${num}`)
    } else {
      console.log(`Enter a valid mobile number.`);
    }
  })
})