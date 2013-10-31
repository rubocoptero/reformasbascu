// Bootstrap jQuery plugins
require(['jquery', 'lib/jquery.stapel', 'lib/jquery.colorbox-min', 'bootstrap'], function ($) {
    $(document).ready(function() {
        // Bootstrap carousel
        $('.carousel').carousel({
          interval: 4000
        });

        // Bootstrap scrollspy
        $('[data-spy="scroll"]').each(function () {
            var $spy = $(this).scrollspy({
                offset: 50,
                refresh: 'refresh'
            });
        });

        // Bootstrap modal
        function getParameterByName(name) {
            name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
            var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
            results = regex.exec(location.search);
            return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
        }

        var action_value = getParameterByName('action');

        if (action_value !== "") {
            if (action_value === "gracias") {
                $('#graciasModal').modal();
            }
        }

        // AJAX images
        $.ajax({
            url: '/gallery',
            context: $('#tp-grid')
        }).done(function(data) {
            $(this).html(data);
            
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
                    // Colorbox
                    setTimeout(function(){
                        var root = ".group-";
                        var i = 1;

                        var colorboxFactory = function(groupName) {
                            return function() {
                                $(groupName).colorbox({
                                    rel:groupName,
                                    slideshow:true,
                                    maxWidth: '95%',
                                    maxHeight: '95%'
                                });
                            };
                        };

                        while($(groupname = root + i++).length !== 0)
                        {
                            $(groupname + "-parent").last()
                                .one("click", colorboxFactory(groupname));
                        }
                    }, 0);
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
        });
    });
});
