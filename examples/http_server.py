import time
import http.server  
import socketserver  

PORT = 8282
  
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):  
    def do_GET(self):  
        # 处理GET请求的逻辑  
        print("GET request received")  
        time.sleep(30)
        # 调用父类的do_GET方法处理请求  
        super().do_GET()  
  
Handler = MyHttpRequestHandler  

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:  
    print(f"Serving at port {PORT}")  
    httpd.serve_forever()