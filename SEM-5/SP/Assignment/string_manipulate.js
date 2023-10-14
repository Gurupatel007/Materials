`Define module and its type in Node.js. Explain local module in node.js with an example. Create a
local module named string_manipulate.js that provides utility functions for manipulating strings.
Export functions to capitalize the first letter of a string and to check if a string is a palindrome. Then,
use this module in a program named app.js to demonstrate the functionality of the exported
functions.
`
// Code:
// // string_manipulate.js
module.exports = {
    capitalize: function (str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    },
    palindrome: function (str) {
        let len = str.length;
        let mid = Math.floor(len / 2);
        for (let i = 0; i < mid; i++) {
            if (str[i] !== str[len - 1 - i]) {
                return false;
            }
        }
        return true;
    }
}
