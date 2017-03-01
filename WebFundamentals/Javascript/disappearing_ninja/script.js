$(document).ready(function(){

  // $('img').click(function(){
  //     $(this).hide('slow');
  // });  dont need this anymore now that we added document.on

  $('button').click(function(){
      $('img').show();
  });

  $('#btn_start').click(function(){
      $('#ninja_div').append('<img src="ninja.jpg" alt="ninja">');
  });


    // $('#btn_start').click(function(){
    //   for(vari = 0; i < 5; i++)
    //   $('#ninja_div').append('<img src="ninja.jpg" alt="ninja">');

    $(document).on('click', 'img', function(){
      $(this).fadeOut();
    }); // this makes the dynamic





















});
