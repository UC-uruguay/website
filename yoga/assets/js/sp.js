function PageTopAnime() {
var scroll = $(window).scrollTop();
if (scroll >= 500){//上から
    $('.lp-fix').removeClass('down-move');
    $('.lp-fix').addClass('up-move');
} else {
    if($('.lp-fix').hasClass('up-move')){//すでにクラス名がついていたら
        $('.lp-fix').removeClass('up-move');
        $('.lp-fix').addClass('down-move');
    }
}
}
$(window).scroll(function () {
    PageTopAnime();
});
$(window).on('load', function () {
    PageTopAnime();
});