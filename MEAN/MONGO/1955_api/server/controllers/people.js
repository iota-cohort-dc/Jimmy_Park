//1955_api
// CONTROLLER
var mongoose = require('mongoose');
var Person = mongoose.model('Person');

module.exports = {

  index: function(req,res){  //// don't forget about commas ////
    Person.find({}, function(req, data) {
      res.json(data);
    })
  },

  create: function(req, res){
    var person = new Person({name: req.params.name});
    person.save(function(err, data){
      if(err){
        res.json(err);
      }
      else {
        res.json(data);
      }
    })
  },

  destroy: function(req, res){
    Person.remove({name: req.params.name}, function(err, data){
      if(err){
        res.json(err);
      }
      else {
        Person.find({}, function(err, data){
          if(err){
            res.json(err);
          }
          else {
            res.json(data);
          }
        })
      }
    })
  },

  show: function(req,res){
    Person.find({name: req.params.name}, function(res, data){
      if(err){
        res.json(err);
      }
      else {
        res.json(data);
      }
    })
  }


} // end of module.exports
