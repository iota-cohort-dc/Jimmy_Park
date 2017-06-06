function Ninja(name, age, prevOccupation) {
  // PRIVATE
  var privateVar = "This is a private variable";
  var privateMethod = function() {
    console.log("this is a private method");
  }
  // PUBLIC
  this.name = name;
  this.age = age;
  this.prevOccupation = prevOccupation;
  this.introduce = function() {
    console.log("Hi my name is " + this.name + ". I used to be a " + this.prevOccupation + " and now I'm a Ninja!");
    privateMethod(); // this works since it is a scope that can access privateMethod!
    console.log(privateVar);      // this works too!
  }
}

var Pariece = new Ninja("Pariece", 24, "TFA Teacher");
// try this:
Pariece.privateMethod();
// or this:
privateMethod();
// or this:
Pariece.privateVar;
// none of these work. Think about the scope of each.

function User(name, ssn){
  var social = ssn;
  this.name = name;
}
var mike = new User('Mike', 274164398);

function User(name, ssn){
  var social = ssn;
  this.name = name;
  // Adds a so-called 'getter' function to allow reading private variables
  this.getSSN = function(){
    return social;
  }
}
var mike = new User('Mike', 274164398);
console.log(mike.getSSN()); // 274164398
