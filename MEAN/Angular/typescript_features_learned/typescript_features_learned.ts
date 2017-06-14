
//
    let x: [string, number];
    x = ["hello", 10];

// myNum = 5;
    var myNum: number = 5;

// myString = "Hello Universe";
    var myString: string = "Hello Universe";

// myArr = [1,2,3,4];
    var arrayOfNumbers: Array<number> = [1,2,4,8,32];

// myObj = { name:'Bill'};
    var myObj: object = { name: 'Bill'};

// anythingVariable = "Hey";
    var anythingVariable: any = "Hey";
    var anythingVariable: any = 10;
    var anythingVariable: any = true;

// arrayOne = [true, false, true, true];
    var arrayOne: Array<boolean> = [true, false, true, true];

// arrayTwo = [1, 'abc', true, 2];
    var arrayTwo: (number|string|boolean|number)[] = [1, 'abc', true, 2];

// myObj = { x: 5, y: 10 };
    var myObj: object = { x: 5, y: 10 };

// object constructor
    MyNode = (function () {
        function MyNode(val) {
            this.val = 0;
            this.val = val;
        }
        MyNode.prototype.doSomething = function () {
            var _priv: number = 10;
            this._priv = 10;
        };
        return MyNode;
    }());

                // did not answer this yet
    class MyNode {
    val: number:

    constructor(val: number) {
        this.val = 0;
        this.val = val;
    }
    doSomethingFun() {
        this._priv = 3;
    }
    }
    let myNodeInstnace = new MyNode(1);
    console.log(myNodeInstnace.val);


// function myFunction() {
    console.log("Hello World");
    return;
    }

    function myFunction(): void {
        console.log("Hello World");
        return;
        }



// function sendingErrors() {
  	throw new Error('Error message');
    }

    function sendingErrors(message: string): never {
        throw new Error('Error message');
        }


















//
