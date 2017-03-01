var quart = 10;
// var winningNum = Math.floor(Math()*100)+1;

function randomChance(quart){
    var winningNum = 50;
    while (quart > 0) {
        if(winningNum === Math.ceil(Math.random()*100)+1){
          quart = quart + Math.trunc(Math.random()*50)+51;
          quart = quart - 1;
          return quart;
        } else {
          quart = quart - 1;
          if (quart == 0){
              return quart;
          }
        }
    }
}
randomChance(quart);
