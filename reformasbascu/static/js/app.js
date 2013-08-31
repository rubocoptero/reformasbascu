requirejs.config({
    paths: {
        jquery: [
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'lib/jquery-1.9.1.min'
        ],
        bootstrap : 'lib/bootstrap.min'
    },
    shim: {
        'bootstrap': {
            deps: ['jquery'],
            exports: 'jQuery.fn.carousel'
        },
        'lib/jquery.stapel': {
            deps: ['jquery'],
            exports: 'jQuery.fn.stapel'
        },
        'lib/jquery.colorbox-min': {
            deps: ['jquery'],
            exports: 'jQuery.fn.colorbox'
        }
    }
});

requirejs(["app/main"]);

