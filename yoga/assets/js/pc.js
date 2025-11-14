$(window).on('load scroll', function(){
    var headerH = $('#header').outerHeight(true);
    var scroll = $(window).scrollTop();
    if (scroll >= headerH){
        $('#header').addClass('header-fix');
    }else{
        $('#header').removeClass('header-fix');
    }
});