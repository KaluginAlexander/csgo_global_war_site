$(document).ready(function () {
    
    // Вызов модалки
    $('.product').on('click', function(){

        // Выключение всего на сайте
        $('body').addClass('disable-body');
        $('.container').addClass('disable');
        
        // Вкл модалки
        $('.modal-window').css('display', 'flex')

        // Анимация
        $('.modal-window .content').fadeOut(0);
        $('.modal-window .content').fadeIn(300);

        // Заполнение productId
        let productId = $(this).data('id');
        $('#productId').val(productId);

    })

    // Обработка модалки
    $('#pay').on('click', function(){
        if ($('#nickname').val().length < 3) {
            $('.modal-window .content .error').text('Минимальная длина ника составляет 3 символа')
            return false;
        }
    })

    // Закрытие модалки
    $('.modal-window .cross').on('click', function(){

        // Выключение всего на сайте
        $('body').removeClass('disable-body');
        $('.container').removeClass('disable');
        
        // Вкл модалки
        $('.modal-window').css('display', 'none')
    })

    // При клике на кнопки в меню

    $('.menu .button').on('click', function() {

        // Получаем классы
        let classList = $(this).attr("class").split(/\s+/),
            dist;

        // Обрабатываем
        if (classList.includes('game')) {
            let link = document.createElement('a');
            link.href = 'https://vk.com/im?media=&sel=-201695936';
            link.click();
        }

        else if (classList.includes('about')) {
            dist = $(".content-block.about").offset().top;
        }

        else if (classList.includes('shop')) {
            dist = $(".content-block.shop").offset().top;
        }

        else if (classList.includes('faq')) {
            dist = $(".content-block.faq").offset().top;
        }

        // Скролл
        $([document.documentElement, document.body]).animate({
            scrollTop: dist - $('header').height() - 50
        }, dist / 2);

    })


    // Обработка клика по вопросу в FAQ
    $('.question-cb').change(function(){
        let element = $(this).get(0),
            questionID = $(this).data('id'),
            jqAnswer = $(`#answer-${questionID}`),
            answer = jqAnswer.get(0);

        answer.hidden = !element.checked;

        if (element.checked) {
            jqAnswer.fadeOut(0);
            jqAnswer.fadeIn(300);
        }
    })
});