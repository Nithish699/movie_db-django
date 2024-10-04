// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    var moreInfoBtn = document.getElementById('more-info-btn');
    var moreInfoDiv = document.getElementById('more-info');

    moreInfoBtn.addEventListener('click', function() {
        if (moreInfoDiv.style.display === 'none') {
            moreInfoDiv.style.display = 'block';
            moreInfoBtn.textContent = 'Less Info';
        } else {
            moreInfoDiv.style.display = 'none';
            moreInfoBtn.textContent = 'More Info';
        }
    });
});
