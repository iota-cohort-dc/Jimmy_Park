var mylib = require('./mathlib');     //notice the extra invocation parentheses!
var math = new mylib();

a = 1;
b = 35;

console.log("\n Sum of " + a + "and " + b + "is ", math.add(a,b));
console.log("hello");
console.log(math.add(5,10));

// =============================================================================

var mylib = require('./mathlib')();     //notice the extra invocation parentheses!
console.log(mylib.add(5,10));
console.log(mylib.add(12,10));
console.log(mylib.multiply(15,20));
console.log(mylib.multiply(12,12));
console.log(mylib.square(12));
console.log(mylib.square(10));
console.log(mylib.random(1,20));
console.log(mylib.random(40,50));
console.log(mylib.random(1,10));
