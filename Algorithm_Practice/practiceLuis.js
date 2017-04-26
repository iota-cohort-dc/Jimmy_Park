function Node(val){
	this.val = val;
	this.next = null;
}
function SLL(){
	this.head = null;
	this.addFront = function(val){
		var node =  new Node(val);
		if(!this.head){    		//or can say if(this.head == null)
			this.head = node;
			return this;
		}
		else{
			node.next = this.head;
			this.head = node;
			return this;
		}
	}
	this.removeNegatives = function(){
		if(!this.head){
			return False;
		}
		if(this.head.val < 0){
			this.head = this.head.next;
			current = this.head;
		}
		while(current){
			if(current.next.val < 0){
				current = current.next.next;
			}
			current = current.next;
		}
		if(current.next == null){
			return this
		}
	}
	return this;
	// new function here
}
function dedup (list){
  if(!list.head){
    return False;
  }
  var current = list.head;
  var current2 = current.next;
  while(current != null){
    while(current2 != null){
      if(current.val == current2.val){
        current.next = current2.next;
        current2.next = null;
      }
    }
    current = current.next;
  }
  return list;
}

var luisList = new SLL();
luisList.addFront(5).addFront(10).addFront(-15).addFront(20);
// console.log(luisList.head)
console.log(dedup(luisList));













// luisList.removeNegatives();
// console.log("NEWLIST",luisList.head)


// in terminal // node file_name.js
