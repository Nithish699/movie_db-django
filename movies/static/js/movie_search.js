// movie_search.js

$(document).ready(function(){
    $(".clickable-row").on("click", function(){
        window.location = $(this).data("href");
    });
});