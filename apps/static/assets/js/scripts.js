$(document).ready(function(){
    
    $('.category_list .category_item_all[cat="all"]').click(function(){
        $('.product-item').css("display", "block");
        $('.input-search').val('');
        // console.log('Select All')
    });
    $('.category_list .category_item').click(function(){
        var canal = $(this).attr('category');
        console.log(canal);
        var grupo = $(this).attr('grupo');
        console.log(grupo);
        var local = $(this).attr('tipoLocal');
        console.log(local);
        // Ocultando contenido
        $('.product-item').hide();

        // Mostrar contenido seleccionado
        $('.products-list .product-item[category="'+canal+'"]').show();
        $('.products-list .product-item[tipoLocal="'+local+'"]').show();
        $('.products-list .product-item[grupo="'+grupo+'"]').show();
        $("html, body").animate({ scrollTop: 0 }, 300);
        
    });
    
    
    $('.input-search').keyup(function(){
        var nombres = $('.username');
        var buscando = $(this).val();
        var item='';
        for( var i = 0; i < nombres.length; i++ ){
            item = $(nombres[i]).html().toLowerCase();
            for(var x = 0; x < item.length; x++ ){
                if( buscando.length == 0 || item.indexOf( buscando ) > -1 ){
                    $(nombres[i]).parents('.product-item').show(); 
                }else{
                        $(nombres[i]).parents('.product-item').hide();
                }
            }
        }
    });
});