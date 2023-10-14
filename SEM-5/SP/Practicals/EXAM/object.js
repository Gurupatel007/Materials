//using object function
/*
var myCar = new Object();
myCar.brand = "hyundai";
myCar.model = "i-10";
myCar.color = "Black";

console.log(myCar)
*/

//using Lieral notation
/*
var myCar  = {
    brand:"Nexa",
    model:'Xl-6',
    color:'blue'
}
console.log(myCar);
*/

//using object Constructor
function emp(id,name,salary){
    this.id = id;
    this.name = name;
    this.salary = salary;
}
var e = new emp(74,'jay',50000);
console.log(e);