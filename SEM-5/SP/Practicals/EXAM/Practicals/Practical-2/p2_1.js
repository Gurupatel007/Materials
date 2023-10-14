var a = process.argv;
var b = a[2];
var c = parseFloat(a[3]);
var d = parseFloat(a[4]);

if(isNaN(c)||isNaN(d)) {
    console.error('Both operand should be number only');
}
else{
    switch(b){
        case '+' :
            console.log("Addition :",c+d);
            break;
        case '-':
            console.log("Subtraction :",c-d);
            break;
        case '*':
            console.log("Multiplication :",c*d);
            break;
        case '/':
            console.log("Division :",c/d);
            break;
        default:
            console.log('Please enter correct operand.');
    }
}