/* ********** Our Node Class **********
Generates a node for a singly linked list
parameters:
  val: a numerical value
private variables/functions:
  none:
public properties/methods:
  val: val;
  next: // another Node or null
  passThis: a function that passes a console log of this and self.
************** END **********   */
var Node = function(val){
  this.val = val;
  this.next = null;
}
Node.prototype.passThis = function(custom_return){
  console.log(this, "this");
  console.log(this.self, "self");
  console.log(custom_return, "My Return");
  return custom_return;
}
// ****************** END OF NODE ******************
/* ************* Singly Linked List Class (SingleList) *****************
Creates a simple singly linked list class with not too many methods yet!
parameters: none
private: none
public properties:
  head: first node in the List
public methods:
  add: adds a new node based on a value passed in. returns this
  dequeue: removes the head, and gives it to a callback, if a callback is passed. returns this
  remove_tail: removes the tail, and gives it to a callback as an argument, only if a callback is passed. returns this.
************** END **********   */
var SingleList= function(){
  this.head = null;
}
SingleList.prototype.add = function (val) {
  if (!this.head){
    this.head = new Node(val);
    return this;
  }
  var current = this.head;
  while(current.next){
    current = current.next;
  }
  current.next = new Node(val);
  return this;
};
SingleList.prototype.dequeue = function (callback) {
  var eliminatedNode = this.head;
  this.head = this.head.next;
  eliminatedNode.next = null;
  if (typeof(callback)=='function'){
    callback(eliminatedNode);
  }
  //console.log(this.head); optional
  return this;
};
// Write a remove tail! :)
// ************************ END OF LIST ************************
sList = new SingleList();
sList.add(1).add(2).add(3).add(4).head.next.passThis(sList).dequeue(
  function callback(myNode){
    console.log(myNode.val, "CHAINING INSANITY!");
  })
  .dequeue(
    function anotherCallback(myNode){
      console.log("******************************");
      console.log('Seriously, Stop!', myNode);
    });
