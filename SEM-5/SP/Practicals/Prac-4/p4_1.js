fs= require('fs');
var a=[];
fs.readFile('que-1.txt',function(error,data){
    console.log(data);
    a = data.toString().split(',');
    var i,sum=0,avg;
    for(i=0;i<a.length;i++){
        sum += parseInt(a[i]);
        avg=sum/parseInt(a.length);
    }
    console.log("Sum: "+sum);
    console.log("Average: "+avg);
    console.log("Maximum: "+Math.max(...a));
    console.log("Minimum: "+Math.min(...a));
})
