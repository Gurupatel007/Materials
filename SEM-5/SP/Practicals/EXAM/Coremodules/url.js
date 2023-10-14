var http = require('http');
var url = require('url');
http.createServer((req,res)=>{
    var querystring = url.parse(req.url,true);
    console.log(url.parse('https://www.ganpatuniversity.ac.in:25/video?num1=10 & num2=30'));
//    console.log(querystring.href);//returns complete url string
//    querystring.href = "https://google.com/ganpatuniversity.ac.in"
//    console.log(querystring.href);
    
    /* host and hostname =>host contains port number
    const querystring1 = new URL('https://www.google.com:25/uvpce');
    console.log(querystring1.host);
    console.log(querystring1.hostname);
    */
    
    //pathname and searchparam
//    const querystring2 = new URL('https://www.google.com/test/test1/test2/test3?username=bhavin');
//    console.log(querystring2.pathname);
//    console.log(querystring2.searchParams);
    
    
//    
    console.log(querystring);
    
}).listen(1074);

//shortcut => HHHHPPPPSS(.href,.host,.hostname,.hash,.path,.pathname,.port,.protocol,.search,.searchParams)