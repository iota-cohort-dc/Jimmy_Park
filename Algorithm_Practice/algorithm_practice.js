

//<----------------------- Print 1-255 (arrays) ---------------------------->

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

//<-------------------------- Odds 1-255 (arrays) --------------------------->

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

//<------------------------- Print Sum 0-255 (arrays) ----------------------->

function sumAll () {
	var sum = 0;
	for ( var i = 0; i < 256; i++ ) {
	sum = sum + i;
	}
	return sum;
}

//<------------------------- Iterate Array (arrays) -------------------------->
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

//<--------------------------- Find Max (arrays) ---------------------------->
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

//<------------------------- Get average (arrays)----------------------------->
//  Analyze an array’s values and print the average

function getAvg (arr) {
	var sum = 0;
	for ( var i = 0; i < arr.length; i++ ) {
		sum = sum + arr[ i ];
	}
	var avg = sum / arr.length;
	return avg;
}

//<------------------------ Array with odds (arrays) ------------------------>
//       Create an array with odd integers from 1 - 255

function arrOdds () {
	var arr = [ ];
	for ( var i = 1; i < 256; i++ ) {
		if ( i % 2 == 1 ) {
		arr.push( i );
	}
	return arr;
}

//<--------------------- Square the Values (arrays) ------------------------->
//       Given an array, square each value in the array

function square (arr) {

	for ( var i = 0; i < arr.length; i++ ) {
	arr[ i ] = arr[ i ] * arr[ i ];
	}
	return arr;
}

//<----------------------- Greater than Y (arrays)---------------------------->
//       Count the number of array values greater than a given Y

function greaterY (arr, Y) {
	var count = 0;
	for ( var i = 0; i < arr.length; i++ ) {
		if ( arr[ i ] > Y ) {
		count++;
	}
	return count;
}


//<---------------------- Zero out negative numbers (arrays)------------------>
//     Set negative array values to zero

function negative (arr) {
	var temp = 0;
	for (var i = 0; i < arr.length; i++) {
		if ( arr[ i ] < 0 ) {
		arr[ i ] = temp;
	}
	return arr;
}

//<----------------------- Max, Min, Average (arrays)------------------------>
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

//<----------------------- Shift array values (arrays)------------------------>
//         Given an array, shift all values forward, dropping the first value and leaving an extra ‘0’ value at the end

function shiftArr (arr) {
	var temp = 0;
	arr.pop[arr.length -1];
	arr[ 0 ] = temp;

	return arr;
}

//<------------------------- Number to string (arrays)------------------------>
//         Replace any negative values in an array with ‘Dojo’

function numString (arr) {
	for ( var i = 0; i < arr.length; i ++ ) {
		if ( arr[ i ] < 0 ) {
			arr[ i ] = “Dojo”
	}
	return arr;
}

//<-------------------------- count non-spaces ------------------------------>
function countNonSpaces (arr){
	count = 0
	for (var i = 0; i < str.length; i++){
		if (arr[i] != ""){
			count += 1;
		}
	}
}

//<---------------------------- string reverse ------------------------------>
function strReverse (str){
	temp = 0;
	arr = str.split("");
	for (var i = 0; i < arr.length/2; i++){
		temp = arr[i];
		arr[i] = arr[(arr.length - 1) - i];
		arr[(arr.length - 1) - i] = temp;
	}
	arr = arr.join;
	return arr;
}

//<-------------------------- zipIt (arrays) (marcos)------------------------>
function zipIt (arr1, arr2){
	var newArr = []
	i = 0
	yep = true
	while (yep){
		yep = false;
		if (i < arr1.length){
			newArr[newArr.length] = arr1[i];
			yep = true;
		}
		if (i < arr2.length){
			newArr[newArr.length] = arr2[i];
			yep = true;
		}
		i++;
	}
	return newArr;
}

//<------------------- remove Blanks from string (arrays) ------------------->
function removeBlanks(str){
	var newArr = []
	for(var i = 0; i < str.length; i++){
		if(str[i] != " "){
			newArr[newArr.length] = str[i];
		}
	}
	return newArr.join("");
}
removeBlanks(['as','fd','rty','hjm','dbf','c','bnn'])

// acronyms

//<--------- Remove Negatives in a given array (arrays) tested good --------->

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

//<---------------- pg 51  Remove Blanks (arrays)---------------------------->

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

//<------------------------------ braces valid ----------------------------->
//  ex ([{}[]{}])

function bracesValid(str) {
    var arr = [];
    for(var i = 0; i < str.length; i++) {
        if(str[i] == "{" || str[i] == "[" || str[i] == "(") {
            arr.push(str[i]);
        }
        else if(str[i] == "}" || str[i] == "]" || str[i] == ")") {
            if(str[i] == "}") {
                if(arr[arr.lenth-1] != "{") {
                    return false;
                }
                else {
                    arr.pop();
                }
            }
            else if(str[i] == "]") {
                if(arr[arr.lenth-1] != "[") {
                    return false;
                }
                else {
                    arr.pop();
                }
            }
            else if(str[i] == ")") {
                if(arr[arr.lenth-1] != "(") {
                    return false;
                }
                else {
                    arr.pop();
                }
            }
        }
    }
    if(arr == []) {
        return true;
    }
    else {
        return false;
    }
}

//<------------------------------ isPalindrone ------------------------------->

// ex racecar
function is Palindrone(str){
	for (var i = 0; i < strength/2; i++){
		if (str[i] != str[str.length -1] - i){
			return false;
		}
	}
}

//<------------------------------ Drop the mike ------------------------------>
// create a standalone function that accepts an input string, removes leading and trailing white space (at beginning and end only), capitlalize the first letter of every word, and returns that string. if original string contains the word "mike" anywhere, immediately return "stunned silence" instead.

function dropMike(str){
	arr = []
	str = str.split("");
	for (var i = 0; i < str.length; i++){
		if (str[i] == "mike" || str[i] == "Mike"){
			return "stunned silence";
		}
	}
	for (for i = 0; i < str.length; i ++){
		if (str[i] != ""){
			arr.push(str[i]);
		}
	}
	for (var i = 0; i < arr.length; i++){
		arr[i] = arr [i].split("");
		arr[i][0] = arr[i][0].toUpperCase();
		arr[i] = arr[i].join("");
	}
	return arr.join("");
}

//<---------------------------- String Concat -------------------------------->
// add string to the end of existing one and return new string

function conCat(str1,str2){
	var newArr1 = [];
	new newArr2 = [];
	new newStr = " ";
	new newArr1 = str1.split(" ");
	new newArr2 = str2.split(" ");
	for (var i = 0; i < newArr2.length; i++){
		newArr1[newArr1.length] = newArr2[1]
	}
	newStr = newArr1.join(" ");
	return newStr;
}

// or

function stringConcat(...args){
	var str = " ";
	for (var i = 0; i < args.length; i++){
		str += args[i];
	}
	return str;
}

// or

function concatString(){
	var x = " ";
	for (var i = 0; i < arguments.length; i++){
		x += arguemnts[i]
	}
	return x;
}

//<-------------------------------- string.slice ----------------------------->
// string.slice(start,end) extract part of a string and return in a new one.  Start and end are indices into the string, with the first character at index 0. end param is optional and if present, refers to one beyond the last character to include.

function stringSlice(str,b,e){
	str = str.split(" ")
	var str1 = [];
	if (e == pull){
		for (var i = b; i < str.length; i++){
			str1[str.length] = str[i];
		}
	}
	else {
		for (var i = 0; i <= e; i++){
			str1[str1 length] = str[i];
		}
	}
	return str1.join("");
}


//<--------------- pg 66 SList: Remove Negatives (linked lists)--------------->
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

//+++++++++++++++++++++++++++ LINKED LISTS ++++++++++++++++++++++++++++++

//<------------------------ SLL add to front --------------------------->

function node(val){
	this.val = value;
	this.head = null;
}
function SLL(){
	this.head = null;
	this.addFront = function(val){
		var node =  new Node(val);
		if(!this.head){    		//or can say if(this.head == null)
			this.head = node;
			return this;
		}
		else{
			node.next = this.head;
			this.head = node;
			return this;
		}
	}
}
var myList = new SLL();
console.log(myList);
myList.addFront(4);
console.log(myList);
myList.addFront(5).addFront(6);
console.log(myList);



//<----------------- page 63 SList: split on Value----------------------->

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

//<------------------------- deck of cards -------------------------->

function DeckConstructor(){
    var suits = ["Hearts", "Spades", "Clubs", "Diamonds"];
    var values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];
    var deck = [];

    this.showDeck = function(){
        console.log(deck);
        console.log("Length:", deck.length);
    }
    var generateDeck = function(){
        deck = [];
        for (var i=0; i < suits.length; i++){
            for (var j=0; j<values.length; j++){
                var card = {};
                card.suit = suits[i];
                card.value = values[j];
                deck.push(card);
            }
        }
        return this;
    }
    generateDeck();

    this.shuffle = function(){
        var numberOfShuffles = Math.floor((Math.random() * 100 ) + 50);
        for (var i = 0; i <= numberOfShuffles; i++){
            var randomInteger1 = Math.floor(Math.random() * deck.length);
            var randomInteger2 = Math.floor(Math.random() * deck.length);
            var temp = deck[randomInteger1];
            deck[randomInteger1] = deck[randomInteger2];
            deck[randomInteger2] = temp;
        }
        return this;
    }
    this.reset = generateDeck;
    this.deal = function(){
        return deck.pop();
    }
}
function PlayerConstructor(name){
    this.name = name;
    this.hand = [];
}
PlayerConstructor.prototype.takeCard = function(deck){
    var card = deck.deal();
    this.hand.push(card);
    return this;
}
