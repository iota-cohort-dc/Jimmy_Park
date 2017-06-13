var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var path = require('path');
//-------------------------------------------------
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '../client/static')));
app.set('views', path.join(__dirname, '../client/views'));
app.set('view engine', 'ejs');
var port = 8000;
//-------------------------------------------------
require('./config/mongoose.js');
//-------------------------------------------------
var routes_setter = require('./config/routes.js')
routes_setter(app);
//-------------------------------------------------

app.listen(port, function(){
  console.log("Listening on Port", port);
});
