var products = [
    {
        name:'tablet',
        inventory:'10',
        unit_price:'20000'
    },
    {
        name:'mobile',
        inventory:'5',
        unit_price:'35000'
    },
    {
        name:'Laptop',
        inventory:'2',
        unit_price:'65000'
    }
]
function listproducts(products){
    products.forEach(currentItem => {
        console.log(currentItem.name);
    });
}
listproducts(products);
var total=0;
function totalvalue(products){
    products.forEach(currentItem => {
        total+= currentItem.inventory * currentItem.unit_price;
    });
    return total;
}
var total = totalvalue(products)
console.log(total);