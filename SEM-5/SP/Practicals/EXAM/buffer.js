//const buffer1 = Buffer.alloc(10);
// buffer1.write(1,2,3,4,5,6,7,8,9);
//buffer1.write("hello")
// console.log(buffer1.toString('utf-8'));
//console.log(buffer1);
var str = "it's gt";
var buff2 = Buffer.from(str,'utf-8');
console.log(buff2.toString());