`Write a Node.js program to take a list of number from command line arguments and print all the
numbers in ascending order without using any in-built function.
For example: >> node example1.js 1 5 7 2 9 0
 Number in ascending order: 0,1,2,3,5,7,9
`
// Code:
const args = process.argv.slice(2);
console.log(args);
let arr = [];
for (let i = 0; i < args.length; i++) {
    arr.push(parseInt(args[i]));
}
for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
        if (arr[j] < arr[i]) {
            let temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }
    }
}
console.log(arr);
