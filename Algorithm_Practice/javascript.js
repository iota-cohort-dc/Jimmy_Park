// remove duplicates

function removeDuplicates (arr){
  var newArr = []
  var x = 0
  for (var i = 0; i < arr.length; i++){
    if(arr[i] != arr[i + 1]){
      newArr[x] = arr[i];
      x++;
    }
  }
  return newArr;
}
removeDuplicates([1,2,2,3,4,5,5,6,7])
