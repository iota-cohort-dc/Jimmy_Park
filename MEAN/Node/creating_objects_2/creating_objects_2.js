function VehicleConstructor(name, wheels, passengers,speed){
  if (!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name,wheels,passengers, speed);
  };
  // private
  var distance_travelled = 0;
  var self = this;
  function updateDistanceTravelled(){
    distance_travelled += self.speed;
    console.log(distance_travelled);
  };
  // properties
  this.name = name;
  this.wheels = wheels;
  this.passengers = passengers;
  this.speed = speed;
  // methods
  this.makeNoise = function(noise){
    this.noise = noise || "Honk Honk";
    console.log(noise);
  };
  this.move = function(){
    this.makeNoise();
    updateDistanceTravelled();
  };
  this.checkMiles = function(){
    console.log(distance_travelled)
  };
};

var unicycle =  new VehicleConstructor();

var bus = new VehicleConstructor("SchoolBus",6,20);
  bus.pickupPassengers = function(newPassengers){
    bus.passengers += newPassengers;
  }

var sedan = new VehicleConstructor("Camry",4,5);
  sedan.makeNoise = function(){
    console.log("Honk,Honk");
  }

var mtbike = new VehicleConstructor("diamond back", 2, 1);
  mtbike.makeNoise = function(){
    console.log("ring,ring!");
  }

var bike = new VehicleConstructor("haro",2,1);
  bike.makeNoise = function(){
    console.log("beep, beep");
  }

var roadBike = new VehicleConstructor("Schwin",2,1);
  roadBike.makeNoise = function(){
    console.log("quack, quack");
  }

  // console.log(bus.passengerNumber);
  // bus.pickupPassengers(6);
  // console.log(bus.passengerNumber);

  var car = new VehicleConstructor('car', 4, 2, 40);
  car.move();
  car.checkMiles();
  console.log(car.speed);
