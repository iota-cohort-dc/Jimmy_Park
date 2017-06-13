//-------------------------------------------------
var animals = require('../controllers/animals.js')
//-------------------------------------------------
module.exports = function(app){

  //<----Index---->
  app.get('/', function(req, res){
    animals.index(req, res);
  });
  //<----New---->
  app.get('/new', function(req, res){
    animals.new(req, res);
  });
  //<----Create---->
  app.post('/create', function(req, res){
    animals.create(req, res);
  });
  // <----Show---->
  app.get('/animals/:id', function(req, res){
    animals.show(req, res);
  });
  // <----Edit---->
  app.get('/:id/edit', function(req, res){
    animals.edit(req, res);
  });
  // <----Update---->
  app.post('/:id', function(req, res){
    animals.update(req, res);
  });
  //<----Delete---->
  app.post('/:id/delete', function(req, res){
    animals.destroy(req, res);
  });
}
