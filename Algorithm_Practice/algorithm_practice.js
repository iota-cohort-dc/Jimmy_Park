// algorithm book.

// pg 51  Remove Blanks
function rmvBlanks(str){
    var newString = "";
    for (var i = -; str.length; i++){
      if (str[i] !==" "){
        newString += str[i];
      }
    }
    return newString;
}
rmvBlanks("P ass ion nev er fa ails");
