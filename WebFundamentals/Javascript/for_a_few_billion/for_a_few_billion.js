function forabillion(){
  var p = .01;
    for(var i = 1; i <= 30; i++){
      p = p *2;
    }
    console.log(p);
}
forabillion();

// function doubleAmount(dollarAmount, days){
//   var total = dollarAmount;
//     while (i < days && days > !) {
//       total += total;
//       i++;
//     }
//     return total;
// }
// console.log(doubleAmount(0.01, 30))

// var money = doubleAmount(0.01, 30);
// money += 1000000000
// console.log(money);


function forabillion(){
  var p = .01;
    for(var i = 1; i <= 30; i++){
      p = p *2;
      if(p > 10000)
        break;
    }
    console.log(i);
}
forabillion();

// function howManyDays (dollarAmount){
//   var total = .01;
//   var i =1;
//   while (true) {
//     if (total >= dollarAmount){
//       return (i);
//     }
//     total += total;
//   }
// }
// console.log(howManyDays());

function forabillion(){
  var p = .01;
    for(var i = 1; i <= Infinity; i++){
      p = p * 2;
      if(p > 1000000000)
        break;
    }
    console.log(i);
}
forabillion();
