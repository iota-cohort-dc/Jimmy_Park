var mongoose = require('mongoose');

var AnimalSchema = new mongoose.Schema({
  name: {type: String, required: true, minlength: 2},
  age: {type: Number, required: true},
  date: {type: Date, default: Date.now}
});
var Animal = mongoose.model('Animal', AnimalSchema);
