function Node(val){
	this.val = val;
	this.head = null;
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

var luisList = new SLL()
luisList.addFront(5).addFront(10).addFront(-15).addFront(20)
console.log(luisList.head)

luisList.removeNegatives();
console.log("NEWLIST",luisList.head)


// in terminal // node file_name.js
