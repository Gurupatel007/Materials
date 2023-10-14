// Create Node.js application which allow users to perform basic mathematical operations such as addition, subtraction, multiplication, and division?
var a=process.argv
var b1=a[2]
var b=parseInt(a[2]);
var c1=a[3];
var c=parseInt(a[3]);
var d=a[4];

switch (d) {
    case '+':
        if (typeof(b)=="number" && typeof(c)=="number") {
            console.log("Addition: "+(b+c));
        }
        else {
            console.log("Enter valid Number.");
        }
        break;

    case '-':
        if (typeof(b)=="number" && typeof(c)=="number") {
            console.log("subtraction: "+(b-c));
        }
        else {
            console.error("Enter valid Number.");
        }
        break;

    case '*':
        if (typeof(b)=="number" && typeof(c)=="number") {
            console.log("Multiplication: "+(b*c));
        }
        else {
            console.error("Enter valid Number.");
        }
        break;

    case '/':
        if (typeof(b)=="number" && typeof(c)=="number") {
            console.log("Division: "+(b/c));
        }
        else {
            console.error("Enter valid Number.");
        }
        break;

    default:
        console.log("Enter valid Input.")
}
