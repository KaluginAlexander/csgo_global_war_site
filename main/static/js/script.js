$(document).ready(function () {
    
    // Вызов модалки
    $('.product').on('click', function(){

        // Выключение всего на сайте
        $('body').addClass('disable-body');
        $('.container').addClass('disable');
        
        // Вкл модалки
        $('.modal-window').css('display', 'flex')

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


});