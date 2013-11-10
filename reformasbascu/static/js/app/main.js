// Bootstrap jQuery plugins
require([
    'lib/cookie-consent.min',
    'lib/jquery.stapel',
    'lib/jquery.colorbox-min',
    'bootstrap'
    ],
    function () {
    $(document).ready(function() {
        // Begin Cookie Consent plugin by Silktide - http://silktide.com/cookieconsent
            // <![CDATA[
            cc.initialise({
                cookies: {
                    analytics: {
                        title: 'Analítica',
                        description: 'De manera anónima analizamos su u'+
                        'so de este sitio web con el fi'+
                        'n de mejorar su experiencia.'
                    }
                },
                settings: {
                    consenttype: "implicit",
                    bannerPosition: "bottom",
                    onlyshowbanneronce: true,
                    disableallsites: true
                },
                strings: {
                    analyticsDefaultTitle: 'Analítica',
                    analyticsDefaultDescription: 'De manera anónima analizamos su uso de este sitio web con el fin de mejorar su experiencia.',
                    closeWindow: 'Cerrar',
                    learnMore: 'Más información',
                    notificationTitleImplicit: 'Usamos cookies para asegurar que obtiene una mejor experiencia en nuestro sitio web.',
                    notificationTitle: 'Su experiencia en este sitio web mejorará permitiendo el uso, de cookies.',
                    seeDetails: 'ver detalles',
                    customCookie: 'Este sitio web usa un tipo personalizado de cookies que nece,sita aprobación específica.',
                    seeDetailsImplicit: 'cambie sus preferencias',
                    hideDetails: 'ocultar detalles',
                    allowCookies: 'Permitir cookies',
                    allowCookiesImplicit: 'Cerrar',
                    allowForAllSites: 'Permitir cookies para todos los sitios',
                    savePreference: 'Guardar preferencias',
                    saveForAllSites: 'Guardar para todos los sitios',
                    privacySettings: 'Preferencias de privacidad',
                    privacySettingsDialogTitleA: 'Preferencias de privacidad',
                    privacySettingsDialogSubtitle: 'Algunas características de este sitio necesitan tu consentimiento para recordarle.',
                    privacySettingsDialogTitleB: 'para este sitio web',
                    preferenceConsent: 'Consiento',
                    preferenceDecline: 'Declino',
                    notUsingCookies: 'Este sitio web no usará cookies.'
                }
            });
            // ]]>
        // End Cookie Consent plugin

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
