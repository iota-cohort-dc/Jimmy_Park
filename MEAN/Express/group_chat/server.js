var express = require('express');
var app = express();
var path = require('path');
var users = [];
// app.use(express.static(path.join()__dirname + "views"))
app.set('views', path.join(__dirname, "./views"));
app.set('view engine', 'ejs');

app.get('/', function(req, res){
  res.render('index')
})

var server = app.listen(8000, function(){
  console.log('server running at port 8000');
});

var io = require('socket.io').listen(server);

io.sockets.on("connection", function(socket){
  socket.on("send_user_name", function(data){
    users.push({id: socket.id, name: data.name});
    var names_arr = users.map(function(x){
      return x.name
    })
    socket.emit("send_user_name", {current_user:users[users.length - 1], all_users:names_arr}
    )
    })
    socket.on("send_message", function(data){
      var sender = users.find(function(x){
        return x.id == data.sender
      })
      data.sender = sender.name;
      console.log(data)
      io.emit("send_message", data)
    })
    socket.on("disconnect", function(){
      var index = users.findIndex(function(x){
        return x.id == socket.id
      })
      if(index >=0){
        users.splice(index, 1);
        var names_arr = users.map(function(x){
          return x.name
        })
        io.emit("user_left", {users: names_arr})
    }
  })
})
