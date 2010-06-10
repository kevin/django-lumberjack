from django.conf import settings

LOGGING = {
    'formatters': {
        'error':{
            '()':'lumberjack.formatters.tb.TracebackFormatter',
            'output':'terminal',
            },
        'sql' : {
            '()':'lumberjack.formatters.sql.SQLFormatter',
            'format':'[%(name)s] %(levelname)s (%(duration)sms) %(message)s',
            'output':'terminal',
        },
        'ajax' : {
            '()':'lumberjack.formatters.ajax.AjaxFormatter',
            'format':'[%(name)s] %(levelname)s %(message)s',
            'output':'terminal',
        },
        'default' : {
            'format' : '[%(name)s] %(levelname)s %(message)s',
        },
    },
    'handlers' : {
        'sqlstream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'sql',
        },
        'errorstream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'error',
            },
        'ajaxstream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'ajax',
            },
        'stream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'default',
        },
    },
    'loggers' : {
        'django.db' : {
            'level' : 'DEBUG',
            'handlers' : ['sqlstream'],   #add additional handlers here (ie:email)
            },
        'django.errors' : {
            'level' : 'DEBUG',
            'handlers' : ['errorstream'],   #add additional handlers here (ie:email)
            },
        'django.ajax' :{
            'level' : 'DEBUG',
            'handlers' : ['ajaxstream'],
            },
        },
}

LOGGING = getattr(settings, 'LOGGING', LOGGING)