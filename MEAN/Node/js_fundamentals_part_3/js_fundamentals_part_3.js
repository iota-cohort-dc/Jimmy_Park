var person = {
  name: "jimmy",
  distance_traveled: 0,
  say_name: function(){
    console.log(person.name);
  },
  say_something: function(phrase){
    console.log(person.name, "says:", phrase);
  },
  walk: function(){
    person.distance_traveled += 3;
    console.log("Walked",person.distance_traveled)
    return person;
  },
  run: function(){
    person.distance_traveled += 10;
    console.log("Ran", person.distance_traveled)
    return person;
  },
  crawl: function(){
    person.distance_traveled += 1;
    console.log("Crawled", person.distance_traveled)
    return person;
  }
}
person.say_something('I am cool');
person.say_name();
person.walk();
person.run();
person.crawl();


function ninjaConstructor(name, cohort){
  var ninja = {}
  var belts = ["yellow", "red", "black"]
  ninja.name = name;
  ninja.cohort = cohort;
  ninja.beltLevel = 0;
  ninja.levelUp = function(){
    if (ninja.beltLevel < 2){
      ninja.beltLevel += 1;
      ninja.belt = belts[ninja.beltLevel];
    }
    return ninja
  }
  ninja.belt = belts[ninja.beltLevel];
  return ninja;
}
