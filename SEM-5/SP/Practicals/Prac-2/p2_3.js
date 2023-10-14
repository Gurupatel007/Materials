// /*
// Write a Node.js program to create an object named book using object 
// literal syntax. Add book_title, author and publish_year as properties to 
// the book object and assign it’s appropriate values. Now create function 
// print_info() to print the book object to the console so the final output 
// looks as below:
// title: Harry Potter and the Sorcerer's Stone
// author: J.K. Rowling
// publish_year: 1997
// */
// const prompt = require('prompt-sync')({sigint: true});
// var title,author,year;
// function takeinput(){
//     title = prompt("Enter the title of the book: ")
//     author = prompt('Enter the author name: ')
//     year = prompt('Enter the year of publishing: ')

// }
// takeinput();
// book={
//     book_title: title,
//     book_author:author,
//     publish_year:year
// }

// // console.log(book)
// function printoutput(){
//     console.log("\ntitle: "+book.book_title)
//     console.log('author: '+book.book_author)
//     console.log('publish_year: '+book.publish_year)
// }
// printoutput()

const book = {
    book_title: "Harry Potter and the Sorcerer's Stone",
    author: "J.K. Rowling",
    publish_year: 1997
}
function print_info() {
    console.log("title: " + `${book.book_title}`)
    console.log("author: " + `${book.author}`)
    console.log("publish_year: " + `${book.publish_year}`)
}
print_info()


