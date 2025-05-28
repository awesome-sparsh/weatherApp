function validateAndSubmit() {
    const location = $('#location').val().trim();
        if (location === '') {
        $('#location-error').text('Please enter a city name, country name or city, country.').removeClass('hidden');
    } 
    else {
        $('#location-error').addClass('hidden').text('');
        $('#weather-form').submit();
    }
}