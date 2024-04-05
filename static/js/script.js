document.addEventListener('DOMContentLoaded', function() {
    var subDiv = document.getElementById('sub');
    var logo = document.getElementById('logo');

    function setCursor(element) {
        element.addEventListener('mouseenter', function() {
            element.style.cursor = 'pointer';
        });

        element.addEventListener('mouseleave', function() {
            element.style.cursor = 'default';
        });
    }

    function setClickEvent(element, url) {
        element.addEventListener('click', function() {
            window.location.href = url;
        });
    }

    setCursor(logo);
    setClickEvent(logo, '/');

    setCursor(subDiv);
    setClickEvent(subDiv, 'https://www.whatsapp.com/channel/0029VaC8d1M3AzNVm4DlYk2H');
});
