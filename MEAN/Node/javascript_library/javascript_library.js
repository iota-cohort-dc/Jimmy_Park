var _ = {
  map: function(array, callback){  // callback is a variable name.. can be named whatever
    for (var i = 0; i < array.length; i++) {
      array[i] = callback(array[i]);
    }
    return array;
  },
  reduce: function(array, callback, memo){
      var el = 0;
      if (!memo){
        memo = array[0];
        el = 1;
      }
      for (var i = el; i < array.length; i++) {
        memo = callback(array[i], memo);
      }
      return memo;

  },
  find: function(array, callback){
    for (var i = 0; i < array.length; i++) {
      if (callback(array[i])){
        return array[i];
      }
    }
  },
  filter: function(array, callback){
    var tempArray =[];
    for (var i = 0; i < array.length; i++) {
      if (callback(array[i])){
        tempArray.push(array[i]);
      }
    }
    // we could also modify the original array
    return tempArray;
  },
  reject: function(array, callback){
    var tempArray =[];
    for (var i = 0; i < array.length; i++) {
      if (!callback(array[i])){
        tempArray.push(array[i]);
      }
    }
    // we could also modify the original array
    return tempArray;
  },
}

var array = [3,4,5];
// console.log(_.map(array, function callback(x){return x * 5;}));
// console.log(_.map(array, function (num){ return num * 3;}));
// console.log(array);

// console.log(_.reduce(array, function callback(x, memo){return x + memo;}));
// console.log(_.find(array, function callback(x){return x == 15;}));
// // note: we used named functions for clarity above, but we can also pass anonymous functions as the second parameter:
// _.filter(array, function(x){return x > 20;})
// console.log(array);





// function plus5(x){
//   console.log(x)
//   console.log(x(10))
// }
//
// plus5(anotherFunction)
//
//
// function anotherFunction(will){
//   return will*10
// }
//
// function changeWill(will, WEYWantToDoToWill){
//   return will*10
//   return WEYWantToDoToWill(will)
// }
//
// changeWill(15, function(x){
//   return x*45
// })
