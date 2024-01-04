tinymce.init({selector:'textarea'})
function toggleTheme() {
    let element = document.body;
    let themeIcon = document.getElementById('themeIcon');

    if (element.dataset.bsTheme === 'light') {
        element.dataset.bsTheme = 'dark';
        themeIcon.classList.remove('bi-moon');
        themeIcon.classList.add('bi-sun'); // Switch to sun icon in dark mode
    } else {
        element.dataset.bsTheme = 'light';
        themeIcon.classList.remove('bi-sun');
        themeIcon.classList.add('bi-moon'); // Switch to moon icon in light mode
    }
}

$(document).ready(function () {
    $('#id_email').on('input', function () {
        var email = $(this).val().trim();
        $.ajax({
            type: 'GET',
            url: '/check_email_availability/',
            data: {'email': email},
            success: function (response) {
                if (response.available) {
                    $('#emailAvailability').text('');
                } else {
                    $('#emailAvailability').text('Email is already taken.');
                }
            }
        });
    });
});