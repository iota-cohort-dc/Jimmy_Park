

var names = ["James","Jill","jane","Jack"];

function fancyArray (){
  count = 0;
  for(var idx = 0; idx < names.length; idx++){
    console.log(idx +" --> " + names[idx]);
    count+=1;
  }
}

fancyArray();
