import http.server
import socketserver
import urllib.request
 
# 创建自定义请求处理类
class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 处理GET请求
        # url = self.path[1:]  # 获取去掉前导斜杠的URL
        # response = urllib.request.urlopen(url)
        # content = response.read()
 
        # 发送响应
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')
 
    def do_POST(self):
        # 处理POST请求
        # 实现自定义逻辑
        pass
 
# 创建HTTPServer实例，并将自定义请求处理类传递给它
server_address = ('localhost', 8000)  # 监听所有可用的接口
httpd = socketserver.TCPServer(server_address, ProxyHandler)
 
# 启动HTTP服务器
httpd.serve_forever()