var express      =  require('express'),
    path         = require('path'),
    mongoose     = require('mongoose'),
    bodyParser   = require('body-parser'),
    port         = 8000,
    app          = express();

// Express basic setup
app.use(bodyParser.urlencoded({ extended: true}));
app.use(express.static(path.join(__dirname, './statc')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

// Connect to db
mongoose.connect('mongodb://localhost/message_board');

// Need Schema variable
var Schema = mongoose.Schema;

// Create Message Schema
var MessageSchema = new Schema({
  name: {type: String, required: true, minlength: 4},
  content: {type: String, required: true},
  comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
}, {timestamps: true});

// Create Comments Schema
var CommentSchema = new Schema({
  _message: {type: Schema.Types.ObjectId, ref: 'Message'},
  name: {type: String, required: true, minlength: 4},
  content: {type: String, required: true}
}, {timestamps: true});

// Register Models
var Message = mongoose.model('Message', MessageSchema);
var Comment = mongoose.model('Comment', CommentSchema);


// ROUTES
app.get('/', function(req, res){
  Message.find({})  //.populate('comments')
  .populate('comments')
  .exec(function(err, results){
    if (err){
      console.log(err);
    };
    console.log(results);
    res.render('index', { messages: results });
  });
});

app.post('/messages', function(req, res){
  Message.create(req.body, function(err, result){
    if (err){
      console.log(err);
      res.redirect('/');
    };
  })
});

app.post('/messages/:id/comments', function(req, res){
  // find message the comment will belong to
  // req.params is pulling from the url
  Message.findOne({_id: req.params.id}, function(err, message){
    // create a comment using data from the form
    var comment = new Comment(req.body);
    // set the reference like this
    comment._message = message._id;
    // the comment now belongs to the message we found above
    // now, save both to the db
    comment.save(function (err){
      // push the comment into the comments array of the message we found
      message.comments.push(comment);
      // save the updated message
      message.save(function (err){
        if (err){
          console.log(err);
        }
        else {
          res.direct('/');
        }
      });
    });
  });
});


// Setting our server to listen to port
app.listen(8000, function(){
  console.log('listening on port', port);
});
