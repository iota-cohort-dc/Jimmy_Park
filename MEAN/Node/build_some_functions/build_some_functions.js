function runningLogger(){
  console.log('I am running');
}

function multiplyByTen(x){
  console.log(x * 10);
}
multiplyByTen(5);

function stringReturnOne(){
  console.log('This is String One')
}

function stringReturnTwo(){
  console.log('This is String Two')
}

function myFunctionRunner(param){   // this one was in solutions
  if (typeof(param)=='function'){
    param();
  }
}
myFunctionRunner(stringReturnOne);

function caller(z){
  if(typeof(z) === 'function'){
    console.log(z);
  }
  else{
    return NaN;
  }
}

caller(multiplyByTen);

function myDoubleConsoleLog(a,b){
  if(typeof(a) === 'function'){
    console.log(a);
  } else {
    return NaN;
  }
  if(typeof(b) === 'function'){
    console.log(b);
  } else {
    return NaN;
  }
}

function caller2(x){
  console.log('starting');
  var a = setTimeout(function(){
    if(typeof(x) === 'function'){
      x(stringReturnOne, stringReturnTwo);
    }
  }, 2000);
  console.log('ending');
  return 'interesting';
}
caller2(myDoubleConsoleLog);

// -----------------------------------------------------------------------------
// ---------------------- below is what the solutions has ----------------------
// -----------------------------------------------------------------------------

/*
  Goal for these first 'easy' difficulty level assignments:
  returns versus void returns
*/

function runningLogger(){
  console.log("I am running");
}

function multiplyBy10(numb){
  if (typeof(numb) == "number"){
    return numb*10;
  }
}

function stringReturnOne(){
  return "cat";
}

function stringReturnTwo(){
  return "dog";
}

function myFunctionRunner(param){
  if (typeof(param)=='function'){
    param();
  }
}
// Somewhat interesting right?
myFunctionRunner(stringReturnOne);

function myDoubleConsoleLog(param1,param2){
  if (typeof(param1) == 'function' && typeof(param2) == 'function'){
    console.log(param1(), param2());
  }
}
myDoubleConsoleLog(stringReturnOne, stringReturnTwo);

// more interesting, we hope!
function caller2(param){
  console.log('starting');
  var x = setTimeout(function(){
    if (typeof(param)=='function'){
      // notice the passed parameters...
      param(stringReturnOne, stringReturnTwo);
    }
  }, 2000);
  console.log('ending');
  return "interesting";
}

caller2(myDoubleConsoleLog);
