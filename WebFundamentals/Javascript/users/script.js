

//
// function #####()
// {
//   $().click(function(){
//     $()...('');
//   });
// }

  $(document).ready(function(){

    $('button').click(function(){
      var fname = $('#f_name').val()
      var lname = $('#l_name').val()
      var email = $('#email').val()
      var phone = $('#phone').val()

      // $('#f_name').val('')

      $('#table').append(
        `<tr><td>${fname}</td><td>${lname}</td><td>${email}</td><td>${phone}</td>`


      );
    });

});
