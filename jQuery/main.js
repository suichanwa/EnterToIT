$(function(){
    $("#btn1").click(function(){ 
        $(this).css('background-color', 'red');
        alert('Мир jQuery');
    });
});

$(function(){
    $("#tab .some").css('background-color', 'silver');

});

$(function(){
    $(".open", "div#menu").css("background-color", "red");
});


$(function(){
    var array = $("tr:even").slice(1,4);
    array.eq(1).css('background-color', 'red');

    //last and frist element
    
    var firstEl = array.first();

    //console.log("first elem: " + firstEl.html());
    var lastEl = array.last();

    //console.log("end elem: " + lastEl.html());

    for(var i=0;i<array.length;i++){
        console.log(i.toString()+". " + array[i].innerHTML);
    }

    var ularray = $('li').map(function(index,elem){
        return $(elem).children()[0];
    })

    ularray.each(function (index,elem) {
        console.log(elem.innerHTML);
    })

    ularray.css('background-color', 'silver');
});

$(function(){
    console.log($('body').css('font-size'));
    // поиск по селектору
    var array0 = $('ul').find('.submenu');
    array0.css('background-color', 'silver');
     
    // поиск по элементу
    // получаем первый элемент выборки
    var elem = $('ul.submenu')[0];
    var array1= $('ul').find(elem);
    array1.css('background-color', 'gray');
     
    // Поиск объекта jQuery
    var jQueryObject = $('ul.submenu');
    var array2= $('ul').find(jQueryObject);
    array2.css('color', 'blue');
    $('a').first().removeAttr('herf');


});

$("input")
.change(function() {
var $input = $(this);
    $( "p" ).html( ".attr( 'checked' ): <b>" + $input.attr( "checked" ) + "</b><br>" +
    ".prop( 'checked' ): <b>" + $input.prop( "checked" ) + "</b><br>" +
    ".is( ':checked' ): <b>" + $input.is( ":checked" ) + "</b>" );
    })
.change();

$(function(){
    //replace one element with another element

    $('li.lang').first().before('<li class="lang">JavaScript</li>'); 
    $('li.lang').last().after($('li.lang').last().clone().html('Visual Basic'));
    $('li.lang').first().replaceWith('<li class="lang">someshit</li>');
});


//efects

$(function() {
    $('button#show').click(function(){
        $('ul').show();
    });
    $('button#hide').click(function(){
        $('ul').hide();
    });

    $('button').click(function(){
        $('ul').toggle();
    });
});

$(function(){
    var current = $("div%langs p").first();
    $('#next').click(function(){
          $(current().not('.last').hide("fast", function(){
                current = $(current).next('p');
                $(currnet).show("fast");
          }));
    });
    $('#prev').click(function(){
        $(current().not('.last').hide("fast", function(){
              current = $(current).prev('p');
              $(currnet).show("fast");
        }));
  });
});

//slide realistaion

$(function(){
    $('#slideUp').click(function(){
         $(this).slideUp();
         $(this).slideToggle('slow');
    });
    $('#slideDown').click(function(){
         $('#slideUp').slideDown();
         $('#slideUp').slideToggle(2000);
    });
});

$(function () { 
    $('#ars').click(function(){
        $('#fadeIn').click(function(){
            $('#ars').fadeIn('slow', function(){alert('Отображено');});
        });
    })
    
    $('#fadeOut').click(function(){
        $('#ars').fadeOut(2000, function(){alert('Скрыто');});
   });
})

//fade

$(function(){
   $('#ars').fadeTo(500,0.6);

   $('#fadeIn').click(function(){
        $('#ars').fadeIn('slow', function(){alert('Отображено');});
    });

    $('#fadeOut').click(function(){
        $('#ars').fadeOut(2000, function(){alert('Скрыто');});
   });
});

//animate method

$(function(){
    $('#anim').click(function(){
        $('#ars').animate({
            opacity:0.25,
            'margin-right': '50',
            'margin-left': '+=50',
            width: '-=10',
            height: '200'
            },{
                duration: 1000,
                step:function(now, fx){
                    var data = fx.elem.ud + '' + fx.prop + ': ' + now;
                    $('body').append('<div>' + data + '</div>');
                },
                complete: function(){
                    console.log("animatio was ended");
                }
            }
        );
    })
})

