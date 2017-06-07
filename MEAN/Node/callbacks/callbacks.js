// var ninja = 'Libby';
// setTimeout( function (){
//   console.log(ninja);
// }, 100 );
// console.log(ninja);
//
//
//
// console.log("NOW: ");
// console.log("Declaring and assigning variable 'ninja'.");
// var ninja = 'Libby';
// setTimeout( function myCallbackFunction(){
//   console.log("LATER: ")
//   console.log(ninja, "LATER");
// }, 2000);
// console.log("Printing ninja value.");
// console.log(ninja, "NOW");
//
//
//
// var a = 2;
// var b = function() {
//   console.log("something");
// };
// function doSomething(x) {
//   console.log(typeof(x));
// };
// doSomething(a);
// doSomething(b);
//
//
//
// function doSomething(possibleCallback) {
//   if (typeof(possibleCallback) === 'function'){
//     console.log('possibleCallback is a callback!');
//     possibleCallback(); //we can invoke the callback!
//   }
//   else {
//     console.log('possibleCallback: ', possibleCallback, ' is not a callback function.');
//   }
// }
// doSomething(function myCallback(){ console.log('yes, I am a callback!') });
// doSomething('string');
//
//
//
//
// function makePasta(pasta, makeSauce) {
//   console.log("Boiling water");
//   console.log("Putting " + pasta + " pasta in the water");
//   console.log("Pasta is done!");
//   return pasta + " Pasta! Voila!";
// }
// makePasta("Penne");
// makePasta("Farfalle");
//
// function makePasta(pasta, makeSauce) {
//   console.log("Boiling water");
//   console.log("Putting " + pasta + " pasta in the water");
//   // create a variable for sauce!
//   var sauce = makeSauce();          // invoke makeSauce, our callback
//   console.log("Mixing sauce");
//   console.log("Pasta is done!");
//   return pasta + " Pasta with " + sauce + " sauce! Voila!";
// }
// function makePesto() {
//   console.log("Making Pesto");
//   return "pesto";
// }
// function makeAlfredo() {
//   console.log("Making Alfredo");
//   return "alfredo";
// }
// // we pass the whole makePesto recipe to makePasta!
// console.log(makePasta("Penne", makePesto));
// // notice lack of parentheses after makeAlfredo.
// // Remember: we want to pass the function, not execute it and pass a return value.
// console.log(makePasta("Farfalle", makeAlfredo));


//
// function leadBootcamp(language, leader){
//     var outcome = leader(language);
//     console.log(outcome);
// }
// function Mike(language){
//   var languages={
//     'javascript':'successful leader',
//     'PHP':'successful leader',
//     'Python':'successful leader',
//     'Ruby':'successful leader',
//   }
//   if(languages[language]){
//     return languages[language];
//   }
//   else {
//     return "maybe not yet";
//   }
// }
// function Charlie(language){
//   var languages={
//     'javascript':'successful leader',
//     'PHP':'successful leader',
//     'Python':'successful leader',
//     'Ruby':'successful leader',
//   }
//   if(languages[language]){
//     return languages[language];
//   }
//   else {
//     return "maybe not yet";
//   }
// }
// function Jimmy(language){
//   var languages={
//     'javascript':'successful leader',
//     'PHP':'successful leader',
//     'Python':'successful leader',
//     'Ruby':'successful leader',
//     'iOS':'successful leader',
//     'java_android':'successful leader',
//   }
//   if(languages[language]){
//     return languages[language];
//   }
//   else {
//     return "maybe not yet";
//   }
// }
// leadBootcamp('java_android', Mike);
// leadBootcamp('java_android', Charlie);
// leadBootcamp('java_android', Jimmy);



var evens = _.filter([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(evens);























//
