// remove duplicates

// function removeDuplicates (arr){
//   var newArr = []
//   var x = 0
//   for (var i = 0; i < arr.length; i++){
//     if(arr[i] != arr[i + 1]){
//       newArr[x] = arr[i];
//       x++;
//     }
//   }
//   return newArr;
// }
// removeDuplicates([1,2,2,3,4,5,5,6,7])
//
// function rfactorial(num){
//   if(num == 1){
//     return 1;
//   }
//   else {
//     return num * rfactorial(num-1);
//   }
// }
// console.log(rfactorial(6));

//===========================================

// function rBinaryStrExp(str){
//   var arr = [];
//   var curr = "";
//   (function helper(str, curr, arr){
//     if(curr.length == str.length){
//       arr.push(curr);
//     }
//     else {
//       helper(str, curr + "0", arr);
//       helper(str, curr + "1", arr);
//     }
//   })(str,curr,arr);
//   return arr;
// }
// console.log(rBinaryStrExp("1,2"));

// function rBinaryStrExp(str){
//   var arr = [];
//   var curr = "";
//   function helper(str, curr, arr){
//     if(curr.length == str.length){
//       arr.push(curr);
//     }
//     else {
//       helper(str, curr + "0", arr);
//       helper(str, curr + "1", arr);
//     }
//   };
//   helper(str, curr, arr);
//   return arr;
// }
// console.log(rBinaryStrExp("AB"));


function binaryStringExpansion(str, substr, arr){
  return helper(str, "", []);
  function helper(str, substr, arr){
    if(!str[substr.length]){
      arr.push(substr);
    }
    else {
      if(str[substr.length] != "?"){
        helper(str, substr + str[substr.length], arr)
      }
      else {
        helper(str, substr + "0", arr);
        helper(str, substr + "1", arr);
      }
    }
    return arr;
  }
}

console.log(binaryStringExpansion("??"));
