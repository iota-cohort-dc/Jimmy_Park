//-------------------------------------------------
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
//-------------------------------------------------
mongoose.connect('mongodb://localhost/quoting_dojo_redux');
var QuoteSchema = new mongoose.Schema({
  name: {type: String, required: true, minlenght: 2},
  quote: {type: String, required: true, minlength: 2},
  date: {type: Date, default: Date.now}
});
// var QuoteSchema = new mongoose.Schema({
//   name: String,
//   quote: String
// });
var Quote = mongoose.model('Quote', QuoteSchema);
//-------------------------------------------------
app.use(bodyParser.urlencoded({ extended: true }));
var path = require('path');
// app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
//-------------------------------------------------
app.get('/', function(req, res){
    console.log("It is getting here");
    res.render('index');
});

app.get('/quotes', function(req, res){
  Quote.find({}, function(err, quotes){
      if(err) { console.log(err); }
      res.render('quotes',{quotes: quotes});

  });
});

app.post('/quotes', function(req, res){
  console.log('POST DATA', req.body);
  var quote = new Quote({name: req.body.name, quote: req.body.quote});
  quote.save(function(err){
    if(err){
      console.log('Something wend wrong!!');
    }
    else {
      console.log('Successfully added quote!');
      res.redirect('/quotes')
    };
  });
});
//-------------------------------------------------
app.listen(8000, function(){
  console.log('listening to port 8000')
});
