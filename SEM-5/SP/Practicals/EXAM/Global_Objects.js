console.log(__dirname);
console.log(__filename);

// it will print the message inside it again and again after the given time interval here 2seconds.    
setInterval(function (){
    console.log("hello users.")
},2000);
clearInterval();
setTimeout(()=>{
    console.log("hello");
},5000);
clearTimeout();