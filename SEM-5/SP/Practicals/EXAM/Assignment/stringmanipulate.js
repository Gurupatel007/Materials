var manipulate = {
    capitalize:(str)=>{
        return str.charAt(0).toUpperCase()+str.slice(1);
    },
    palindrome:(str)=>{
        var str1 = str.split('').reverse().join('');
        return str1==str;
    }
}
module.exports = manipulate;