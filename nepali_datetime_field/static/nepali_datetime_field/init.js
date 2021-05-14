var css = document.createElement('link');
css.rel='stylesheet';
css.href="https://unpkg.com/nepali-date-picker@2.0.1/dist/nepaliDatePicker.min.css";
css.crossorigin="anonymous";
document.getElementsByTagName('body')[0].appendChild(css);

var script = document.createElement('script');
script.src = "https://code.jquery.com/jquery-3.5.1.slim.min.js";
script.crossorigin = "anonymous";
script.onload = function() {
    var dpScript = document.createElement('script');
    dpScript.src="https://unpkg.com/nepali-date-picker@2.0.1/dist/jquery.nepaliDatePicker.min.js";
    dpScript.crossorigin = "anonymous";
    dpScript.onload = function() {
        $('input[type=nepali-date]').nepaliDatePicker({
            dateFormat: '%y-%m-%d',
            closeOnDateSelect: true,
            minDate: '१९७५-१-१',
            maxDate: '२१००-१२-३०'
        });
    }
    document.getElementsByTagName('body')[0].appendChild(dpScript);
}
document.getElementsByTagName('body')[0].appendChild(script);
