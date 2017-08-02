/**
 * Created by xiejiaxin on 2017/2/1.
 */
(function ($, document, window) {
    var utils =  {
        handlePageScroll: function(){
            function handleTopLink() {
                var $topLink = $('#btn-gotop');
                if($topLink.length){
                    // console.log($topLink);
                    if ($(this).scrollTop() > 100) {
                        $topLink.fadeIn();
                    } else {
                        $topLink.fadeOut();
                    }
                }
            }
            $(window).scroll(handleTopLink)
        },

        gotop: function() {
            $("#btn-gotop >a").on('click', function() {
                $("html, body").animate(
                    {scrollTop : 0}, 400
                );
                return false;
            });
        },


        showWeixin: function(){
            var $weixinBtn = $("#btn-wechat >a");
            $weixinBtn.find('.fa-weixin').mouseover(function(){
                $weixinBtn.find('div').fadeIn();
            });
            $weixinBtn.find('.fa-weixin').mouseout(function(){
                $weixinBtn.find('div').fadeOut();
            });
        },
        //
        // refreshCaptcha: function () {
        //     $('img.captcha').on('click', function(){
        //         // console.log("OKOKOKO");
        //         // console.log('click');
        //         var captcha_img = $(this);
        //         $.getJSON('/accounts/captcha/', function (res) {
        //             // console.log(captcha_img);
        //             captcha_img.attr('src', res['image_url']);
        //             $('#id_register-captcha_0').val(res['key']);
        //         });
        //     });
        // }
    };

    (function init() {
        utils.handlePageScroll();
        utils.gotop();
        // utils.autocomplete();
        utils.showWeixin();
        // utils.refreshCaptcha();
        $("#autocomplete").autocomplete({
            minLength:1,
            scroll: true,
            max:5,
            deferRequestBy: 5,
            noCache: true,
            source: function(request, response){
                $.ajax({
                    url: '/search/autocomplete',
                    dataType: 'json',
                    data: request,
                    success: function(data) {
                        response( data.results );
                    }
                })
            }
        });
        $(".content img").addClass('img-responsive');
    })();

}(jQuery, document, window));
