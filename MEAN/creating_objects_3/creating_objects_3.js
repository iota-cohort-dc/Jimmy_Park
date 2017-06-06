function VehicleConstructor(name, wheels, passengers,speed){
  if (!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name,wheels,passengers, speed);
  };
  // properties
  this.distance_travelled = 0;
  this.name = name || unicycle;  //  the || are the ((or)). if name isnt specified, unicycle will be defalt
  this.wheels = wheels || 1;
  this.passengers = passengers;
  this.speed = speed;
  // methods
  VehicleConstructor.prototype.makeNoise = function(noise){
    this.noise = noise || "Honk Honk";
    return this;
  };
  VehicleConstructor.prototype.udpateDistanceTravelled = function(){
    this.distance_travelled += self.speed;
    console.log(this.distance_travelled);
    return this;
  };
  VehicleConstructor.prototype.move = function(){
    this.makeNoise();
    this.updateDistanceTravelled();
    return this;
  };
  VehicleConstructor.prototype.checkMiles = function(){
    console.log(this.distance_travelled);
    return this;
  };
};

var unicycle =  new VehicleConstructor(); //

var bus = new VehicleConstructor("SchoolBus",6,20);
  bus.pickupPassengers = function(newPassengers){
    bus.passengers += newPassengers;
  };
var sedan = new VehicleConstructor("Camry",4,5);
  sedan.makeNoise = function(){
    console.log("Honk,Honk");
  };
var mtbike = new VehicleConstructor("diamond back", 2, 1);
  mtbike.makeNoise = function(){
    console.log("ring,ring!");
  };
var bike = new VehicleConstructor("haro",2,1);
  bike.makeNoise = function(){
    console.log("beep, beep");
  };
var roadBike = new VehicleConstructor("Schwin",2,1);
  roadBike.makeNoise = function(){
    console.log("quack, quack");
  };

var car = new VehicleConstructor('car', 4, 2, 40);
// car.move();
console.log(car.checkMiles());
console.log(car.speed);
