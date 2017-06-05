// =============================================================================
// Create a simple for loop that sums all the integers between x and y (inclusive). Have it console log the final sum.
function sumIntegers(x,y){
  var sum = 0;
  for(var i = 0; i < y; i++){
    sum = sum + i;    // ((or)) sum += i;
    console.log(sum); // this one console log every iteration
  }
  console.log(sum); // this one just gives total of sum // return sum;
}
sumIntegers(10,10);

// Anonymous functions assigned to variables
var sumIntegers = function(x,y){
  var sum = 0;
  for(var i = 0; i < y; i++){
    sum = sum + i;   // ((or)) sum += i;
    console.log(sum);
  }
  console.log(sum); // return sum;
}
sumIntegers(4,4);

// Rewrite these as methods of an object
var myobject = {
  name: 
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
    console.log('The min is: ',min);  // return sum;
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
  console.log(min);
  return min;
}
findMin([0,1,2,3,4,5,6,7,8,9,10]);

// Rewrite these as methods of an object

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

// =============================================================================

    //--------------- CODE BELOW IS FROM THE A PREVIOUS ASSIGNMENT -------------
    // ------------- FROM js_fundamentals_part_1 -------------------------------
    //
    // // ITERATE THRU ALL THE ITEMS IN THE ARRAYS
    // x = [[3,5,"Dojo", "rocks", "Michael", "Sensei"], ["hello", "world", "JavaScript is Fun"]]
    // for (var i = 0; i < x.length; i++){
    //   console.log(x[i]);
    // };
    // x.push(100);
    //
    // // GET THE SUM OF ALL VALUES IN THE ARRAY
    // var array = [1, 5, 90, 25, -3, 0];
    // var sum = 0;
    // for (var i = 1; i < 501; i++){
    //   sum = sum + i;
    // };
    // console.log(sum);
    //
    // // GET THE MIN OF THE ARRAY
    // var array = [1, 5, 90, 25, -3, 0];
    // var min = 0;
    // for (var i = 0; i < array.length; i++){
    //   if(array[i] < min){
    //     sum = array[i];
    //   }
    // };
    // console.log(min);
    //
    // // FIND MAX MIN AVG
    // var array = [1, 5, 90, 25, -3, 0];
    // var max = 0;
    // var min = 0;
    // var sum = 0;
    // for (var i = 0; i < array.length; i++){
    //   if(array[i] > max){
    //     max = array[i];
    //   }
    //   if(array[i] > min){
    //     min = array[i];
    //   }
    //   if(array[i] < min){
    //     sum = array[i];
    //   }
    //   var avg = sum/array.length;
    // }
    // console.log('this is the sum:',sum);
    // console.log('this is the avg:',avg);
    //
    // // GET THE SUM OF THE ARRAY
    // var array = [1, 5, 90, 25, -3, 0];
    // var sum = array[0];
    // for (var i = 1; i < array.length; i++) {
    //     sum  += array[i];
    // }
    // console.log(sum/array.length);
    //
    // // *FOR-IN* LOOP, OF THE OBJECT
    // var new_ninja = {
    // name: 'Jessica',
    // profession: 'coder',
    // favorite_language: 'JavaScript',
    // dojo: 'Dallas'
    // };
    //
    // for (var key in new_ninja){
    //   console.log(key + " : " + new_ninja[key]);
    // }
