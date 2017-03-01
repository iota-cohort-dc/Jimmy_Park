var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]





function output(){
  for (var i = 0; i < students.length; i++){
    console.log(students[i].first_name + " " + students[i].last_name);
  }
}
output();

// function output(){
//   for(var i = 0; i < students.length; i++){
//     console.log(students[i].first_name + " " + students[i].last_name);
//   }
// }
// output();
//

// function nameOutput (){
//   for (var i = 0 ; i < students.length ; i++){
//   console.log(students[i].first_name + " " + students[i].last_name);
//   }
// }
// nameOutput();

// var users = {
//  'Students': [
//      {first_name:  'Michael', last_name : 'Jordan'},
//      {first_name : 'John', last_name : 'Rosales'},
//      {first_name : 'Mark', last_name : 'Guillen'},
//      {first_name : 'KB', last_name : 'Tonel'}
//   ],
//  'Instructors': [
//      {first_name : 'Michael', last_name : 'Choi'},
//      {first_name : 'Martin', last_name : 'Puryear'}
//   ]
//  }
