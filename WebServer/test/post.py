# 通常application/x-www-form-urlencoded或在有文件上载时multipart/form-data
def is_post_request(environ):
    if environ['REQUEST_METHOD'].upper() != 'POST':
        return False
    content_type = environ.get('CONTENT_TYPE', 'application/x-www-form-urlencoded')
    return (content_type.startswith('application/x-www-form-urlencoded' or content_type.startswith('multipart/form-data'))
# 关于对 post 处理 https://wsgi.readthedocs.io/en/latest/specifications/handling_post_forms.html