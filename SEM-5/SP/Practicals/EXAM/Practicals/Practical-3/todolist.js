var arr = new Array();
var top=-1;
var todo = {
    add:(t1)=>{
        arr.push(t1);
    },
    remove:(t2)=>{
        arr.splice(indexOf(t2),1,0)
    },
    listing:(t3)=>{
        return arr;
    }
}
module.exports = todo;