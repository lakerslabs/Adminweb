$(window).on("scroll", function() { 
    var nav = $('#container-floating');

    if ($(this).scrollTop() < 250 ||$(window).scrollTop() + $(window).height() > $(document).height() - 420 ) {
        nav.removeClass("mostrar");
     // alert("1");
    
      }else {
      nav.addClass("mostrar");

    }
});