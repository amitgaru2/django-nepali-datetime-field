$(document).ready(function() {
    $('input[type=nepali-date]').nepaliDatePicker({
        dateFormat: '%y-%m-%d',
        closeOnDateSelect: true,
        minDate: '१९७५-१-१',
        maxDate: '२१००-१२-३०'
    });
});