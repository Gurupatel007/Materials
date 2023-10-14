//OBJECTS LITERALS PROPERTIES
var ob1 ={};
ob1.bar=123;
console.log(ob1);

//LITERALS NESTING
/*var ob2={
    name:"guru",
}
console.log(ob2)*/

// function
/*function add(a,b){
    console.log(a+b);
}
add(1,30);
add(4,5);*/

// immediately function
/*(function(){
    console.log("hello there");
}
)();*/

// anonymous function
/*var func = function (){
    console.log("Anonymous function");
}
func();*/

// setTimeout function
setTimeout(function (){
    console.log("hii");
},2000)

function foo(){
    console.log("Hii there!");
}
setTimeout(foo,5000);