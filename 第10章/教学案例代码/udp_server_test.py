from socketserver import BaseRequestHandler, UDPServer
import time
class TimeHandler(BaseRequestHandler):
    def handle(self):
        print("got connection from", self.client_address)
        msg, sock = self.request
        print("receive from %s: %s" % (str(self.client_address), msg))
        resp = time.ctime()
        sock.sendto(resp.encode("utf-8"), self.client_address)

if __name__ == "__main__":
    server = UDPServer(("", 8885), TimeHandler)
    server.serve_forever()
