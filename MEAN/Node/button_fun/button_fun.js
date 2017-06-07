//
// // Link our variable "button" to a DOM element
// var button = document.getElementById("someButton")
// // add a DOM eventListener to that variable.
// button.addEventListener("click", whatToDoOnClick);
// // here we define the whatToDoOnClick function
// function whatToDoOnClick() {
//   alert("You Did it!")
// }

$(document).ready(function(){


  $("button").on('click', 'button', function(){
      $(this).toggleClass(".red");
  });

  $("button").hover(function(){
      $(this).addClass(".green")
  }, function(){ $(this).removeClass(".green") });


});
