$(document).ready(function(){
    
    $('.category_list .category_item_all[cat="all"]').click(function(){
        $('.product-item').css("display", "block");
        // console.log('Select All')
    })
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
        
    })
    // $('.category_list .category_item').click(function(){
    //     var local = $(this).attr('tipoLocal');
    //     console.log(local);

    //     // Ocultando contenido
    //     $('.product-item').hide();

    //     // Mostrar contenido seleccionado
    //     $('.products-list .product-item[tipoLocal="'+local+'"]').show();
    // })
    // $('.category_list .category_item').click(function(){
    //     var grupo = $(this).attr('grupo');
    //     console.log(grupo);

    //     // Ocultando contenido
    //     $('.product-item').hide();

    //     // Mostrar contenido seleccionado
    //     $('.products-list .product-item[grupo="'+grupo+'"]').show();
    //     $("html, body").animate({ scrollTop: 0 }, 600);
    // })
    $('.btn-filtrar').click(function(){
        var cadena = $('.input-search').val();
        filtro = cadena.toUpperCase()
        console.log(filtro)
        var aux = $('a:contains("'+filtro+'")').closest('.product-item').attr('sucursal');
        $('.product-item').hide();
        $('.products-list .product-item[sucursal="'+aux+'"]').show();
        $('.input-search').val('');
        console.log(aux);

        
    })
    
});