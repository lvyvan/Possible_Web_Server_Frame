# 静态文件处理
'''

'''

'''
if httpRequest.url == '/':
    httpRequest.url == self.index
if httpRequest.GetFileType() != 'wop':   # web of python
    # static
    response = self.staticFile(httpRequest)
else:
    # .wop
    print("wop")
    response = self.wopFile(httpRequest)
'''

'''
    parameList = list
    if '&' in parame:
        parameList = parame.split('&')
    else:
        parameList = parameList.append(parame)
    for item in parameList:
        key, value = item.split('=')
        self.urlParameDic[key] = value
else:
    self.url = self.requestUrl

# 赋值
self.host = self.httpRequestDir.get("Host", None)
'''

'''
environ['REQUEST_METHOD'] = None
        # HTTP请求方法，例如GET或POST。这不可能是一个空字符串，因此总是需要。

        environ['SCRIPT_NAME'] = None
        # 请求URL的“路径”的初始部分，它对应于应用程序对象，以便应用程序知道其虚拟“位置”。
        # 如果应用程序对应于服务器的“根”，则这可以是空字符串。

        environ['PATH_INFO'] = None
        # 请求URL的“路径”的其余部分，指定应用程序中请求目标的虚拟“位置”。
        # 如果请求URL以应用程序根目标为止，并且没有尾部斜杠，则此字符串可能为空字符串。

        environ['QUERY_STRING'] = None
        # 请求URL中 "?" 后面的部分，如果有的话。 可能是空的或缺席。
        
        environ['CONTENT_TYPE'] = None
        # Content-TypeHTTP请求中任何字段的内容。可能是空的或缺席。

        environ['CONTENT_LENGTH'] = None

        environ['SERVER_NAME'] = None
        environ['SERVER_PORT'] = '80'
        # 与SCRIPT_NAME和PATH_INFO结合使用时，可以使用这些变量来完成URL。 
        # 但请注意，HTTP_HOST（如果存在）应优先于SERVER_NAME用于重建请求URL。 
        # 有关更多详细信息，请参阅下面的URL重建部分。
        # SERVER_NAME和SERVER_PORT永远不能是空字符串，因此始终是必需的。
        '''
        '''
        from urllib import quote
        url = environ['wsgi.url_scheme']+'://'

        if environ.get('HTTP_HOST'):
            url += environ['HTTP_HOST']
        else:
            url += environ['SERVER_NAME']

            if environ['wsgi.url_scheme'] == 'https':
                if environ['SERVER_PORT'] != '443':
                url += ':' + environ['SERVER_PORT']
            else:
                if environ['SERVER_PORT'] != '80':
                url += ':' + environ['SERVER_PORT']

        url += quote(environ.get('SCRIPT_NAME', ''))
        url += quote(environ.get('PATH_INFO', ''))
        if environ.get('QUERY_STRING'):
            url += '?' + environ['QUERY_STRING']
        '''
        '''
        environ['SERVER_PROTOCOL'] = None
        # 客户端用于发送请求的协议版本。 通常，这将类似于“HTTP / 1.0”或“HTTP / 1.1”，
        # 并且应用程序可以使用它来确定如何处理任何HTTP请求标头。 
        #（此变量可能应该称为REQUEST_PROTOCOL，因为它表示请求中使用的协议，
        # 并不一定是服务器响应中使用的协议。但是，为了与CGI兼容，我们必须保留现有名称。）

        # HTTP_ Variables
        # 对应于客户端提供的HTTP请求标头的变量（即名称以“HTTP_”开头的变量）。 
        # 这些变量的存在与否应与请求中是否存在适当的HTTP头相对应

        # 服务器或网关应尝试提供适用的其他CGI变量。 
        # 此外，如果正在使用SSL，则服务器或网关还应提供尽可能多的适用的Apache SSL环境变量，例如HTTPS = on和SSL_PROTOCOL。 
        # 但请注意，使用除上面列出的CGI变量之外的任何CGI变量的应用程序必然不可移植到不支持相关扩展的Web服务器。 
        # （例如，不发布文件的Web服务器将无法提供有意义的DOCUMENT_ROOT或PATH_TRANSLATED。）

        # 符合WSGI的服务器或网关应记录它提供的变量及其定义。 
        # 应用程序应检查是否存在所需的任何变量，并在没有此类变量的情况下制定备用计划。

        # 注意：缺少变量（例如未发生身份验证时的REMOTE_USER）应该不在environ词典中。
        # 另请注意，CGI定义的变量必须是字符串，如果它们存在的话。 如果CGI变量的值不是str，则违反此规范。

        # 除了CGI定义的变量之外，environ字典还可以包含任意操作系统“环境变量”，并且必须包含以下WSGI定义的变量：

        environ['wsgi.version'] = (1, 0)
        # 元组（1,0），代表WSGI版本1.0。

        environ['wsgi.url_scheme'] = None
        # 一个字符串，表示调用应用程序的URL的“方案”部分。
        # 通常，这将具有值“http”或“https”，视情况而定。

        environ['wsgi.input'] = None
        # 可以从中读取HTTP请求正文的输入流（类文件对象）。
        #（服务器或网关可以按照应用程序的请求执行按需读取，
        # 或者它可以预先读取客户端的请求主体并将其缓冲在内存中或磁盘上，
        # 或者使用任何其他技术来提供这样的输入流， 它的偏好。）

        environ['wsgi.errors'] = None
        # 可以从中读取HTTP请求正文的输入流（类文件对象）。 
        # （服务器或网关可以根据应用程序的请求执行按需读取，
        # 或者可以写入错误输出的输出流（类文件对象），
        # 以便在标准化和可能集中的情况下记录程序或其他错误 
        # 这应该是一个“文本模式”流;即，应用程序应使用“\ n”作为行结尾，
        # 并假设它将被转换为由服务器/网关结束的正确行。
        # 对于许多服务器，wsgi.errors将是服务器的主错误日志。
        #  或者，这可能是sys.stderr，或某种日志文件。 
        # 服务器的文档应包括如何配置此文件或在何处查找记录的输出的说明。 
        # 如果需要，服务器或网关可以向不同的应用程序提供不同的错误流。

        environ['wsgi.multithread'] = None
        # 如果应用程序对象可能由同一进程中的另一个线程同时调用，
        # 则此值应该为true，否则应该为false。

        environ['wsgi.multiprocess'] = None
        # 如果另一个进程可以同时调用等效的应用程序对象，
        # 则该值应该为true，否则应该为false。

        environ['wsgi.run_once'] = None
        # 如果服务器或网关期望（但不保证！）应用程序将仅在其包含进程的生命周期内调用一次，
        # 则此值应评估为true。 
        # 通常，这仅适用于基于CGI（或类似的东西）的网关。
'''

'''
sql = "select * from info"
count, infos = self.sqlhelper.select(sql)
info = infos.fetchall()
inputButton = "<td><input type='button' value='添加' id='toAdd' name='toAdd' systemidvaule='%s'></td>"
htmlTdTemp = "<tr>" + "<td>%s</td>" * 8 + inputButton + "</tr>"
htmlTbody = ""
for item in info:
    htmlTbody += htmlTdTemp %(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[1])
    
content = self.templates.retContent("index.html", {r"@%content%": htmlTbody, })
''' 