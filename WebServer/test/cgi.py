import os
import sys

def run_with_cgi(app, charset=None):
    environ = dict(os.environ.items())
    environ['wsgi.charset'] = charset
    environ['wsgi.input'] = sys.stdin
    environ['wsgi.errors']  = sys.stderr
    environ['wsgi.version'] = (1,0)
    environ['wsgi.multithread'] = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once'] = True

    if environ.get('HTTPS','off').lower() in ('on','1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'

    headers_set = []
    headers_sent = []

    def write(data):
        if not headers_set:
             raise AssertionError('write() before start_response()')
        elif not headers_sent:
             status, response_headers = headers_sent[:] = headers_set
             sys.stdout.write('Status: %s\r\n' % status)
             for header in response_headers:
                 sys.stdout.write('%s: %s\r\n' % header)
             sys.stdout.write('\r\n')
        if isinstance(data, unicode):
            charset = environ['wsgi.charset']
            if charset is None:
                raise AssertionError('application returned unicode without '
                                     'defined charset')
            data = data.encode(charset)
        sys.stdout.write(data)
        sys.stdout.flush()

    def start_response(status,response_headers,exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    raise exc_info[0], exc_info[1], exc_info[2]
            finally:
                exc_info = None
        elif headers_set:
            raise AssertionError('Headers already set!')
        headers_set[:] = [status,response_headers]
        return write

    result = app(environ, start_response)
    try:
        for data in result:
            if data:
                write(data)
        if not headers_sent:
            write('')
    finally:
        if hasattr(result,'close'):
            result.close()