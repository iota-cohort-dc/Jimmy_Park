  $(document).ready(function() {
      $('form').submit(function() {
          // your code here (build up your url)
          var city = $('.search').val()
          $.get('http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=da562d00c2de02b934c496eec0697c91', function(res) {
              $('.city_box').html(res.name)
              $('.temp_box').html(res.object.temp)            // your code here
              console.log(res);
          }, 'json');
          // don't forget to return false so the page doesn't refresh
          return false;
      });
  });
