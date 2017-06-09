var express = require("express"); // require express
var path = require("path");  // path module -- try to figure out where and why we use this
var app = express(); // create the express app
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views')); // setting up ejs and our views folder
app.set('view engine', 'ejs'); // setting up ejs and our views folder
app.get('/', function(req, res) { //// this is rendering the index.ejs from views folder
  res.render("index");
});
// post route for adding a user
app.post('/results', function(req, res) { //// this is is from the FORM
  var survey = req.body;                  //// this is getting content from FORM and setting it to a variable survey
  console.log("POST DATA", req.body);
  res.render('results', {survey: survey});//// this is passing content to parse info on the page.  Parsing to the page.
});
// tell the express app to listen on port 8000
var server = app.listen(8000, function() {
 console.log("listening on port 8000");
});
//<----------- below is where we use SOCKET ---------------------->
var io = require('socket.io').listen(server); //// ((server)) is from line 25
io.sockets.on('connection', function (socket) {
  socket.on("posting_form", function (data){
    var random_number = Math.floor((Math.random() * 1000) + 1);
    socket.emit('updated_message', {response: data});
    socket.emit('random_number', {response: random_number});
    console.log(socket.id);
  })
})
