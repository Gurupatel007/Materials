//var arr1 = new Array();
//Operations/ methods & properties
/*
arr1.push(2); //insets elemnt to last index
console.log(arr1);
arr1.unshift(40);// inserts elemnt to first index
console.log(arr1);
console.log(arr1.indexOf(2)); //returns the index of given elemnt
console.log(arr1.length);
arr1.splice(1,0,20);//(start index,no of elements,value) inserts number 20 at index 1 by deleting o elements
console.log(arr1);
arr1.splice(1,2,3);//replaces two elements 20 nd 2 by 3 
console.log(arr1);
*/

//array traversal through command line input
/*
process.argv.forEach((val,index)=>{
    console.log(`${index}:${val}`);
});
*/

var arr2 = [10,20,30,40,51];
arr2.forEach(ele=>{
    console.log(ele);
})
