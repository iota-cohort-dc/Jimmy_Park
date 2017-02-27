var hour = 8;
var minute = 50;
var period = "AM";

if (hour < 10 && hour > 8) {
  if (minute < 51 && hour > 30){
    if (period === "AM"){
      console.log("It's almost 9 in the morning");
    } else {
      console.log("It's 9 at night");
    }
  } else {
    console.log("It's not close to 9 yet");
  }
  console.log("It's time to go back to sleep");
}

var hour = 7;
var minute = 15;
var period = "PM";
