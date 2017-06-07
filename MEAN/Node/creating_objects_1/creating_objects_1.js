function VehicleConstructor(name, wheels, passengers){
  var vehicle = {};

  // properties
  vehicle.name = name;
  vehicle.wheels = wheels;
  vehicle.passengers = passengers ;

  // methods
  vehicle.makeNoise = function(noise){
    var noise = noise || "Honk Honk";
    console.log(noise);
  }
  return vehicle;
}
var unicycle = VehicleConstructor();

var bus = VehicleConstructor("SchoolBus",6,20);
  bus.pickupPassengers = function(newPassengers){
    bus.passengers += newPassengers;
  }

var sedan = VehicleConstructor("Camry",4,5);
  sedan.makeNoise = function(){
    console.log("Honk,Honk");
  }

var mtbike = VehicleConstructor("diamond back", 2, 1);
  mtbike.makeNoise = function(){
    console.log("ring,ring!");
  }

var bike = VehicleConstructor("haro",2,1);
  bike.makeNoise = function(){
    console.log("beep, beep");
  }

var roadBike = VehicleConstructor("Schwin",2,1);
  roadBike.makeNoise = function(){
    console.log("quack, quack");
  }

  console.log(bus.passengerNumber);
  bus.pickupPassengers(6);
  console.log(bus.passengerNumber);
