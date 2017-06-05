// =============================================================================
// Create a simple for loop that sums all the integers between x and y (inclusive). Have it console log the final sum.
function sumIntegers(x,y){
  var sum = 0;
  for(var i = 0; i < y; i++){
    sum = sum + i;    // ((or)) sum += i;
  }
  return sum;
}
sumIntegers(10,10);

// Anonymous functions assigned to variables
var sumIntegers = function(x,y){
  var sum = 0;
  for(var i = 0; i < y; i++){
    sum += i;
  }
  return sum;
}
sumIntegers(4,4);

// Rewrite these as methods of an object
var myobject = {
  sumIntegers: function(x,y){
    var sum = 0;
    for(var i = 0; i < y; i++){
      sum += i;
    }
    return sum;
  }
}

// ALL THREE METHOD FUNCTION TOGETHER
var myobject = {
  sumIntegers: function(x,y){
    var sum = 0;
    for(var i = 0; i < y; i++){
      sum += i;
    }
    return sum;
  },                              /// DONT FORGET COMMAS ,
  findMin: function(array){
    var min = array[0];
    for(var i = 0; i < array.length; i++){
      if(array[i] < min){
        min = array[i];
      }
    }
    return min;
  },                              /// DONT FORGET COMMAS ,
  findMin: function(array){
    var min = array[0];
    for(var i = 0; i < array.length; i++){
      if(array[i] < min){
        min = array[i];
      }
    }
    return min;
  }
}

// =============================================================================
// Write a loop that will go through an array, find the minimum value, and then return it

function findMin(array){
  if(array){  // this line was in the solutions.  not sure..why
    var min = array[0];
    for(var i = 1; i < array.length; i++){
      if(array[i] < min){
        min = array[i];
      }
    }
    return min;
  }
}
findMin([0,1,2,3,4,5,6,7,8,9,10])

// Anonymous functions assigned to variables
var findMin = function(array){
  var min = array[0];
  for(var i = 0; i < array.length; i++){
    if(array[i] < min){
      min = array[i];
    }
  }
  return min;
}
findMin([0,1,2,3,4,5,6,7,8,9,10]);

// Rewrite these as methods of an object

var myObject = {
  findMin: function(array){
    var min = array[0];
    for(var i = 0; i < array.length; i++){
      if(array[i] < min){
        min = array[i];
      }
    }
    return min;
  }
}

// =============================================================================
// Write a loop that will go through an array, find the average of all of the values, and then return it
function findAvg(array){
  var sum = 0;
  for(var i = 0; i < array.length; i++){
    sum = sum + i;
  }
  var avg = sum/array.length;
  console.log('The avg number is: ', avg);
}
findAvg([0,1,2,3,4,5,6,7,8,9,10]);

// Anonymous functions assigned to variables
var findAvg = function(array){
  var sum = 0;
  for(var i = 0; i < array.length; i++){
    sum = sum + i;
  }
  var avg = sum/array.length;
  console.log('The avg number is: ', avg);
}
findAvg([0,1,2,3,4,5,6,7,8,9,10]);

// Rewrite these as methods of an object
var myObject = {
  findAvg: function(array){
    var sum = 0;
    for(var i = 0; i < array.length; i++){
      sum = sum + i;
    }
    var avg = sum/array.length;
    console.log('The avg number is: ', avg);

  }
}

// =============================================================================
// =============================================================================
// =============================================================================
// Create a JavaScript object called person with the following properties/methods

var person = {
  name: "jimmy",
  distance_traveled: 0,
  say_name: function(){
    console.log(person.name);
  },
  say_something: function(phrase){
    console.log(person.name, "says:", phrase);
  },
  walk: function(){
    person.distance_traveled += 3;
    console.log("Walked",person.distance_traveled)
    return person;
  },
  run: function(){
    person.distance_traveled += 10;
    console.log("Ran", person.distance_traveled)
    return person;
  },
  crawl: function(){
    person.distance_traveled += 1;
    console.log("Crawled", person.distance_traveled)
    return person;
  }
}
person.say_something('I am cool');
person.say_name();
person.walk();
person.run();
person.crawl();

// =============================================================================
// =============================================================================
// =============================================================================
