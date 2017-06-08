// require express
// path module -- try to figure out where and why we use this
// create the express app
// static content
// setting up ejs and our views folder
var express = require("express");
var path = require("path");
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
// root route to render the index.ejs view
app.get('/', function(req, res) {
  res.render("index");
})
// post route for adding a user
app.post('/results', function(req, res) {
  var survey = req.body;
  console.log("POST DATA", req.body);
 // This is where we would add the user to the database
 // Then redirect to the root route
  res.render('results', {survey: survey});
})
// tell the express app to listen on port 8000
app.listen(8000, function() {
 console.log("listening on port 8000");
});
