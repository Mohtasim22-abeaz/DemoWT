let x = {name : "rumman", age : 24, y : () => "hello " + x.name};
console.log(x.age);
console.log(x.y());
//variable (let add =) arrow{() => {return 2 + 3;};}

arrow=(a, b) => {return a + b;};
console.log(arrow(2, 3));

cars = [
    {name:"rumman", age : 24},
    "corona",
    22,
    10,
    [1, 2, 3, 4]
];
console.log(cars);
