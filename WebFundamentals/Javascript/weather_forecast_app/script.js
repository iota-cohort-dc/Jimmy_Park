
$(document).ready(function() {
    $('form').submit(function() {
        // your code here (build up your url)
        var city = $('.search').val()

        $.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=da562d00c2de02b934c496eec0697c91", function(res) { //added &unit=imperial
            $('.city_box').html(res.name)
            $('.temp_box').html(res.main.temp + ' °F')
            console.log(res);
        }, 'json');
        return false;
    });
});


// this is the sample weather site for london // use this first to get your console.log to work  $.get('http://samples.openweathermap.org/data/2.5/find?q=London&units=imperial&appid=b1b15e88fa797225412429c1c50c122a1', function(res) {
