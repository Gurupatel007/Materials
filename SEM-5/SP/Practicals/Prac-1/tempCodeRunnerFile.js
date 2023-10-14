const products = [{
    name: "Pen",
    inventory: 10,
    unit_price: 5
},
{
    name: "Pencil",
    inventory: 5, unit_price:
        5
}, {
    name: "Marker",
    inventory: 10,
    unit_price: 5
}
];
function listProduct(products) {
    products.forEach(element => {
        console.log('Product: ' + element.name);
    });
}
listProduct(products);
function totalValue(products) {
    var total = 0;
    products.forEach(element => {
        total +=
        element.inventory * element.unit_price;
    });
    console.log("Total value: " + total);
}
totalValue(products);