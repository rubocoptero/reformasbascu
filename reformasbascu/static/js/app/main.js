// Bootstrap jQuery plugins
require(['jquery', 'lib/jquery.stapel', 'lib/jquery.colorbox-min', 'bootstrap'], function ($) {
    $(document).ready(function() {
        // Bootstrap
        $('.carousel').carousel({
          interval: 4000
        });

        // Stapel
        $( '#close' ).hide();

        var $grid = $( '#tp-grid' ),
          $name = $( '#name' ),
          $close = $( '#close' ),
          $loader = $( '<div class="loader"><i></i><i></i><i></i><i></i><i></i><i></i><span>Loading...</span></div>' ).insertBefore( $grid ),
          stapel = $grid.stapel( {
            delay : 50,
            onLoad : function() {
              $loader.remove();
            },
            onBeforeOpen : function( pileName ) {
              $name.html( pileName );
              $close.show();
            },
            onAfterOpen : function( pileName ) {
              $close.show();
            }
          } );

        $close.on('click', function() {
          $close.hide();
          $name.empty();
          stapel.closePile();
        });

        // Colorbox
        setTimeout(function(){
            var root = ".group-";
            var i = 1;

            while($(groupname = root + i++).length !== 0)
            {
                $(groupname).colorbox({rel:groupname, slideshow:true});
            }
        }, 0);

        $('[data-spy="scroll"]').each(function () {
            var $spy = $(this).scrollspy({
                offset: 50,
                refresh: 'refresh'
            });
        });
    });
});
