    $(document).ready(function(){

        $('#clickMe').click(function(){
          alert('hello');
        });


        $('#button1').click(function(){
          $('#button1').hide('slow');
        });


        $('#hideMe').click(function(){
          $('#clickMe').hide('slow');
        });

        // $('#showMe').(function(){
        //   $('#button1').show('slow');
        // });

        $('#toggleMe').click(function(){
          $('#toggleMe').toggle('slow', function(){
          });
        });
//
        $('#slideDownMe').click(function(){
          $('#slideDownMe').slideDown('slow', function(){
          });
        });
//
        $('#slideUpMe').click(function(){
          $('#slideUpMe').slideUp('slow', function(){
          });
        });


        $('#slideToggleMe').click(function(){
          $('#slideToggleMe').slideToggle('slow', function(){
          });
        });

        $('#fadeInMe').click(function(){
          $('#fadeInMe').fadeIn('slow', function(){
          });
        });

        $('#fadeOutMe').click(function(){
          $('#fadeOutMe').fadeOut('slow', function(){
          });
        });
//
        $('#addClassMe').click(function(index){
          $('#sometext').addClass('intro')
        });


        $('#beforeMe').click(function(){
          $('#textHere').before('This text is from the  script file')
        });

        $('#afterMe').click(function(){
          $('#afterMe').after('<b>This is a new line from the script file.</b>')
        });

        $('#appendMe').click(function(){
          $('#appendMe').append('<b>This is a new line from the script file.</b>')
        });

        $('#htmlMe').click(function(){
          $('#htmlMe').html('<p> this is a replacemtne text....</p>');
        });

        // $('#attrMe').click(function(){
        //   $('#attrMe').attr('title','was written by');
        // });


        $('#val').click(function(){
          $('input:text').val('Glenn');
        });

        // $('').(function(){
        //   $('')('')
        // });

        // $('').(function(){
        //   $('')('')
        // });

























    });
