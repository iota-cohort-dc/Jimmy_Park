
  // $(document).on('click','#btn',function contact_card(){



$(document).ready(function(){

          // $(document).on('click','button' function(){

          $('button').click(function(){
              var fname = $('#f_name').val()
              var lname = $('#l_name').val()
              var descript = $('#description').val()
              // console.log(fname, lname);
              $('#right').append(
              `<h1 id="id_card">${fname} ${lname} <br><p><button id="click_for_descrip" type="button" name ="button">Click for description</button></h1>`)
              $('#right').append(`<p id="poop">${descript}</p>`)

          });

          $(document).on('click','#id_card', function(){
            $(this).hide('slow')
            $('#poop').show('slow')
          });


})
