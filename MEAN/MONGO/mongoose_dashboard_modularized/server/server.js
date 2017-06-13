var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
//-------------------------------------------------
mongoose.connect('mongodb://localhost/mongoose_dashboard');
var AnimalSchema = new mongoose.Schema({
  name: {type: String, required: true, minlength: 2},
  age: {type: Number, required: true},
  date: {type: Date, default: Date.now}
});
var Animal = mongoose.model('Animal', AnimalSchema);
//-------------------------------------------------
app.use(bodyParser.urlencoded({ extended: true }));
var path = require('path');
app.use(express.static(path.join(__dirname, '.static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
//-------------------------------------------------

//<----Index page---->
app.get('/', function(req, res){
  Animal.find({}, function(err, results){
    if (err){
      console.log(err)}
      res.render('index',{animals: results});
  });
});
//<----New page with form---->
app.get('/new', function(req, res){
  console.log('Its Getting /animal/new route function');
  res.render('new');
});
//<----Create---->
app.post('/create', function(req, res){
  Animal.create(req.body, function(err, results){
    if (err){
      console.log(err);}
      res.redirect('/');
  });
});
//<----Show---->
app.get('/animals/:id', function(req, res){
  Animal.find({ _id: req.params.id }, function(err, response){
    if (err){
      console.log(err);}
      res.render('show', {animal: response[0] });
  });
});
//<----Edit---->
app.get('/:id/edit', function(req, res){
  Animal.find({ _id: req.params.id }, function(err, response){
    if (err){
      console.log(err);}
      res.render('edit', { animal: response[0] });
  });
});
//<----Update---->
app.post('/:id', function(req, res){
  Animal.update({ _id: req.params.id }, req.body, function(err, result){
    if (err){
      console.log(err);}
      res.redirect('/');
  });
});
//<----Delete---->
app.post('/:id/delete', function(req, res){
  Animal.remove({ _id: req.params.id}, function(err,result){
    if (err){
      console.log(err);};
      res.redirect('/');
  });
});
//-------------------------------------------------
app.listen(8000, function(){
  console.log("Listening on Port 8000");
});
