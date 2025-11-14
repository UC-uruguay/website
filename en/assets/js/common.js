//Swiper
const mySwiper = new Swiper('.lp-slide', {
    loop: true,
    slidesPerView: 1.8,
    speed: 5000,
    allowTouchMove: false,
    centeredSlides: true,
    autoplay: {
        delay: 0, // 途切れなくループ
    },
    breakpoints: {
		768: {
			slidesPerView: 4,
		},
        1000: {
			slidesPerView: 5,
		}
	}
});


//FAQ
$(function () {
    $(".lp-faq__a:not(:first-of-type)").css("display", "none");// 最初のコンテンツ以外は非表示
    $(".lp-faq__q:first-of-type").addClass("open");// 矢印の向きを変えておく
    $(".lp-faq__q").click(function () {
        $(".open").not(this).removeClass("open").next().slideUp(300);
        $(this).toggleClass("open").next().slideToggle(300);
    });
});

//fadeup
const targets = document.getElementsByClassName('fade-up');
for(let i = targets.length; i--;){
    let observer = new IntersectionObserver((entries, observer) => {
    for(let j = entries.length; j--;){
        if (entries[j].isIntersecting) {
            entries[j].target.classList.add('fade-active');
        } else{
            entries[j].target.classList.remove('fade-active');
        }
    }
    });
    observer.observe(targets[i]);
}

//page-top
$(function(){
    $('.page-top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 500);
        return false;
    });
});
$(window).on('load scroll', function(){
    if($(this).scrollTop() > 1) {
        $('.page-top').removeClass('down-move');
        $('.page-top').addClass('up-move');
    } else if($('.page-top').hasClass('up-move')) {
        $('.page-top').removeClass('up-move');
        $('.page-top').addClass('down-move');
    }
});
//スクロール
$('a[href^="#"]').click(function () {
    const speed = 500;
    const href = $(this).attr('href');
    const target = $(href == '#' || href == '' ? 'html' : href);
    const position = target.offset().top;
    $('html, body').animate({
        scrollTop: position
    }, speed, 'swing');
    return false;
});