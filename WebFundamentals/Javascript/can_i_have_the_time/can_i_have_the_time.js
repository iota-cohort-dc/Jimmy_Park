// var hour = 8;
// var minute = 50;
// var period = "AM";

function gotTime(hour, minute, period) {
  if(minute > 30){
    minute = "its almost";
    hour +=1;
  }
  else (minute = "just after");
  if (period == "AM"){
    period = "in the morning";
  }
  else (period = "in the eveneing");

  console.log(minute, hour, period);
}
gotTime(6, 40, "PM");
