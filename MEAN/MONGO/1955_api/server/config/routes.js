//1955_api
//-------------------------------------------------
var people = require('../controllers/people.js')
//-------------------------------------------------
module.exports = function(app){

    //<----Index---->
    app.get('/', function(req, res){
      people.index(req, res);
    });
    //<----New---->
    app.get('/new/:name/', function(req, res){
      people.create(req, res);
    });
    //<----Create---->
    app.get('/remove/:name', function(req, res){
      people.destroy(req, res);
    });
    // <----Show---->
    app.get('/:name', function(req, res){
      people.show(req, res);
    });
    // // <----Edit---->
    // app.get('/:id/edit', function(req, res){
    //   people.edit(req, res);
    // });
    // // <----Update---->
    // app.post('/:id', function(req, res){
    //   people.update(req, res);
    // });
    // //<----Delete---->
    // app.post('/:id/delete', function(req, res){
    //   people.destroy(req, res);
    // });
  }
