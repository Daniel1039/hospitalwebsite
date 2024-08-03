(function($){
    'use strict'

    $(window).on("load", function(){
		$(".preloader").fadeOut();
	});

    $('.navigation').meanmenu({
        'meanMenuContainer' : '.mobile-nav',
        'meanScreenWidth'   : '768',
        'meanMenuClose'     : '<i class="fas fa-times"></i>',
        'meanMenuOpen'      : '<span></span><span></span><span></span>'
    });

    // Sticky Navigation Bar
    $(window).scroll(function(){
        var scrollHeight = $(document).scrollTop();
        if(scrollHeight > 106){
            $('.primary-nav').addClass('navigation-fixed');
        }else{
            $('.primary-nav').removeClass('navigation-fixed');
        }
        // Scroll to Top
        if(scrollHeight > 106){
            $('.scrolltotop').fadeIn();
        }else{
            $('.scrolltotop').fadeOut();
        }
    });

    $(".scrolltotop a").click(function(event){
        $("html").animate({scrollTop:$("body").offset().top}, "1000");
        event.preventDefault();
    });
}(jQuery))