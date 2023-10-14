/* types of functions
1)Simple Function
2)Anonymous function =>{
    (a) assignment variable
    (b) callback function
    (c) immdeiate invoke function
}
3)Arrow Function


//simple function
/*
function add(num1,num2){
    console.log(num1+num2);
}
add(3,99);
*/

//Anonymous function
/*
var show = function (){
    console.log('Anonymous function');
}
show();
*/

//call back function
/*
setTimeout(function (){
    console.log('executed after 1 second')
},1000);
*/

//immediate function
(function (){
    console.log('iynyk');
})();

//arrow function
var add = function (a,b){
    return a+b;
};
var add1 =(a,b,c)=>a+b+c;

console.log(add(10,20),add1(10,20,30));
