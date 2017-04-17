
function Node(val){
	this.val = val;
	this.head = null;
}
function SLL(){
	this.head = null;
	this.addFront = function(val){ // addFront
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
  // ADD NEW FUNCTION HERE!
	this.back = function(){   // back
		if(!this.back){
			return False;
		}
		current = this.head;
		while(current){
			if(current.next == null){
				return current.val;
			}
			current = current.next
		}
	}
}




var luisList = new SLL(); //creates a new list
luisList.addFront(5).addFront(10).addFront(15).addFront(20); //adds values to list
console.log(luisList.head); //logging new list

console.log(luisList.back());
// in terminal // node file_name.js


// *****************************************************************************
// *****************************************************************************


//<-------------------------------- Back ------------------------------------->
function Node(val){
	this.val = val;
	this.head = null;
}
function SLL(){
	this.head = null;
	this.back = function(val){
		if(!this.back){
			return False;
		}
		current = this.head;
		while(current){
			if(current.next == null){
				return current.val;
			}
			current = current.next
		}
	}
}
//<----------------------------- Remove Back --------------------------------->

//<------------------------------- Add Back ---------------------------------->
  // this.addBack = function(val){
  //   var lastNode = new Node (val)
  //   if(!this.head){
  //     this.head = lastNode;
  //     return this;
  //   }
  //   var current = this.head
  //   while(current.next){
  //     current = current.next
  //   }
  //   current.next = lastNode;
  //   return this;
  // }
