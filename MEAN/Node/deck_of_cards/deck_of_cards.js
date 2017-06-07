//<------------------------- deck of cards -------------------------->

function DeckConstructor(){
    var suits = ["Hearts", "Spades", "Clubs", "Diamonds"];
    var values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];
    var deck;    // = [];

    this.showDeck = function(){
        console.log(deck);
        console.log("Length:", deck.length);
    }
    var generateDeck = function(){
        deck = [];
        for (var i=0; i < suits.length; i++){
            for (var j=0; j<values.length; j++){
                var card = {};
                card.suit = suits[i];
                card.value = values[j];
                deck.push(card);
            }
            // var card = new Card(suits[i], value[j]);
            // deck.push(card);
        }
        return this;
    }
    generateDeck();

    this.shuffle = function(){
        var numberOfShuffles = Math.floor((Math.random() * 100 ) + 50);
        for (var i = 0; i <= numberOfShuffles; i++){
            var randomInteger1 = Math.floor(Math.random() * deck.length);
            var randomInteger2 = Math.floor(Math.random() * deck.length);
            var temp = deck[randomInteger1];
            deck[randomInteger1] = deck[randomInteger2];
            deck[randomInteger2] = temp;
        }
        return this; // this is the deck object // this you can chain methods
    }
    this.reset = generateDeck;

    // this.getDeck = function(){
    //   return deck;
    // }
    this.deal = function(){
        return deck.pop();
    // DeckConstructor.prototype.deal = function(){
    //  return this.deck.pop();
    // }
    }
}
function PlayerConstructor(name){
    this.name = name;
    this.hand = [];
}
PlayerConstructor.prototype.takeCard = function(deck){
    var card = deck.deal();
    this.hand.push(card);
    return this;
}




// function Card(suit,value){   // constructor
//   this.suit = suit;
//   this.value = value;
// }

var myDeck = new DeckConstructor();

myDeck.shuffle().show();
myDeck.shuffle().reset();
myDeck.show();

console.log(myDeck.deal());
