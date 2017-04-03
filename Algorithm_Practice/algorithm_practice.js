// #1  Print 1-255
//       Print all the integers from 1 to 255

function  integers () {
	var arr = [];
	for ( var i = 1; i < 256; i++ ) {
		arr.push( i );
	}
	return arr;
}

function integers () {
	for ( var i = 1; i < 256; i++) {
	console.log( i );
}



// #2  Odds 1-255
//       Print all odd integers from 1 to 255

function odds () {
	var arr = [];
	for ( var i = 1; i < 256; i++ ) {
		if ( i % 2 == 1 ) {
		arr.push( i );
	}
	return arr;
}

function off () {
	for ( var i = 1; i < 256; i++ ) {5
		if ( i % 2 ==1 ) {
		console.log( i );
	}
}



// #3  Print Sum 0-255
//       Print integers from 0 to 255, and the sum so far

function sumAll () {
	var sum = 0;
	for ( var i = 0; i < 256; i++ ) {
	sum = sum + i;
	}
	return sum;
}



// #4  Iterate Array
//       Print all values in a given array.

function iterateArr (arr) {
	for ( var i = 0; i < arr.length; i++) {
	console.log( i );
	}
}

function iterArr (arr) {
	for ( var i = 0; i < arr.length; i++ ) {
	arr[ i ] = sum + arr[ i ];
	}
	return sum:
}


// #5  Find Max
//       Print the largest element in a given array

function maxMinAvg (arr) {
	var max = [0];
	var min = [0];
	var sum = [0];
	for ( var i = 1; i < arr.length; i++ ) {
		if ( max < arr[ i ] ) {
		     max = arr[ i ];
		}
		if ( min > arr[ i ] ) {
		     min = arr[ i ];
		}
		sum = sum + arr[ i ];
	}
	}
	var avg = sum / arr.length;
	var arrNew = [max, min, avg]
	return arrNew;
}


// #6  Get average
//       Analyze an array’s values and print the average

function getAvg (arr) {
	var sum = 0;
	for ( var i = 0; i < arr.length; i++ ) {
		sum = sum + arr[ i ];
	}
	var avg = sum / arr.length;
	return avg;
}


// #7  Array with odds
//       Create an array with odd integers from 1 - 255

function arrOdds () {
	var arr = [ ];
	for ( var i = 1; i < 256; i++ ) {
		if ( i % 2 == 1 ) {
		arr.push( i );
	}
	return arr;
}


// #8  Square the Values
//       Given an array, square each value in the array

function square (arr) {

	for ( var i = 0; i < arr.length; i++ ) {
	arr[ i ] = arr[ i ] * arr[ i ];
	}
	return arr;
}


// #9  Greater than Y
//       Count the number of array values greater than a given Y

function greaterY (arr, Y) {
	var count = 0;
	for ( var i = 0; i < arr.length; i++ ) {
		if ( arr[ i ] > Y ) {
		count++;
	}
	return count;
}


// #10  Zero out negative numbers
//         Set negative array values to zero

function negative (arr) {
	var temp = 0;
	for (var i = 0; i < arr.length; i++) {
		if ( arr[ i ] < 0 ) {
		arr[ i ] = temp;
	}
	return arr;
}


// #11  Max, Min, Average
//         Given an array, print max, min, and average values

function maxMinAvg (arr) {
	var max = [0];
	var min  = [0];
	var sum = [0];
	for ( var i = 1; i < arr.length; i++ ) {
		if ( max < arr[ i ] ) {
		     max  = arr [ i ];
		}
		if ( min > arr[ i ] ) {
		     min = arr[ i ];
		}
	var avg = sum / arr.length;
	var arrNew = [max, min , avg]
	return arrNew;
}


// #12  Shift array values
//         Given an array, shift all values forward, dropping the first value and leaving an extra ‘0’ value at the end

function shiftArr (arr) {
	var temp = 0;
	arr.pop[arr.length -1];
	arr[ 0 ] = temp;

	return arr;
}


// #13  Number to string
//         Replace any negative values in an array with ‘Dojo’

function numString (arr) {
	for ( var i = 0; i < arr.length; i ++ ) {
		if ( arr[ i ] < 0 ) {
			arr[ i ] = “Dojo”
	}
	return arr;
}


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

// pg 66 SList: Remove Negatives
// Given a pointer to the head node of the singly linked list, remove any nodes containing negative values and return the new list.

function ListNode (){
  this.val = value;
  this.next = null;
}
this.removeNegatives = function SLL (){
  this.head = null;
  var current = this.head;
  var temp = null;
  if ( !this.head ){
    return false;
  }
  while( current.next != null){}
    if ( current.val > 0 ){
      current = current.next;
    }
    else; {
    temp = current.next;
    temp.next = current.next.next;
    }
  }
}


// page 63 SList: split on Value
function ListNode () {
	this.val = value;
	this.next = null;
}
function SLL () {
	this.head = null;

	this.addFront = function(val){
		if ( !this.head) {
			this.head = new Node (val);
			return this;
		}
	}

	this.SplitOnVal = function (list,num){
	var current = this.head;
	if (!this.head){
		return False;
	}
	if (this.head.val == num) {
		console.log("num is at beginning of list");
		return list;
	}
	while (current.next) {
		current = current.next;
		if (current.next.val == num) {
			list.head == current.next;
			current.next = null;
			break;
		}
	var list = new SLL ();
	list.head = temp;
	return list.head;
	}
}

var list  = new SLL ()
list.addFront(5)
list.addFront(2)
list.addFront(7)
list.addFront(1)
list.addFront(22)
console.log(list.SplitOnVal(4));





































//
