'''
# The application interface is a callable object 应用程序接口是可调用对象
def application (
    # 它接受两个参数：
    # environ指向包含CGI环境的字典
    # 变量由服务器为每个变量填充
    # 收到客户的请求
    environ,
    # start_response is a callback function supplied by the server
    # which takes the HTTP status and headers as arguments
    # start_response是服务器提供的回调函数
    # 它将HTTP状态和标头作为参数
    start_response
):

    # 可能构建响应主体
    # 使用提供的环境字典
    response_body = 'Request method: %s' % environ['REQUEST_METHOD']

    # HTTP响应代码和消息
    status = '200 OK'

    # 客户端期望的HTTP标头
    # 必须将它们包装为一组元组：
    # [(Header name, Header value)].
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    # 使用提供的功能将它们发送到服务器
    start_response(status, response_headers)

    # 返回响应正文。 注意它被包裹了
    # 在列表中虽然它可以是任何可迭代的。
    return [response_body]

#----------------------------
#   2019年3月16日
#----------------------------

#! /usr/bin/env python

# Python捆绑的WSGI服务器
from wsgiref.simple_server import make_server

def application (environ, start_response):

    # ＃对环境键，值对进行排序和字符串化
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]

# 实例化服务器
httpd = make_server (
    'localhost', # 主机名
    8051, # 端口号等待请求的位置
    application # 应用程序对象名称，在本例中是一个函数
)

# 等待一个请求，提供服务并退出
httpd.handle_request()

#!/usr/bin/env python
'''
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="get" action="">
        <p>
           Age: <input type="text" name="age" value="%(age)s">
        </p>
        <p>
            Hobbies:
            <input
                name="hobbies" type="checkbox" value="software"
                %(checked-software)s
            > Software
            <input
                name="hobbies" type="checkbox" value="tunning"
                %(checked-tunning)s
            > Auto Tunning
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    <p>
        Age: %(age)s<br>
        Hobbies: %(hobbies)s
    </p>
</body>
</html>
"""

def application (environ, start_response):

    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    # As there can be more than one value for a variable then
    # a list is provided as a default value.
    age = d.get('age', [''])[0] # Returns the first age value
    hobbies = d.get('hobbies', []) # Returns a list of hobbies

    # Always escape user input to avoid script injection
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % { # Fill the above html template in
        'checked-software': ('', 'checked')['software' in hobbies],
        'checked-tunning': ('', 'checked')['tunning' in hobbies],
        'age': age or 'Empty',
        'hobbies': ', '.join(hobbies or ['No Hobbies?'])
    }

    status = '200 OK'

    # Now content type is text/html
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

httpd = make_server('localhost', 8051, application)

# Now it is serve_forever() in instead of handle_request()
httpd.serve_forever()