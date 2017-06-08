//load the express module
//load the path module
//load the body-parser
var express = require("express");
var path = require("path");
var bodyParser = require('body-parser');
// invoke var express and store the resulting application in var app
var app = express();
// =================================================================
app.use(bodyParser.urlencoded());
app.use(express.static(path.join(__dirname, "./static")));
// setting up ejs and our views folder
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

//we're going to have /routes/index.js handle all of our routing
var route = require('./routes/index.js')(app);
// setting server to run on port 3000
app.listen(3000, function() {
 console.log("listening on port 3000!");
})
