var fs = require('fs');
//readfile operation //data read from file

//fs.readFile('gt.txt',(err,data)=>{
//    if(err) console.error(err);
//    console.log(data.toString());
//});

//appendfile operation //simply inserts data at the end of the file.

//fs.appendFile('gt.txt','\ni am from Modasa',(err)=>{
//    if(err) throw err;
//    console.log('saved');
//});

//writeFile operation //it simply replaces all the content with the passed content.

//fs.writeFile('gt.txt','Btech',(err)=>{
//    if(err) throw err;
//    console.log('inserted');
//});


//renaming file
//fs.rename('gt.txt','g_t.txt',(err)=>{
//    if(err) throw err;
//    console.log('renamed');
//});

//delete file operation

fs.unlink('g_t.txt',(err)=>{
    if(err) throw err;
    console.log('deleted');
});