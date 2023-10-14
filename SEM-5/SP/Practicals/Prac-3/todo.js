var arr = new Array();
var todo = {
    add:(t1)=>{
        arr.push(t1);
    },
    remove:(t2)=>{
        var index = t2-1;
        if(index>=0 && index<=t2)
        arr.splice(index,1);
    },
    listing:(t3)=>{
        return arr;
    }
}
module.exports = todo;