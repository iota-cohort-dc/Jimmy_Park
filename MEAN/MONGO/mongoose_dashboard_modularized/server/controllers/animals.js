var mongoose = require('mongoose');
var Animal = mongoose.model('Animal');

module.exports = {

  index: function(req, res){
    Animal.find({}, function(err, results){
      if (err){
        console.log(err)}
        res.render('index',{animals: results});
    });
  },

  new: function(req, res){
    console.log('Its Getting /animal/new route function');
    res.render('new');
  },

  create: function(req, res){
    Animal.create(req.body, function(err, results){
      if (err){
        console.log(err);}
        res.redirect('/');
    });
  },

  show: function(req, res){
    Animal.find({ _id: req.params.id }, function(err, response){
      if (err){
        console.log(err);}
        res.render('show', {animal: response[0] });
      });
    },

  edit: function(req, res){
    Animal.find({ _id: req.params.id }, function(err, response){
      if (err){
        console.log(err);}
        res.render('edit', { animal: response[0] });
    });
  },

  update: function(req, res){
    Animal.update({ _id: req.params.id }, req.body, function(err, result){
      if (err){
        console.log(err);}
        res.redirect('/');
    });
  },

  destroy: function(req, res){
    Animal.remove({ _id: req.params.id}, function(err,result){
      if (err){
        console.log(err);};
        res.redirect('/');
    });
  }
}
