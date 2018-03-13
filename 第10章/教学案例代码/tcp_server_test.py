from socketserver import BaseRequestHandler, TCPServer, ThreadingTCPServer
class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("connection from %s" % str(self.client_address))
        while True:
            msg = self.request.recv(4096)  # 获得客户端请求来的消息
            if not msg:            # 如果服务器接收到空消息，则跳出循环，结束此会话
                break
            print("来自客户端消息：%s" % str(msg, "utf-8"))
            self.request.send(msg)  # 接收到的消息发送回去

if __name__ == "__main__":
    # server = TCPServer(("", 9995), EchoHandler)
    server = ThreadingTCPServer(("", 9995), EchoHandler)
    server.serve_forever()
