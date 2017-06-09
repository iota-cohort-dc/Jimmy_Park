var express = require("express"); // require express
var path = require("path");  // path module -- try to figure out where and why we use this
var app = express(); // create the express app
// var bodyParser = require('body-parser');
// app.use(bodyParser.urlencoded({ extended: true }));
// app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views')); // setting up ejs and our views folder
app.set('view engine', 'ejs'); // setting up ejs and our views folder
app.get('/', function(req, res) { //// this is rendering the index.ejs from views folder
  res.render("index");
});
// tell the express app to listen on port 8000
var server = app.listen(8000, function() {
 console.log("listening on port 8000");
});
//<----------- below is where we use SOCKET ---------------------->
var io = require('socket.io').listen(server); //// ((server)) is from line 25
io.sockets.on('connection', function (socket) {
  var counter = 0;
  socket.on("clicking_push_button", function (data){
    counter +=1;
    console.log(data.action);
    socket.emit('send_counter', {response: counter});
    console.log(counter);
  })
  socket.on("clicking_reset_button", function (data){
    counter = 0;
    console.log(data.action);
    socket.emit('reseting_counter', {response: counter});
    console.log(counter);
  })

})
