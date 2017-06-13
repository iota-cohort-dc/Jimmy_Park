//-------------------------------------------------
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
//-------------------------------------------------
mongoose.connect('mongodb://localhost/basic_mongoose');
var UserSchema = new mongoose.Schema({
  name: {type: String, required: true, minlength: 2},
  age: {type: Number, min: 1, max: 150}
})
mongoose.model('User', UserSchema);
var User = mongoose.model('User');
//-------------------------------------------------
app.use(bodyParser.urlencoded({ extended: true}));
var path = require('path');
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
//-------------------------------------------------
app.get('/', function(req, res){
  User.find({}, function(err, users){
    res.render('index',{users: users});
    console.log(User.name); // this console.log does not work.
  })
})


app.post('/users', function(req, res){
  console.log('POST DATA', req.body);
  var user = new User({name: req.body.name, age: req.body.age});
  user.save(function(err){
    if(err){
      console.log('Something went wrong!!');
    }
    else {
      console.log('Successfully added a user!');
      res.redirect('/');
    }
  })
})
//-------------------------------------------------
//-------------------------------------------------
app.listen(8000, function(){
  console.log('listening on port 8000')
})
