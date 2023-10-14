const readline = require('readline')
const r1 = readline.createInterface({
    input:process.stdin,
    output: process.stdout
});

r1.question('Enter the book title?',(title)=>{
    r1.question('Enter the Author name?',(aname)=>{
        r1.question('Enter the publish year?',(year)=>{
            const book = createBook(title,aname,year);
            printInfo(book);
            r1.close();
        });
    });
});
function createBook(title,aname,year){
    return {
        book_title:title,
        author:aname,
        publish_year:year
    };
}
function printInfo(book){
    console.log('title :',book.book_title);
    console.log('author :',book.author);
    console.log('publish_year :',book.publish_year);
}