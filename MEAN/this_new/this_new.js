function NinjaConstructor(name, prevOccupation) {
var ninja = {}; // <-- PAY ATTENTION TO THIS LINE!
ninja.name = name;
ninja.prevOccupation = prevOccupation;
ninja.introduce = function() {
  console.log("Hi my name is " + ninja.name + ". I used to be a " + ninja.prevOccupation + " and now I'm a Ninja!");
}
return ninja; // <-- AND THIS LINE!
}

( The two lines we are drawing your attention to are the lines where we create the object called ninja and then return the object called ninja.
this and new work in concert to eliminate those two lines!
Stepping through the process:
We can replace ninja with this. )

1. We can replace ninja with this.
var samurai = NinjaConstructor("Jimmy", "Dental Crown Design");
console.log(samurai);

function NinjaConstructor(name, prevOccupation) {
  var this = {}; // <-- PAY ATTENTION TO THIS LINE!
  this.name = name;
  this.prevOccupation = prevOccupation;
  this.introduce = function() {
    console.log("Hi my name is " + this.name + ". I used to be a " + this.prevOccupation + " and now I'm a Ninja!");
  }
  return this; // <-- AND THIS LINE!
}

2. var this = {}; and return this; can and should be removed...
function NinjaConstructor(name, prevOccupation) {
  this.name = name;
  this.prevOccupation = prevOccupation;
  this.introduce = function() {
    console.log("Hi my name is " + this.name + ". I used to be a " + this.prevOccupation + " and now I'm a Ninja!");
  }
}

3. ...because the new keyword placed before invoking the function will do that for us!
function NinjaConstructor(name, prevOccupation) {
  this.name = name;
  this.prevOccupation = prevOccupation;
  this.introduce = function() {
    console.log("Hi my name is " + this.name + ". I used to be a " + this.prevOccupation + " and now I'm a Ninja!");
  }
}
var dylan = new NinjaConstructor('Dylan', 'Construction Worker');
var nikki = NinjaConstructor('Nikki','Historian');






















//
