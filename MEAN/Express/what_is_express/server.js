var express = require("express")

var app = express();

// app can handle get and post requests

app.get('/', function(request, response){
  response.send("hello express");
})

app.listen(8000, function(){
  console.log("listening on 8000");
})
















//
