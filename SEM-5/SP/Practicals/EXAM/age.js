//wanp to check eligibilty of any user via command line arguments for voting.
var age = process.argv;
age = parseInt(age[2]);
if(age>=18) console.log("eligible");
else console.log("not eligible");
